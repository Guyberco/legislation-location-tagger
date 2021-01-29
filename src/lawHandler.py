import codecs
from src.DataBase import updateWord, buildWordThatHasLocTags, DataBase, apppendLocationOcc

#TODO
# things that dont work ארץ-ישראל, באר-שבע
# work- ארץ ישראל  - it tags ישראל which is fine/
from src.dictionary import loc_dictionray


def initializeDataBase(file, dataBase):
    """
    go through the file(NRE output) and for each line check if had a location tag, if so add it to the db.
    :param file: contains the NRE output
    :param dataBase: empty dataBase
    """
    lines = file.readlines()
    indx = 0
    while indx < len(lines):
        columns = lines[indx].split()
        (newIndex, aggregatedWord, aggregatedWordToTag) = buildWordThatHasLocTags(lines, indx)
        if not aggregatedWord == '' and loc_dictionray.checkValue(aggregatedWordToTag):
            dataBase.createNewLocationEntry(aggregatedWordToTag, aggregatedWord)
            indx = newIndex
        else:
            indx += 1






# def checkForLocKey(db, lines, indx):
#     """
#     given an index in the lines, check if the word in lines[indx] is a key in the db, is so increase the counter in the db.
#     Also if the word appears as a location add the current counter value to the occurrence list in the db.
#     :param db:  database of words that are locations
#     :param lines: all the lines of the file (file here is the output of the tagger)
#     :param indx: index of line we check
#     :return: index of the next word to check in lines
#     """
#     increase_counter_flag = False
#     line = lines[indx]
#     columns = line.split()
#     if len(columns) < 4:
#         return indx+1
#     line_num = columns[0]    # index of line (if we have more than one entry for a word then the next lines would have the same index)
#     word = columns[3]     # the word as it appears in the xml
#     while len(columns) >= 3 and line_num == columns[0]:
#         location = db.getValueByKey(word)
#         # the word appears in the db so increase the counter before exiting the function
#         if location:
#             increase_counter_flag = True
#             # check if this key occurrence is tagged as location if so add the counter value to the occurrence list
#             if CheckLocationOcc(columns):
#                 apppendLocationOcc(location, db.getCounterByKey(word))
#         indx += 1
#         if not indx < len(lines):
#             break
#         line = lines[indx]
#         columns = line.split()
#     # if the word is a key in the db, increase the counter for this key in the db
#     if increase_counter_flag:
#         db.increaseCounter(word)
#     return indx



# def updateOccurances(file, dataBase):
#     """
#     go through the file and for each word that is key in the db (location word), increase the counter for that key in the db. determine if the word context is
#     a location and if so add the current counter value to the "instancesToTag" list
#     each key entrance is composed of ( counter:int , instancesToTag:int[] )
#     :param file: contains the NRE output
#     :param dataBase: initialized database with all the location keys
#     """
#     lines = file.readlines()
#     indx = 0
#     while indx < len(lines):
#         indx = checkForLocKey(dataBase, lines, indx)

def getNextNonEmptyLine(lines, indx):
    while indx < len(lines):
        if not len(lines[indx].split()) < 3:
            return indx
        else:
            indx += 1
    return -1


def seekLastWordDup(lines, indx):
    indx = getNextNonEmptyLine(lines, indx)
    if indx == -1:
        return -1
    columns = lines[indx].split()
    lineNum = columns[0]
    while indx + 1 < len(lines):
        nextLinecolumns = lines[indx + 1].split()
        if len(nextLinecolumns) < 3 or not nextLinecolumns[0] == lineNum:
            return indx
        indx += 1
    return indx



def updateOccurances(file, db):
    lines = file.readlines()
    indx = 0

    while indx < len(lines):
        indx = seekLastWordDup(lines, indx)
        if indx == -1:
            break;
        (newIndex, aggregatedWord, aggregatedWordToTag) = buildWordThatHasLocTags(lines, indx)
        if db.isKey(aggregatedWord):
            if loc_dictionray.checkValue(aggregatedWordToTag): # if aggratedWord is location
                db.updateAsLocationOcc(aggregatedWord)
                indx = newIndex
            db.increaseCounter(aggregatedWord)
        else:
            indx += 1


def createDataOfLocs(filePath):
    dataBase = DataBase()
    # file =  open(FilePath, mode='r',encoding='UTF-8').read()
    file = codecs.open(filePath, 'r', 'utf8')
    initializeDataBase(file, dataBase)
    file.close()
    file = codecs.open(filePath, 'r', 'utf8')   # It is necessary to reopen the file
    updateOccurances(file, dataBase)
    file.close()
    dataBase.clearAllCounters()
    return dataBase