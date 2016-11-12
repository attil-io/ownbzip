#!/usr/bin/python

from manber_myers import *
import unittest


class MMTest(unittest.TestCase):
    def testEmpty(self):
        res = manberMyers("")
        self.assertEqual([], res)
    def testOneLetter(self):
        res = manberMyers("a")
        self.assertEqual([0], res)
    def testWord(self):
        res = manberMyers("bobocel")
        self.assertEqual([0, 5, 1, 6, 2, 3, 4], res)

if __name__ == '__main__':
    unittest.main()
