import xml.etree.ElementTree as ET
import re
import stringHelper as stringHelper
# from lawHandler import dataBase
from DateBase import updateWord, isLocationOcc, DataBase


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


def handleXml(filePath):
    ET.register_namespace('', "http://docs.oasis-open.org/legaldocml/ns/akn/3.0")  # ENV VARIABLE
    fileTree = ET.parse(filePath)

    dataBase = DataBase()
    dataBase.put({'היצירה': {'counter': 3, 'instancesToTag': [0, 1, 5]}})
    dataBase.clearAllCounters()

    fileRoot = fileTree.getroot()
    mapKeys = dataBase.getKeys() 
    for key in mapKeys:
        traverseTree(fileRoot, dataBase.getValueByKey(key), key)
    createXmlFileFromTree("../laws/newtemp",fileTree)


def createXmlFileFromTree(filePath, tree):
    openedFile = open(filePath + ".xml", 'w')
    tree.write(filePath + ".xml", encoding='UTF-8')


def traverseTree(node, locationObj, locationToTag):
    if node.text is not None:
        node.text = tagDesignatedLocations(node.text, locationObj, locationToTag)
    for child in node:
        traverseTree(child, locationObj,locationToTag)
    if(node.tail is not None):
        node.tail = tagDesignatedLocations(node.tail, locationObj, locationToTag)


# def traverseTree(node):
#     innerText = node.text 
#     if innerText is not None:
#          print(innerText)
#     for child in node:
#         traverseTree(child)
#     if(node.tail is not None):
#         print(node.tail)



handleXml("../laws/main.xml")



# def extractTextFromXml(path, fileName):
#     file = open(path + fileName + ".xml", mode='r', encoding='UTF-8').read()
#     text = re.sub('<[^<]+>', "", file)
#     with open("" + fileName + ".txt", "w+", encoding='UTF-8') as f:
#         f.write(text)
#
#
# def updateXmlFile(filePath):
#     # file = open(filePath, mode='r', encoding='UTF-8').read()
#     # with open("deletelater.txt", "w+", encoding='UTF-8') as f:
#     #    f.write(file)
#     # print(file)
#     fileTree = ET.parse(filePath)
#     fileRoot = fileTree.getroot()
#     for child in fileRoot:
#         print(child.tail)
#     print("ddda")
#     # for item in fileRoot:
#     #     print(item)
#     # xmlstr = ET.tostring(fileRoot, encoding='utf8', method='xml')
#     # print(xmlstr)
#
#     # fileTree = ET.parse(filePath)
#     # # print(fileTree[2])
#     # # for key, value in fileTree[2]:
#     # #     print(key, value)
#     # # for node in fileTree.iter():
#     # #     print("tag is",node.tag)
#     # #     print("attr" ,node.attrib)
#     # fileRoot = fileTree.getroot()
#     # for item in fileRoot:
#     #     print(item)
#
#
# # extractTextFromXml("../laws/", "main")
# updateXmlFile("../laws/main.xml")
