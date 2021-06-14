import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QMessageBox

from DB.db import DB


class WorkExpo:
    def __init__(self, window, coll=None, db=None):
        self.coll = coll
        self.autors = coll.Autors
        self.window = window
        self.db = db

    def export(self, ids, mode):
        filename, ok = QFileDialog.getSaveFileName(self.window,
                                                   "Сохранить файл",
                                                   ".",
                                                   "All Files(*.*)")
        count = 0
        if (ok):
            default_out = sys.stdout
            outfile = open(filename, 'w', encoding='utf-8')
            sys.stdout = outfile
        else:
            print("file was not selected!")
            return
        if mode == 1:       #xx,yy
            ids = [int(id) for id in ids]
            for e in self.coll.Exponats:
                if e.id in ids:
                    print(e.getStringToSaveForFile(self.coll))
                    print(e, file=sys.stderr)
                    count += 1
            if count != len(ids):
                QtWidgets.QMessageBox.warning(self.window, "Предупреждение",
                                              "Не все экспонаты с указанными id найдены в базе!",
                                              buttons=QtWidgets.QMessageBox.Cancel)
        elif mode == 2:     #xx-yy
            startid = int(ids[0])
            endid = int(ids[1])
            for id in range(startid, endid+1):
                for e in self.coll.Exponats:
                    if int(e.id) == id:
                        print(e.getStringToSaveForFile(self.coll))
                        print(e, file=sys.stderr)
                        count += 1
            if count != endid - startid + 1:
                QtWidgets.QMessageBox.warning(self.window, "Предупреждение",
                                              "Не все экспонаты с указанными id найдены в базе!",
                                              buttons=QtWidgets.QMessageBox.Cancel)
        elif mode == 3:     #xx
            for e in self.coll.Exponats:
                if e.id == int(ids):
                    print(e.getStringToSaveForFile(self.coll))
                    print(e, file=sys.stderr)
                    count += 1
            if count == 0:
                QtWidgets.QMessageBox.warning(self.window, "Предупреждение",
                                              "Экспонат с указанным id не найден в базе!",
                                              buttons=QtWidgets.QMessageBox.Cancel)
        if count != 0:
            QtWidgets.QMessageBox.information(self.window, "Файл создан",
                                      "Был создан файл: %s" % (filename),
                                      buttons=QtWidgets.QMessageBox.Ok)

        sys.stdout = default_out
        outfile.close()

    def import_from_file(self):
        '''Вернет количество успешно импортированных экспонатов'''
        filename, filetype = QFileDialog.getOpenFileName(self.window,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt); ;All Files(*)")
        try:
            f = open(filename, 'r', encoding='utf-8')
            db = DB()
            strips = [line.strip() for line in f]
            f.close()
        except FileNotFoundError:
            print('No such file or directory')
            return 0

        succes = False
        count = 0
        for s in strips:
            start_autor = s.find("//")
            end_autor = s.rfind("//")
            autor_id = s[start_autor+2:end_autor]
            #подготовка строки к запросу
            expo_s = s.replace("//", "")
            print(autor_id)
            print(expo_s, '\n')

            succes = db.insertExpo(expo_s)
            if not succes:
                break
            else:
                count += 1

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText('Успешно импортировано экспонатов: %d' % (count))
        msg.setWindowTitle("Импорт")
        msg.exec_()

        return count


    '''
    def is_id_in_autors(self, id):
        for a in self.autors:
            if id == a.id:
                return True
        return False
    '''