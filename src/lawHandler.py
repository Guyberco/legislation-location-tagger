import codecs
from DateBase import updateWord, isLocationOcc, DataBase

dataBase = DataBase()

def initializeDataBase(file):
    for line in file:
        columns = line.split()
        if(isLocationOcc(columns)):
            dataBase.createNewLocationEntry(columns[0])


def updateOccurances(file):
    for line in file:
        columns = line.split()
        if len(columns) >= 1:
            word = dataBase.getValueByKey(columns[0])
            if word:
                updateWord(word, columns)


def createDataOfLocs(FilePath):
    # file =  open(FilePath, mode='r',encoding='UTF-8').read()
    file = codecs.open(FilePath, 'r', 'utf8')
    initializeDataBase(file)
    file = codecs.open(FilePath, 'r', 'utf8')
    updateOccurances(file)
    dataBase.clearAllCounters()
   

# createDataOfLocs("../TextFiles/output/out1.txt")