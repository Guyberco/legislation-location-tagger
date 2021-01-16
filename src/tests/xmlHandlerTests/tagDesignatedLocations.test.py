import unittest
import src.xmlHandler as XmlHandler
import copy

from src.DateBase import DataBase


class TestTagDesignatedLocations(unittest.TestCase):

    data_base = DataBase()
    data_base.put({'jerusalem': {'counter': 0, 'instancesToTag': [0, 1, 2]}})
    data_base.put({'תל אביב': {'counter': 0, 'instancesToTag': [0, 2]}})
    data_base.put({'beer sheve': {'counter': 0, 'instancesToTag': [0]}})
    data_base.put({'Yavne': {'counter': 0, 'instancesToTag': [0, 1]}})
    data_base.put({'rehovot': {'counter': 0, 'instancesToTag': [0, 2]}})
    data_base.put({'arad': {'counter': 0, 'instancesToTag': [1]}})
    data_base.put({'Bat yam': {'counter': 0, 'instancesToTag': [2, 4]}})
    data_base.put({'tel aviv': {'counter': 0, 'instancesToTag': []}})
    data_base.put({'Ramat gan': {'counter': 2, 'instancesToTag': [2, 4, 5]}})


    # # One word location
    def test_oneWordLocation_not_exist(self):
        string = 'אם זו יצירה דרמטית, להפוך אותה לרומן או לכל יצירה אחרת שאינה דרמטית'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual(string, stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_start(self):
        string = 'beer sheve I think is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'beer sheve'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('<location refersTo="beer sheve" href="beer sheve">beer sheve</location> I think is the best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_start_with_dummy(self):
        string = 'beer sheve I think beer sheve is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'beer sheve'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('<location refersTo="beer sheve" href="beer sheve">beer sheve</location> I think beer sheve is the best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_middle(self):
        string = 'I think Yavne is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('I think <location refersTo="Yavne" href="Yavne">Yavne</location> is the best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_middle_with_dummy(self):
        string = 'arad I think arad is the yavne best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'arad'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('arad I think <location refersTo="arad" href="arad">arad</location> is the yavne best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_end(self):
        string = 'I think is the best jerusalem city Yavne'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('I think is the best jerusalem city <location refersTo="Yavne" href="Yavne">Yavne</location>', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_end_with_dummy(self):
        string = 'I Bat yam Bat yam think is the jerusalem best city Bat yam'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Bat yam'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('I Bat yam Bat yam think is the jerusalem best city <location refersTo="Bat yam" href="Bat yam">Bat yam</location>', stringWithWrappedLocation)


    def test_oneWordLocation_2_instance(self):
        string = 'I think Yavne is Yavne the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('I think <location refersTo="Yavne" href="Yavne">Yavne</location> is <location refersTo="Yavne" href="Yavne">Yavne</location> the best city', stringWithWrappedLocation)

    def test_oneWordLocation_2_instance_begin_end(self):
        string = 'rehovot think rehovot is the best city rehovot'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'rehovot'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('<location refersTo="rehovot" href="rehovot">rehovot</location> think rehovot is the best city <location refersTo="rehovot" href="rehovot">rehovot</location>', stringWithWrappedLocation)

    def test_oneWordLocation_3_instance_(self):
        string = 'jerusalem jerusalem jerusalem something something'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'jerusalem'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('<location refersTo="jerusalem" href="jerusalem">jerusalem</location> <location refersTo="jerusalem" href="jerusalem">jerusalem</location> <location refersTo="jerusalem" href="jerusalem">jerusalem</location> something something', stringWithWrappedLocation)

    def test_in_two_separatedTexts(self):
        string1 = 'I Bat yam Bat yam think is the jerusalem best city Bat yam'
        string2 = 'I Bat yam Bat yam think is the jerusalem best city Bat yam'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Bat yam'
        locationObj = db.getValueByKey(locationToTag)
        XmlHandler.tagDesignatedLocations(string1, locationObj, locationToTag)
        stringWithWrappedLocation2 = XmlHandler.tagDesignatedLocations(string2, locationObj, locationToTag)
        self.assertEqual('I Bat yam <location refersTo="Bat yam" href="Bat yam">Bat yam</location> think is the jerusalem best city Bat yam', stringWithWrappedLocation2)

    def test_in_three_separatedTexts(self):
        string1 = 'I Bat yam Bat yam think is the jerusalem best city Bat yam'
        string2 = 'I Bat yam Bat yam think is the jerusalem best city Bat yam'
        string3 = 'I Bat yam Bat yam think is the jerusalem best city Bat yam'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Bat yam'
        locationObj = db.getValueByKey(locationToTag)
        XmlHandler.tagDesignatedLocations(string1, locationObj, locationToTag)
        XmlHandler.tagDesignatedLocations(string2, locationObj, locationToTag)
        stringWithWrappedLocation3 = XmlHandler.tagDesignatedLocations(string3, locationObj, locationToTag)
        self.assertEqual('I Bat yam Bat yam think is the jerusalem best city Bat yam', stringWithWrappedLocation3)

    def test_empty_instancesList(self):
        string = 'I think tel aviv is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'tel aviv'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('I think tel aviv is the best city', stringWithWrappedLocation)

    def test_incremented_counter_1_instance(self):
        string = 'I think Ramat gan is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Ramat gan'
        locationObj = db.getValueByKey(locationToTag)
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, locationObj, locationToTag)
        self.assertEqual('I think <location refersTo="Ramat gan" href="Ramat gan">Ramat gan</location> is the best city', stringWithWrappedLocation)

if __name__ == '__main__':
    unittest.main()

