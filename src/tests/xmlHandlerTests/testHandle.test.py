import sys
#  sys.path.append("C:/Users/zemse/Desktop/school/digital sc/final project/legislation-location-tagger/src")
# sys.path.append("../../")
# import parent.xmlHandler
import unittest
# from ...src import xmlHandler
from src.xmlHandler import handleXml 
from lawHandler import createDataOfLocs

class TesTCreateLocationOpenTag(unittest.TestCase):
    srcOutput = "../../TextFiles/output"
    db = createDataOfLocs(srcOutput+"/untaggedmain.txt")
    
    def handleXml(self):
        handleXml("../../laws/main.xml", self.db.getDBCopy())
    


if __name__ == '__main__':
    unittest.main()