import xml.etree.ElementTree as ET
import re
import src.stringHelper as stringHelper
from src.googleTrans import checkIsLocationInTranslate


def tagDesignatedLocations(string, locationObj, LocationKey):
    """

    :param string:the string we want to tag with locations
    :param locationObj: object of the location key
    :param LocationKey: the key for the location we want to tag
    :return: tagged string with the locations we found
    """
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
    """
    :param path: path to the original law xml file
    :param pathToSave: path to save the new tagged xml file
    :param xmlFileName: name of the law file
    :param db: database with all the locations data created for this specific xml file
    :return:
    """
    ET.register_namespace('', "http://docs.oasis-open.org/legaldocml/ns/akn/3.0")  # ENV VARIABLE
    fileTree = ET.parse(f"{path}/{xmlFileName}")
    fileRoot = fileTree.getroot()
    mapKeys = db.getKeys()
    for key in mapKeys:
        traverseTree(fileRoot, db.getValueByKey(key), key)
    newFileName = createXmlFileFromTree(pathToSave, xmlFileName, fileTree)
    parseEscapeCharsInXML(f"{pathToSave}/{newFileName}")



def createXmlFileFromTree(path, xmlFileName, tree):
    """

    :param path: path to save the xml file to
    :param xmlFileName: the file name of the xml file we wnat to create
    :param tree: xml parse tree for the xml file we want to create
    :return: path for the newly created xml file
    """
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
    """
    :param s: string
    :return: s without white space in the start of the string
    """
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



