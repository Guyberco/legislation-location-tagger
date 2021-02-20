import os
import xml.etree.ElementTree as ET
from src.lawHandler import createDataOfLocs
from src.taggerRunner import runTagger
from src.xmlHandler import extractTextFromXml, handleXml, parseEscapeCharsInXML

def write_list_to_file(lst):
    list_to_print = '\n'.join(map(str, lst))
    error_file = open("error_files.txt", "w")
    error_file.write(list_to_print)
    error_file.close()

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def verifyXML(filePath):
    fileTree = ET.parse(filePath)

def check_files():
    list_of_erros = []
    for filename in os.listdir("../final_outputs"):
        try:
            verifyXML(f"../final_outputs/{filename}")
        except ET.ParseError:
            list_of_erros.append(f"{filename}.xml")
            print(f"Not valid output {filename}.xml")
    print(list_of_erros)



def main():
    originalXmlPath = "../originalLaws"
    list_of_erros = []
    for filename in os.listdir("../originalLaws"):
        filename = filename[:-4]    # remove .xml ending
        extractTextFromXml(originalXmlPath, "../TextFiles/tagger_input", filename)
    runTagger()
    for filename in os.listdir("../TextFiles/tagger_output"):
        filename = filename[14:-4]    # remove .txt ending and untagged_ prefix
        print(f"****Starting: {filename}.xml")
        db = createDataOfLocs(f"../TextFiles/tagger_output/afteruntagged_{filename}.txt")
        handleXml(originalXmlPath, "../final_outputs", f"{filename}.xml", db)
        print(f"Finished working on file: {filename}.xml")
        try:
            verifyXML(f"../final_outputs/locationTagged_{filename}.xml")
        except ET.ParseError:
            list_of_erros.append(f"{filename}.xml")
            print(f"Not valid output {filename}.xml")
    write_list_to_file(list_of_erros)






main()
