  
import xml.etree.ElementTree as ET
import re

def wrapTextWithLocationTag(location):
    pass

def createLocationTag(location):
    pass

def createXmlFileFromTree(tree):
    pass

def extractTextFromXml(path, fileName):
    print("start")
    # amendmentsTree = ET.parse('employmentLaw.xml')
    # amendmentsRoot = amendmentsTree.getroot()
    # print(amendmentsRoot)
    file =  open(path + fileName + ".xml",mode='r',encoding='UTF-8').read()
    text = re.sub('<[^<]+>', "", file)
    # print(text)
    with open("" + fileName + ".txt", "w+", encoding='UTF-8') as f:
       f.write(text)
    


extractTextFromXml("../laws/", "main")

