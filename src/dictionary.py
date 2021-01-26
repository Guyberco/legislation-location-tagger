import codecs
from env import envPath
FilePath = envPath + "TextFiles/dict.txt"

class Dictionary:
    def __init__(self):
        self.db = {}
        file = codecs.open(FilePath, 'r', 'utf8')  ########### note: ארץ was removed..... maybe remove א"י
        for line in file:
            splitedLine = line.split()
            if len(splitedLine) == 2:
                self.db.update({splitedLine[1] : True})

    def checkValue(self, location):
        """
        :param location:
        :return: true if the locations is in the dictionary
        """
        if location in self.db:
            return True
        return False

loc_dictionray =  Dictionary()
