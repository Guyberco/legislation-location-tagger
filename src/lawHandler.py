import codecs

dataBase = {}

def initializeDataBase(file):
    for line in file:
        columns = line.split()
        if(isLocationOcc(columns)):
            dataBase.update({columns[0] : {"counter" : 0, "indexOfOoccurrence": [] }})
    # print(dataBase)

def updateOccurances(file):
    for line in file:
        columns = line.split()
        if(len(columns) >= 1):
            word = dataBase.get(columns[0])
            if(word):
                updateWord(word, columns)
    print(dataBase)

def updateWord(word, columns):
    counter = word["counter"]
    word["counter"] = counter + 1
    if(isLocationOcc(columns)):
        apppendLocationOcc(word, counter)

def isLocationOcc(columns):
    return len(columns) >= 3 and columns[2] == "I_LOC"

def apppendLocationOcc(word, counter):
    word["indexOfOoccurrence"].append(counter)
       
def createDataOfLocs(FilePath):
    # file =  open(FilePath, mode='r',encoding='UTF-8').read()
    file = codecs.open(FilePath, 'r', 'utf8')
    initializeDataBase(file)
    file = codecs.open(FilePath, 'r', 'utf8')
    updateOccurances(file)
   

createDataOfLocs("../TextFiles/output/out1.txt")