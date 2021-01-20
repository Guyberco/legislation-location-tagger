import codecs
from src.DataBase import updateWord, isLocationOcc, DataBase

def initializeDataBase(file, dataBase):
    for line in file:
        columns = line.split()
        if(isLocationOcc(columns)):
            dataBase.createNewLocationEntry(columns[0])


def updateOccurances(file, dataBase):
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
    initializeDataBase(file, dataBase)
    file = codecs.open(FilePath, 'r', 'utf8')
    updateOccurances(file, dataBase)
    dataBase.clearAllCounters()
    return dataBase
   

# createDataOfLocs("../TextFiles/output/out1.txt")