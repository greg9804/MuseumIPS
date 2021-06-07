

class Search:
    def __init__(self, params):
        self.params = params

    def start(self):
        for k, v in self.params.items():
            print(k, v)