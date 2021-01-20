import xml.etree.ElementTree as ET
import re
import src.stringHelper as stringHelper
# from lawHandler import dataBase
from src.DataBase import updateWord, isLocationOcc, DataBase
import codecs

def tagDesignatedLocations(string, locationObj, locationToTag):
    index = 0
    instancesToTag = locationObj["instancesToTag"]
    locationToTagLen = len(locationToTag)

    while index < len(string) and len(instancesToTag) > 0:  # keep len calculation inside thw while
        foundIndex = string.find(locationToTag, index)
        if foundIndex == -1:
            break
        else:
            if shouldWrapCurrentInstance(locationObj["counter"], instancesToTag[0]):  # validate that the list locationObj["instancesToTag"] isnt empty
                instancesToTag.pop(0)
                openingTag = createLocationOpenTag(locationToTag)  # add here attribute data
                closingTag = "</location>"
                wrappedTargetWord = stringHelper.wrapString(locationToTag, openingTag, closingTag)
                string = stringHelper.replaceWordAtIndex(string, wrappedTargetWord, foundIndex, locationToTagLen)
                index = foundIndex + len(wrappedTargetWord)
            else:
                index = foundIndex + locationToTagLen
            incrementLocationCounter(locationObj)
    return string

def createLocationTag(location):
    pass

def incrementLocationCounter(locationObj, incrementBy: int = 1):
    locationObj["counter"] += incrementBy

def shouldWrapCurrentInstance(counter: int, currentInstance: int) -> bool:
    return counter == currentInstance

def createLocationOpenTag(location):
    if location != '':
        return f"<location refersTo=\"{location}\" href=\"{location}\">"
    else:
        return "<location>"


def handleXml(path, pathToSave, xmlFileName, db):
    ET.register_namespace('', "http://docs.oasis-open.org/legaldocml/ns/akn/3.0")  # ENV VARIABLE
    fileTree = ET.parse(f"{path}/{xmlFileName}")
    fileRoot = fileTree.getroot()
    mapKeys = db.getKeys()
    for key in mapKeys:
        traverseTree(fileRoot, db.getValueByKey(key), key)
    createXmlFileFromTree(pathToSave, xmlFileName, fileTree)


def createXmlFileFromTree(path, xmlFileName, tree):
    # openedFile = open(f"{path}/{xmlFileName}", 'w')
    tree.write(f"{path}/locationTagged_{xmlFileName}", encoding='UTF-8')


def traverseTree(node, locationObj, locationToTag):
    if node.text is not None:
        node.text = tagDesignatedLocations(node.text, locationObj, locationToTag)
    for child in node:
        traverseTree(child, locationObj,locationToTag)
    if(node.tail is not None):
        node.tail = tagDesignatedLocations(node.tail, locationObj, locationToTag)




# handleXml("../laws/main.xml")

# dataBase = DataBase()
# dataBase.put({'מזל': {'counter': 1, 'instancesToTag': [0]}})
# dataBase.clearAllCounters()
# tagDesignatedLocations(node.text, locationObj, locationToTag)

# createXmlFileFromTree("../laws/newtemp",fileTree)


def extractTextFromXml(path, pathToSave, fileName):
    file = open(f"{path}/{fileName}.xml", mode='r', encoding='UTF-8')
    text = re.sub('<[^<]+>', "", file.read())
    file.close()

    with open(f"{pathToSave}/untagged_{fileName}.txt", "w+", encoding='UTF-8') as f:
        f.write(text)
        f.close()

# extractTextFromXml("../laws/", "main")



# def traverseTree(node):
#     innerText = node.text 
#     if innerText is not None:
#          print(innerText)
#     for child in node:
#         traverseTree(child)
#     if(node.tail is not None):
#         print(node.tail)

