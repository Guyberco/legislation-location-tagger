from src.lawHandler import createDataOfLocs
from src.taggerRunner import runTagger
from src.xmlHandler import extractTextFromXml, handleXml


def main():
    fileName = "main"
    originalXmlPath = "../originalLaws"
    extractTextFromXml(originalXmlPath, "../TextFiles/input", fileName)
    runTagger()
    db = createDataOfLocs(f"../TextFiles/tagger_output/untagged_{fileName}.txt")
    print(db.getDictionaryDeepCopy())
    handleXml(originalXmlPath, "../final_outputs", f"{fileName}.xml", db)
    print(db)

main()