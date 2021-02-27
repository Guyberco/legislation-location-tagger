import copy
from src.dictionary import getLocationToTagByAcronym, getLocationToTagByAcronymHEBREW
from src.googleTrans import tranlsateText
from deep_translator import GoogleTranslator


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
            self.db.update({wordInText: {"counter": 0, "instancesToTag": [], "tagToAddHebrew": location, "tagToAddEnglish": translateLoctionToTag(location)}})
        else:
            self.db.update({wordInText: {"counter": 0, "instancesToTag": [], "tagToAddHebrew": getLocationToTagByAcronymHEBREW(location), "tagToAddEnglish": locationToTagAcronym}})

    def put(self, entry):
        self.db.update(entry)

    def clearCounter(self, key):
        """
        set the counter value of the key in the db to zero
        :param key:
        """
        value = self.db[key]
        if value:
            value['counter'] = 0

    def clearAllCounters(self):
        """
        set count to zero for all keys in the db
        """
        for key in self.db.keys():
            self.clearCounter(key)

    def increaseCounter(self, word):
        """
        increase counter for a given key in the db
        :param word:
        """
        location = self.db.get(word)
        if location:
            location["counter"] += 1

def apppendLocationOcc(word, counter):
    word["instancesToTag"].append(counter)


def translateLoctionToTag(location):
    """
    :param location: string in hebrew for a location
    :return: the translated string in english
    """
    translatedText = tranlsateText("אני גר " + location)
    return "_".join(translatedText.split()[3:])



def updateWord(word, columns):
    """
    increment by 1 the counter filed for the given key. if the word in the list is also a location - add its occurance
    number to the list of occurrences
    :param word: key in the db
    :param columns: list of strings
    """
    counter = word["counter"]
    word["counter"] = counter + 1
    if(buildWordThatHasLocTags(columns)):
        apppendLocationOcc(word, counter)

def checkTagInColumns(columns, findWord):
    """
    :param columns: list of strings
    :param findWord: string to lookup
    :return: true if string is in the list
    """
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
            if not (i-1 == indx or wordAsInText == '-' or (len(aggregatedWord)>1 and aggregatedWord[-1] == '-')):
                aggregatedWord += " "
                aggregatedWordToTag += " "
            aggregatedWord += wordAsInText
            aggregatedWordToTag += wordToTag
        else:
            break
    return (i, aggregatedWord, aggregatedWordToTag)


