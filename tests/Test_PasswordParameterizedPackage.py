import unittest
from src.Zad1.Password import *
from parameterized import parameterized, parameterized_class

class PasswordParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Password()

    @parameterized.expand([
        ("Has1*", False),
        ("withoutCapital", False),
        ("withoutNumber", False),
        ("withoutSymbol", False),
    ])
    def test_one_parameterized(self, password, expected):
        self.assertEqual(self.tmp.ValidPassword(password), expected)


@parameterized_class(('password', 'expected'), [
    ("onlyNumber", False),
    ("onlyCapital", False),
    ("onlySymbol", False),
    ("correctPassword", True),
])
class PasswordParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Password()

    def test_two_parameterized(self):
        self.assertEqual(self.tmp.ValidPassword(self.password), self.expected)



        
withoutLetter False
withoutSymbol False
 False
