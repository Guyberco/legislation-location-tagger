import unittest
import copy
from src.lawHandler import createDataOfLocs
from src.xmlHandler import handleXml 


class TesTCreateLocationOpenTag(unittest.TestCase):
    srcOutput = "../TextFiles/tagger_output/untagged_main.txt"
    db = createDataOfLocs(srcOutput)


    def test_handleXml(self):
        db = copy.deepcopy(self.db)
        handleXml("../../../originalLaws/main.xml", db)

    


if __name__ == '__main__':
    unittest.main()