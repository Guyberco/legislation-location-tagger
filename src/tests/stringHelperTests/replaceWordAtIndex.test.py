import unittest
import src.stringHelper as stringHelper


class TestReplaceWordAtIndex(unittest.TestCase):

    def test_replace_at_end(self):
        str = 'I want to be in Jerusalem'
        word = 'Jerusalem'
        strToReplaceWith = '<location>Jerusalem</location>'
        wordIndex = str.find(word)
        wordLen = len(word)
        self.assertEqual('I want to be in <location>Jerusalem</location>', stringHelper.replaceWordAtIndex(str, strToReplaceWith, wordIndex, wordLen))

    def test_replace_at_beginning(self):
        str = 'Tel Aviv is the best!'
        word = 'Tel Aviv'
        strToReplaceWith = '<location>Tel Aviv</location>'
        wordIndex = str.find(word)
        wordLen = len(word)
        self.assertEqual('<location>Tel Aviv</location> is the best!', stringHelper.replaceWordAtIndex(str, strToReplaceWith, wordIndex, wordLen))

    def test_replace_at_middle(self):
        str = 'I think Beer sheva is in the south'
        word = 'Beer sheva'
        strToReplaceWith = '<location> Beer sheva</location>'
        wordIndex = str.find(word)
        wordLen = len(word)
        self.assertEqual('I think <location> Beer sheva</location> is in the south', stringHelper.replaceWordAtIndex(str, strToReplaceWith, wordIndex, wordLen))

    def test_replace_nothing(self):
        str = 'I think Beer not sheva is in the south'
        word = 'Beer sheva'
        strToReplaceWith = '<location> Beer sheva</location>'
        wordIndex = str.find(word)
        wordLen = len(word)
        self.assertEqual('I think Beer not sheva is in the south', stringHelper.replaceWordAtIndex(str, strToReplaceWith, wordIndex, wordLen))



if __name__ == '__main__':
    unittest.main()