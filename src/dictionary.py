import codecs
from env import envPath
FilePath = envPath + "/TextFiles/dict.txt"

class Dictionary:
    def __init__(self):
        self.db = {}
        file = codecs.open(FilePath, 'r', 'utf8')
        for line in file:
            splitedLine = " ".join(line[4:].split())
            self.db.update({splitedLine : True})
    def checkValue(self, location):
        """
        :param location:
        :return: true if the locations is in the dictionary
        """
        if location in self.db:
            return True
        return False




acronymToLocationTag = {
    "א\"י": "Israel",
    "ארה\"ב": "USA",
    "דרא\"פ": "South_Africa",
    "ב\"ש": "Beer_Sheba",
    "בני עי\"ש": "Bnei_Ayish",
    "בסמ\"ה": "Basma",
    "כפ\"ס": "Kfar_Saba",
    "פ\"ת": "Petah_Tikva",
    "רשל\"צ": "Rishon_Lezion",
    "ר\"ג": "Ramat_Gan",
    "רמה\"ש": "Ramat_Hasharon",
    "ת\"א": "Tel_Aviv"
}

def getLocationToTagByAcronym(acronym):
    return acronymToLocationTag.get(acronym)

loc_dictionray =  Dictionary()
