import copy
from src.dictionary import loc_dictionray

class DataBase:
    def __init__(self):
        self.db = {}

    def getDBCopy(self):
        return copy.deepcopy(self.db)
        
    def getValueByKey(self, location):
        return self.db.get(location)

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
    """
    check if the given list of strings (represents an entry in the NRE output) is a location
    returns true the 4th element is "properName", the word(first element) is contained in the loc dictionary
    and contains an element "I_LOC" (should be located from the 4th index)
    :param columns: list of strings
    :return: BOOLEAN
    """
    if len(columns) >= 4 and columns[4] == "properName":
        if loc_dictionray.checkValue(columns[1]):
            for word in columns[3:]:
                if word == "I_LOC":
                    return True
    return False



