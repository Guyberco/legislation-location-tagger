import xml.etree.ElementTree as ET
import os

from env import envPath

locationsMap = {}

def extractDataFromAllLaws():
    dir = f"{envPath}/final_outputs"
    print(dir)
    for filename in os.listdir(dir):
        extractDataFromLaw(f"{dir}/{filename}")

def extractDataFromLaw(xmlFilePath):
    ET.register_namespace('', "http://docs.oasis-open.org/legaldocml/ns/akn/3.0")  # ENV VARIABLE
    fileTree = ET.parse(xmlFilePath)
    fileRoot = fileTree.getroot()
    locations = getLocations(fileRoot)
    date = getLawDate(fileRoot)
    lawName = getLawName(fileRoot)
    law = {"name": lawName, "date": date}
    addLawToLoactionMap(law, locations)


def getLocations(root):
    locationsTag = list(root.iter("{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}location"))
    return set(map(lambda location: location.attrib["refersTo"], locationsTag))

def getLawDate(root):
    FRBRdateList = list(root.iter("{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}FRBRdate"))
    date = None
    if len(FRBRdateList) > 0:
        date = FRBRdateList[0].attrib["date"]
    return date

def getLawName(root):
    p = getLawFirstP(root)
    if not p == None:
        pContext = traverseParagraph(p)
        return " ".join(pContext.split())



def addLawToLoactionMap(law, locations):
    for location in locations:
        locationInMap = locationsMap.get(location)
        if not locationInMap ==  None:
            locationInMap.append(law)
        else:
            locationsMap.update({location: [law]})

def getLawFirstP(root):
    body = list(root.iter("{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}body"))
    if len(body) > 0:
        pList = list(body[0].iter("{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}p"))
        if len(pList) > 0:
            return pList[0]
    return None

def traverseParagraph(node):
    text = ''
    if node.text is not None:
        text += node.text
    for child in node:
        text += traverseParagraph(child)
    if(node.tail is not None):
        text += node.tail
    return text
