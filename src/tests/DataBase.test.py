import unittest
import src.stringHelper as stringHelper
from src.DataBase import DataBase
import copy

class TestDataBase(unittest.TestCase):

    data_base = DataBase()
    data_base.put({'jerusalem': {'counter': 3, 'instancesToTag': [0, 1, 2]}})
    data_base.put({'תל אביב': {'counter': 0, 'instancesToTag': [0, 2]}})
    data_base.put({'beer sheve': {'counter': 5, 'instancesToTag': [0]}})
    data_base.put({'Yavne': {'counter': 2, 'instancesToTag': [0, 1]}})
    data_base.put({'rehovot': {'counter': 0, 'instancesToTag': [0, 2]}})
    data_base.put({'arad': {'counter': 0, 'instancesToTag': [1]}})
    data_base.put({'Bat yam': {'counter': 1, 'instancesToTag': [2, 4]}})
    data_base.put({'tel aviv': {'counter': 0, 'instancesToTag': []}})
    data_base.put({'Ramat gan': {'counter': 2, 'instancesToTag': [2, 4, 5]}})

    def test_clearCounter(self):
        key = 'jerusalem'
        db = copy.deepcopy(self.data_base)
        db.clearCounter(key)
        newCounter = db.getValueByKey(key)
        self.assertEqual(0, newCounter['counter'])

    def test_clearAllCounter(self):
        db = copy.deepcopy(self.data_base)
        db.clearAllCounters()


    def test_getValueByKey(self):
        key = 'jerusalem'
        db = copy.deepcopy(self.data_base)
        self.assertEqual({'counter': 3, 'instancesToTag': [0, 1, 2]}, db.getValueByKey(key))

    def test_createNewDataBase(self):
        db = DataBase()
        self.assertEqual({}, db.getDictionaryDeepCopy())

    def test_createNewLocationEntry(self):
        db = DataBase()
        db.createNewLocationEntry('tel aviv')
        self.assertIsNotNone(db.getValueByKey('tel aviv'))

    def test_put(self):
        db = DataBase()
        db.put({'tel aviv': {'counter': 0, 'instancesToTag': []}})
        self.assertNotEqual({}, db.getDictionaryDeepCopy())
        self.assertIsNotNone(db.getValueByKey('tel aviv'))



if __name__ == '__main__':
    unittest.main()