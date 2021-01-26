from env import envPath
from src.lawHandler import createDataOfLocs
from src.taggerRunner import runTagger
from src.xmlHandler import extractTextFromXml, handleXml, parseEscapeCharsInXML


def main():
    fileName = "main"
    originalXmlPath = "../originalLaws"
    # generateTaggerOutput(originalXmlPath, fileName)
    db = createDataOfLocs(f"../TextFiles/tagger_output/untagged_{fileName}.txt")
    handleXml(originalXmlPath, "../final_outputs", f"{fileName}.xml", db)

def generateTaggerOutput(originalXmlPath, fileName):
    extractTextFromXml(originalXmlPath, "../TextFiles/input", fileName)
    runTagger()
main()