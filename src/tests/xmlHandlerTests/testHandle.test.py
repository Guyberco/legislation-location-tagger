import unittest
import copy
from src.lawHandler import createDataOfLocs
from src.xmlHandler import handleXml 


class TesTCreateLocationOpenTag(unittest.TestCase):
    srcOutput = "../../../TextFiles/output/untagged2001438.txt"
    db = createDataOfLocs(srcOutput)
    print(db.getDBCopy())
    def test_handleXml(self):
        db = copy.deepcopy(self.db)
        handleXml("../../../laws/2001438.xml", db)

    


if __name__ == '__main__':
    unittest.main()