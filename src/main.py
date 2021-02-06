import codecs
import glob
import os
import shutil

from env import envPath
from src.lawHandler import createDataOfLocs
from src.taggerRunner import runTagger
from src.xmlHandler import extractTextFromXml, handleXml, parseEscapeCharsInXML


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


def moveLawsToOneFolder():
    dst = "C:/Users/zemse/Downloads/LawRepoWiki/putlaws"
    listOfAllFiles = getListOfFiles("C:/Users/zemse/Downloads/LawRepoWiki/akn/il/act")
    # listOfFiles = glob.glob("C:/Users/zemse/Downloads/LawRepoWiki/akn/il/act" + '/**/*/.xml', recursive=True)
    # print(listOfFiles)
    for nameFile in listOfAllFiles:
        if nameFile[-3:] == "xml":
            shutil.copy(nameFile, dst)
            Prefixname = nameFile.split("\\")[3]
            os.rename('C:/Users/zemse/Downloads/LawRepoWiki/putlaws/main.xml', f"C:/Users/zemse/Downloads/LawRepoWiki/putlaws/{Prefixname}Law.xml")



def main():
    originalXmlPath = "../originalLaws"
    # for filename in os.listdir("../originalLaws"):
    #     filename = filename[:-4]    # remove .xml ending
    #     extractTextFromXml(originalXmlPath, "../TextFiles/tagger_input", filename)
    runTagger()
    # for filename in os.listdir("../TextFiles/tagger_output"):
    #     filename = filename[14:-4]    # remove .txt ending and untagged_ prefix
    #     db = createDataOfLocs(f"../TextFiles/tagger_output/afteruntagged_{filename}.txt")
    #     handleXml(originalXmlPath, "../final_outputs", f"{filename}.xml", db)


main()

# file = codecs.open("C:/Users/zemse/Desktop/school/digital sc/final project/legislation-location-tagger/TextFiles/tagger_input/afteruntagged_94272Law.txt", 'r', 'utf8')
