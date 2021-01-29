import os

from env import envPath
from src.lawHandler import createDataOfLocs
from src.taggerRunner import runTagger
from src.xmlHandler import extractTextFromXml, handleXml, parseEscapeCharsInXML


def main():
    originalXmlPath = "../originalLaws"
    # for filename in os.listdir("../originalLaws"):
    #     filename = filename[:-4]    # remove .xml ending
    #     extractTextFromXml(originalXmlPath, "../TextFiles/tagger_input", filename)
    # runTagger()
    for filename in os.listdir("../TextFiles/tagger_output"):
        filename = filename[9:-4]    # remove .txt ending and untagged_ prefix
        db = createDataOfLocs(f"../TextFiles/tagger_output/untagged_{filename}.txt")
        handleXml(originalXmlPath, "../final_outputs", f"{filename}.xml", db)

    # db = createDataOfLocs(f"../TextFiles/tagger_output/untagged_madeup.txt")

main()