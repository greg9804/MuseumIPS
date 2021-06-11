from PySide6 import QtCharts, QtCore
import sys, random
from PySide6.QtCharts import QBarSet, QBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView


class Diagramm:
    def __init__(self, window, layout, collection):
        self.window = window
        self.layout = layout
        self.exponats = collection.Exponats
        self.autors = collection.Autors
        self.styles = collection.stylesList

    def render(self):
        #удаляет предыдущий график
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        series = QBarSeries()

        #общее количество экспонатов
        count = 0

        #создание множества распределений
        for s in self.styles:
            set0 = QBarSet(s[1])
            count_of_style = 0
            for e in self.exponats:
                if e.style == s[1]:
                    count_of_style += 1
                    count += 1
            set0.append(count_of_style)
            series.append(set0)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Визуализация распределения количества экспонатов по стилям')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axisX = QBarCategoryAxis()
        axisX.append(tuple([item[1] for item in self.styles]))

        axisY = QValueAxis()
        axisY.setRange(0, count/2)

        chart.addAxis(axisX, QtCore.Qt.AlignBottom)
        chart.addAxis(axisY, QtCore.Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        self.chartView = QChartView(chart)
        self.layout.addWidget(self.chartView)