import unittest
import src.XmlHandler as XmlHandler
import copy


class TestTagDesignatedLocations(unittest.TestCase):

    data_base = {
        'jerusalem': {'counter': 0, 'instancesToTag': [0, 1, 2]},
        'תל אביב': {'counter': 0, 'instancesToTag': [0, 2]},
        'beer sheve': {'counter': 0, 'instancesToTag': [0]},
        'Yavne': {'counter': 0, 'instancesToTag': [0, 1]},
        'rehovot': {'counter': 0, 'instancesToTag': [0, 2]},
        'arad': {'counter': 0, 'instancesToTag': [1]},
        'Bat yam': {'counter': 0, 'instancesToTag': [2, 5]},
    }

    # One word location
    def test_oneWordLocation_not_exist(self):
        string = 'אם זו יצירה דרמטית, להפוך אותה לרומן או לכל יצירה אחרת שאינה דרמטית'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual(string, stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_start(self):
        string = 'beer sheve I think is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'beer sheve'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('<location refersTo="beer sheve" href="beer sheve">beer sheve</location> I think is the best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_start_with_dummy(self):
        string = 'beer sheve I think beer sheve is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'beer sheve'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('<location refersTo="beer sheve" href="beer sheve">beer sheve</location> I think beer sheve is the best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_middle(self):
        string = 'I think Yavne is the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('I think <location refersTo="Yavne" href="Yavne">Yavne</location> is the best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_middle_with_dummy(self):
        string = 'arad I think arad is the yavne best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'arad'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('arad I think <location refersTo="arad" href="arad">arad</location> is the yavne best city', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_end(self):
        string = 'I think is the best jerusalem city Yavne'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('I think is the best jerusalem city <location refersTo="Yavne" href="Yavne">Yavne</location>', stringWithWrappedLocation)

    def test_oneWordLocation_1_instance_in_end_with_dummy(self):
        string = 'I Bat yam Bat yam think is the jerusalem best city Bat yam'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Bat yam'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('I Bat yam Bat yam think is the jerusalem best city <location refersTo="Bat yam" href="Bat yam">Bat yam</location>', stringWithWrappedLocation)


    def test_oneWordLocation_2_instance(self):
        string = 'I think Yavne is Yavne the best city'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'Yavne'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('I think <location refersTo="Yavne" href="Yavne">Yavne</location> is <location refersTo="Yavne" href="Yavne">Yavne</location> the best city', stringWithWrappedLocation)

    def test_oneWordLocation_2_instance_begin_end(self):
        string = 'rehovot think rehovot is the best city rehovot'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'rehovot'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('<location refersTo="rehovot" href="rehovot">rehovot</location> think rehovot is the best city <location refersTo="rehovot" href="rehovot">rehovot</location>', stringWithWrappedLocation)

    def test_oneWordLocation_3_instance_(self):
        string = 'jerusalem jerusalem jerusalem something something'
        db = copy.deepcopy(self.data_base)
        locationToTag = 'jerusalem'
        stringWithWrappedLocation = XmlHandler.tagDesignatedLocations(string, db, locationToTag)
        self.assertEqual('<location refersTo="jerusalem" href="jerusalem">jerusalem</location> <location refersTo="jerusalem" href="jerusalem">jerusalem</location> <location refersTo="jerusalem" href="jerusalem">jerusalem</location> something something', stringWithWrappedLocation)

if __name__ == '__main__':
    unittest.main()