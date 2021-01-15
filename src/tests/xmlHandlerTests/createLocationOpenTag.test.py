import unittest
import src.xmlHandler as XmlHandler


class TesTCreateLocationOpenTag(unittest.TestCase):

    def test_location(self):
        location = 'Yavne'
        self.assertEqual('<location refersTo="Yavne" href="Yavne">', XmlHandler.createLocationOpenTag(location))

    def test_some_empty_location(self):
        location = ''
        self.assertEqual('<location>', XmlHandler.createLocationOpenTag(location))


if __name__ == '__main__':
    unittest.main()