  
import xml.etree.ElementTree as ET
import re



def findLocationInStringAndWrapAllOcc(string, db, location):
    index = 0
    locationObj = db[location]
    indexOfOoccurrence = locationObj["indexOfOoccurrence"]
    
    while(index < len(string) and len(indexOfOoccurrence) > 0): # keep lne calculation inside thw while
        foundIndex = string.find(location, index)
        if foundIndex == -1:
            break

        if(locationObj["counter"] == indexOfOoccurrence.get(0)):  #validate that the list locationObj["indexOfOoccurrence"] isnt empty
            indexOfOoccurrence.pop(0)
            tagPrefix = "<location>"  # add here attribute data 
            tagSuffix = "</location>"
            string = wrapTextWithLocationTag(string, location, locationObj, tagPrefix, tagSuffix)
            index = foundIndex + len(tagPrefix) + len(location) + len(tagSuffix)
        locationObj["counter"] += 1
    return string

 # Add tag to the Locatio
def wrapTextWithLocationTag(string, location, locationVal, tagPrefix , tagSuffix): 
    string = addToString(string, tagPrefix, locationVal)      
    string = addToString(string, tagSuffix, locationVal + len(tagPrefix) + len(location))
    return string

def addToString(str, addstr, index):
    return str[ : index] + addstr + str[index : ]

def createLocationTag(location):
    pass

def createXmlFileFromTree(filePath,tree):
    openedFile = open(filePath + ".xml", 'w')
    tree.write(filePath + ".xml", encoding='UTF-8')

def extractTextFromXml(path, fileName):
    file =  open(path + fileName + ".xml",mode='r',encoding='UTF-8').read()
    text = re.sub('<[^<]+>', "", file)
    with open("" + fileName + ".txt", "w+", encoding='UTF-8') as f:
       f.write(text)



def updateXmlFile(filePath):
    # file = open(filePath, mode='r', encoding='UTF-8').read()
    # with open("deletelater.txt", "w+", encoding='UTF-8') as f:
    #    f.write(file)
    # print(file)
    fileTree = ET.parse(filePath)
    fileRoot = fileTree.getroot()
    for child in fileRoot:
        print(child.tail = <loc>bisli</loc> is not a bamba)
    print("ddda")
    # for item in fileRoot: 
    #     print(item)
    # xmlstr = ET.tostring(fileRoot, encoding='utf8', method='xml')
    # print(xmlstr)
     
    # fileTree = ET.parse(filePath)
    # # print(fileTree[2])
    # # for key, value in fileTree[2]:
    # #     print(key, value)
    # # for node in fileTree.iter():
    # #     print("tag is",node.tag)
    # #     print("attr" ,node.attrib)
    # fileRoot = fileTree.getroot()
    # for item in fileRoot: 
    #     print(item)


# extractTextFromXml("../laws/", "main")
updateXmlFile("../laws/main.xml")



