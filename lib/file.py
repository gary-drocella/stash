class File:
    def __init__(self, data, index):
        self.data = data
        self.index = index
    
    def getData(self):
        return self.data
    
    def getIndex(self):
        return self.index