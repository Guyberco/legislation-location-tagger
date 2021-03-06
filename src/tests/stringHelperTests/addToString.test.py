import unittest
import src.stringHelper as stringHelper


class TestAddToString(unittest.TestCase):

    def test_empty_string_addition(self):
        str = 'Hi'
        self.assertEqual(str, stringHelper.addToString(str, '', 0))

    def test_add_to_empty_string_1(self):
        str = ''
        self.assertEqual(str + 'mama', stringHelper.addToString(str, 'mama', 0))

    def test_add_to_empty_string_2(self):
        str = ''
        self.assertEqual(str + 'mama', stringHelper.addToString(str, 'mama', -1))

    def test_add_at_beginning(self):
        str = 'world'
        self.assertEqual('Hello' + str, stringHelper.addToString(str, 'Hello', 0))

    def test_add_at_end(self):
        str = 'Hello'
        self.assertEqual(str + ' world', stringHelper.addToString(str, ' world', 5))

    def test_add_at_middle(self):
        str = 'Oh god'
        self.assertEqual('Oh my god', stringHelper.addToString(str, 'my ', 3))

    def test_false_1(self):
        str = 'world'
        self.assertNotEqual('Hello' + str, stringHelper.addToString(str, 'Hello', 1))

    def test_false_2(self):
        str = 'world'
        self.assertNotEqual('Hello' + str, stringHelper.addToString(str, 'Hello', 10))

    def test_false_3(self):
        str = 'Oh god'
        self.assertNotEqual('Oh my god', stringHelper.addToString(str, 'my', 3))

    def test_isAcronym(self):
        str = 'sd"sd'
        self.assertTrue(stringHelper.isAcronym(str))

    def test_isAcronym2(self):
        str = 'sd.sd'
        self.assertTrue(stringHelper.isAcronym(str))

    def test_isAcronym3(self):
        str = 'sdsd'
        self.assertFalse(stringHelper.isAcronym(str))

    def test_isMoreThanOneWord(self):
        str = 'sd sd'
        self.assertTrue(stringHelper.isMoreThanOneWord(str))

    def test_isMoreThanOneWord2(self):
        str = 'sds-d'
        self.assertTrue(stringHelper.isMoreThanOneWord(str))

    def test_isMoreThanOneWord3(self):
        str = 's_dsd'
        self.assertTrue(stringHelper.isMoreThanOneWord(str))

    def test_isMoreThanOneWord4(self):
        str = 'sdsd'
        self.assertFalse(stringHelper.isMoreThanOneWord(str))

# def isMoreThanOneWord(word):
#     return ' ' in word or '-' in word or '_' in word

if __name__ == '__main__':
    unittest.main()