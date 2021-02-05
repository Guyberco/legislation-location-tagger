import copy
from src.dictionary import getLocationToTagByAcronym
from src.googleTrans import tranlsateText


class DataBase:
    def __init__(self):
        self.db = {}

    def getDictionaryDeepCopy(self):
        return copy.deepcopy(self.db)

    def getDBDeepCopy(self):
        return copy.deepcopy(self)
        
    def getValueByKey(self, location):
        return self.db.get(location)

    def getCounterByKey(self, location):
        return self.db.get(location).get("counter")

    def getKeys(self):
        return self.db.keys()

    def isKey(self, key):
        return key in self.db.keys()

    def updateAsLocationOcc(self, wordInText):
        location = self.getValueByKey(wordInText)
        apppendLocationOcc(location, self.getCounterByKey(wordInText))

    def createNewLocationEntry(self, location, wordInText):
        locationToTagAcronym = getLocationToTagByAcronym(location)
        if locationToTagAcronym is None:
            translateLoctionToTag(location)
            self.db.update({wordInText: {"counter": 0, "instancesToTag": [], "tagToAdd": location}})
        else:
            self.db.update({wordInText: {"counter": 0, "instancesToTag": [], "tagToAdd": locationToTagAcronym}})

    def put(self, entry):
        self.db.update(entry)

    def clearCounter(self, key):
        value = self.db[key]
        if value:
            value['counter'] = 0

    def clearAllCounters(self):
        for key in self.db.keys():
            self.clearCounter(key)

    def increaseCounter(self, word):
        location = self.db.get(word)
        if location:
            location["counter"] += 1

def apppendLocationOcc(word, counter):
    word["instancesToTag"].append(counter)


def translateLoctionToTag(location):
    return tranlsateText("אני גר" + location)

def updateWord(word, columns):
    counter = word["counter"]
    word["counter"] = counter + 1
    if(buildWordThatHasLocTags(columns)):
        apppendLocationOcc(word, counter)

def checkTagInColumns(columns, findWord):
    for word in columns:
        if findWord == word:
            return True
    return False


def buildWordThatHasLocTags(list, indx):
    """
    check if the given list of strings (represents an entry in the NRE output) is a location
    returns true the 4th element is "properName", the word(first element) is contained in the loc dictionary
    and contains an element "I_LOC" (should be located from the 4th index)
    :param columns: list of strings
    :return: indx - the next line to check, aggregatedWord loc key to put , aggregatedWordToTag - word to tag
    if not found both aggregatedWord, aggregatedWordToTag are ""
    """
    aggregatedWord = ''
    aggregatedWordToTag = ''
    i = indx
    while i < len(list):
        columns = list[i].split()
        i += 1
        if len(columns) < 3:
            continue
        wordAsInText = columns[3]
        wordToTag = columns[1]
        if checkTagInColumns(columns, "I_LOC") and checkTagInColumns(columns, "properName"):
            if not (i-1 == indx or wordAsInText == '-' or aggregatedWord[-1] == '-'):
                aggregatedWord += " "
                aggregatedWordToTag += " "
            aggregatedWord += wordAsInText
            aggregatedWordToTag += wordToTag
        else:
            break
    return (i, aggregatedWord, aggregatedWordToTag)

print(translateLoctionToTag("באר שבע"))