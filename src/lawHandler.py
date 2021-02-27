import codecs
from src.DataBase import buildWordThatHasLocTags, DataBase
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


def getNextNonEmptyLine(lines, indx):
    """
    from the given index - indx, go through the list lines and return the next non empty line, if function reaches
    the end of the list return -1
    :param lines: list with strings
    :param indx: index in the list lines
    :return:
    """
    while indx < len(lines):
        if not len(lines[indx].split()) < 3:
            return indx
        else:
            indx += 1
    return -1


def seekLastWordDup(lines, indx):
    """
    check for the next duplicate word of lines[indx] if no such word exists return -1
    :param lines: list of strings
    :param indx: index in the list
    :return:
    """
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
    """
    go through the lines of the file, for each word if is part is key in the db, increment the counter in the db,
    if the the word also appears as location in its occurrence in the file, add it's occurrence counter to the list of occurrence in the db
    :param file: LDA tagged txt file
    :param db: database with locations
    :return:
    """
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
    """
    given the filePath create a data base that contains all the locations in the filed, occurrences in the file that
    we want to tag and tag information we want to add.
    :param filePath: file path for the LDA tagged file
    """
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