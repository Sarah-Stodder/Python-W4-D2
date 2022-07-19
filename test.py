from unittest import TestCase, main

from homework import palindrome

class MatchTestCase(TestCase):
    def test_1(self):
        self.assertTrue(palindrome('tacocat'), True)
    def test_nonAlpha(self):
        self.assertTrue(palindrome('Race-car'), True )
    def test_false(self):
        self.assertFalse(palindrome("Race A car"), False )
    def test_empty(self):
        self.assertTrue(palindrome(" "), True)
    def test_more_backspace(self):
        self.assertTrue(palindrome("A man, a plan, a canal: Panama"), True)

if __name__ == '__main__':
    main()