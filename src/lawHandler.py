import codecs
from src.DataBase import updateWord, isLocationOcc, DataBase

def initializeDataBase(file, dataBase):
    """
    go through the file(NRE output) and for each line check if had a location tag, if so add it to the db.
    :param file: contains the NRE output
    :param dataBase: empty dataBase
    """
    for line in file:
        columns = line.split()
        if(isLocationOcc(columns)):
            dataBase.createNewLocationEntry(columns[1])


def updateOccurances(file, dataBase):
    """
    go through the file and for each word that is key in the db (location word), increase the counter for that key in the db. determine if the word context is
    a location and if so add the current counter value to the "instancesToTag" list
    each key entrance is composed of ( counter:int , instancesToTag:int[] )
    :param file: contains the NRE output
    :param dataBase: initialized database with all the location keys
    """
    for line in file:
        columns = line.split()
        if len(columns) >= 1:
            word = dataBase.getValueByKey(columns[0])
            if word:
                updateWord(word, columns)


def createDataOfLocs(FilePath):
    dataBase = DataBase()
    # file =  open(FilePath, mode='r',encoding='UTF-8').read()
    file = codecs.open(FilePath, 'r', 'utf8')
    initializeDataBase(file, dataBase)              #TODO add also complex words like bear - sheva or tel aviv
    file = codecs.open(FilePath, 'r', 'utf8')
    updateOccurances(file, dataBase)                #TODO updateWord meathod need to be changed
    dataBase.clearAllCounters()
    return dataBase
   

# createDataOfLocs("../TextFiles/output/out1.txt")