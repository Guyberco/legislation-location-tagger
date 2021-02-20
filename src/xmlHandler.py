import xml.etree.ElementTree as ET
import re
import src.stringHelper as stringHelper
# from lawHandler import dataBase
from env import envPath
from src.DataBase import updateWord, buildWordThatHasLocTags, DataBase
import codecs

from src.googleTrans import checkIsLocationInTranslate


def tagDesignatedLocations(string, locationObj, LocationKey):
    index = 0
    instancesToTag = locationObj["instancesToTag"]
    locationToTagEnglish = locationObj["tagToAddEnglish"]
    locationToTagHebrew = locationObj["tagToAddHebrew"]
    locationToTagLen = len(LocationKey)

    while index < len(string) and len(instancesToTag) > 0:  # keep len calculation inside thw while
        foundIndex = string.find(f" {LocationKey}", index)
        if foundIndex == -1:
            break
        else:
            if shouldWrapCurrentInstance(locationObj["counter"], instancesToTag[0]):  # validate that the list locationObj["instancesToTag"] isnt empty
                instancesToTag.pop(0)
                if verifyInGoogleContext(string, LocationKey):
                    openingTag = createLocationOpenTag(locationToTagEnglish, locationToTagHebrew)  # add here attribute data
                    closingTag = "</location>"
                    wrappedTargetWord = stringHelper.wrapString(LocationKey, openingTag, closingTag)
                    string = stringHelper.replaceWordAtIndex(string, wrappedTargetWord, foundIndex, locationToTagLen)
                    index = foundIndex + len(wrappedTargetWord)
                else:
                    index = foundIndex + locationToTagLen
            else:
                index = foundIndex + locationToTagLen
            incrementLocationCounter(locationObj)
    return string

def verifyInGoogleContext(string, LocationKey):
    return stringHelper.isAcronym(LocationKey) or stringHelper.isMoreThanOneWord(LocationKey) or checkIsLocationInTranslate(string)


def incrementLocationCounter(locationObj, incrementBy: int = 1):
    locationObj["counter"] += incrementBy

def shouldWrapCurrentInstance(counter: int, currentInstance: int) -> bool:
    return counter == currentInstance

def createLocationOpenTag(locationToTagEnglish, locationToTagHebrew):
    if locationToTagHebrew != '':
        return f"<location refersTo=\"{locationToTagHebrew}\" href=\"https://dbpedia.org/page/{locationToTagEnglish}\">"
    else:
        return "<location>"


def handleXml(path, pathToSave, xmlFileName, db):
    ET.register_namespace('', "http://docs.oasis-open.org/legaldocml/ns/akn/3.0")  # ENV VARIABLE
    fileTree = ET.parse(f"{path}/{xmlFileName}")
    fileRoot = fileTree.getroot()
    mapKeys = db.getKeys()
    for key in mapKeys:
        traverseTree(fileRoot, db.getValueByKey(key), key)
    newFileName = createXmlFileFromTree(pathToSave, xmlFileName, fileTree)
    parseEscapeCharsInXML(f"{pathToSave}/{newFileName}")



def createXmlFileFromTree(path, xmlFileName, tree):
    # openedFile = open(f"{path}/{xmlFileName}", 'w')
    newFileName = f"locationTagged_{xmlFileName}"
    tree.write(f"{path}/{newFileName}", encoding='UTF-8')
    return newFileName

def traverseTree(node, locationObj, locationKey):
    if node.text is not None:
        node.text = tagDesignatedLocations(node.text, locationObj, locationKey)
    for child in node:
        traverseTree(child, locationObj, locationKey)
    if(node.tail is not None):
        node.tail = tagDesignatedLocations(node.tail, locationObj, locationKey)

def parseEscapeCharsInXML(filePath):
    """
    :param filePath: path to xml file
    :return: xml file with fixed parenthesis
    """
    file = open(filePath, mode='r', encoding='UTF-8')
    text = re.sub('&lt;', "<", file.read())
    text = re.sub('&gt;', ">", text)
    file.close()

    with open(filePath, "w+", encoding='UTF-8') as f:
        f.write(text)
        f.close()


def strip_empty_lines(s):
    indx = 0;
    for c in s:
        if indx == 0:
            indx = 1
            continue
        if c == '' or c == '\n' or c == ' ' or c == '\"' or c == '\'':
            indx += 1
        else:
            break
    return s[indx:]

    # lines = s.splitlines("\n")
    # for line in lines:
    #     if line == ' ' or line == "\n":
    #         lines.pop(0)
    # while lines and not lines[0].strip():
    #     lines.pop(0)
    # return '\n'.join(lines)

def extractTextFromXml(path, pathToSave, fileName):
    """
    Given xml file - create a text file without the tags
    :param path: import path - where the original xml
    :param pathToSave: path to the dir where we save the new xml
    :param fileName: original xml file name
    """
    file = open(f"{path}/{fileName}.xml", mode='r', encoding='UTF-8')
    text = re.sub('<[^<]+>', "", file.read())
    file.close()

    with open(f"{pathToSave}/untagged_{fileName}.txt", "w+", encoding='UTF-8') as f:
        f.write(strip_empty_lines(text))
        f.close()



