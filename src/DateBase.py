import copy

class DataBase:
    def __init__(self):
        self.db = {}

    def getDBCopy(self):
        return copy.deepcopy(self.db)
        
    def getValueByKey(self, location):
        return self.db[location]

    def getKeys(self):
        return self.db.keys()

    def createNewLocationEntry(self, location):
        self.db.update({location: {"counter": 0, "instancesToTag": []}})

    def put(self, entry):
        self.db.update(entry)

    def clearCounter(self, key):
        value = self.db[key]
        if value:
            value['counter'] = 0

    def clearAllCounters(self):
        for key in self.db.keys():
            self.clearCounter(key)

def apppendLocationOcc(word, counter):
    word["instancesToTag"].append(counter)


def updateWord(word, columns):
    counter = word["counter"]
    word["counter"] = counter + 1
    if(isLocationOcc(columns)):
        apppendLocationOcc(word, counter)


def isLocationOcc(columns):
    return len(columns) >= 3 and columns[2] == "I_LOC"


