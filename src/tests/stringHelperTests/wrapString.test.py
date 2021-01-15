import unittest
import src.stringHelper as stringHelper


class TestWrapString(unittest.TestCase):

    def test_full_wrap_1(self):
        str = 'Hi'
        prefix = '<location>'
        suffix = '</location>'
        self.assertEqual('<location>Hi</location>', stringHelper.wrapString(str, prefix, suffix))

    def test_full_wrap_2(self):
        str = 'love'
        prefix = 'I '
        suffix = ' science'
        self.assertEqual('I love science', stringHelper.wrapString(str, prefix, suffix))

    def test_wrap_at_beginning(self):
        str = 'dog'
        prefix = 'Whats up '
        suffix = ''
        self.assertEqual('Whats up dog', stringHelper.wrapString(str, prefix, suffix))

    def test_wrap_at_end(self):
        str = 'Hi'
        prefix = ''
        suffix = ' you'
        self.assertEqual('Hi you', stringHelper.wrapString(str, prefix, suffix))

    def test_wrap_with_noting(self):
        str = 'love'
        prefix = 'I'
        suffix = 'science'
        self.assertNotEqual('I love science', stringHelper.wrapString(str, prefix, suffix))


if __name__ == '__main__':
    unittest.main()