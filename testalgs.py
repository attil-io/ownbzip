#!/usr/bin/python

from algs import *
import unittest

longText="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

longTransformed = ['.', '.', '.', 'm', 'r', 'a', 't', 't', 't', 's', 'e', 'a', ',', 'o', 'n', 't', 'a', 'd', 'e', 'm', 'm', 't', 'x', 'o', 'g', 't', 't', 'd', 'e', 'e', 'p', 'd', 'u', 'm', 't', 'r', 't', 'r', 'm', 'e', 't', 'o', 't', 'e', 'd', 't', 's', 't', 's', 't', 't', 'i', 'a', 'n', 'a', ',', 'n', ',', 'r', 'r', ',', 'd', 'n', 'i', 't', 'e', 'm', 'n', 't', 'm', 't', 't', 't', 'r', 'a', 'm', ' ', ' ', '.', ' ', 'n', 'e', 'i', 'l', 'p', 'u', 'l', 'l', 'l', ' ', ' ', 'c', 'm', ' ', ' ', 'i', 'l', ' ', ' ', 'p', 'c', 't', 'i', 'u', 'd', 't', 't', 'i', ' ', 'a', 'a', 'a', 'c', 'e', 'o', 'x', 'i', 'n', ' ', 's', 'r', 'm', ' ', ' ', ' ', 'e', ' ', ' ', 'e', 'i', 'u', 'a', 'o', 'i', 'i', 'n', ' ', 'i', 'a', 'o', ' ', ' ', ' ', ' ', ' ', 'i', 's', 'r', 'r', 'r', 't', 'r', 't', ' ', 'a', 's', 's', 'r', ' ', 'v', ' ', 'r', 't', 'h', 'v', ' ', 'd', 'r', 'c', 's', 'x', 'd', 's', 'd', ' ', ' ', ' ', 'm', 't', ' ', 't', ' ', ' ', 'o', 'f', ' ', 'n', 'u', 'a', 'e', 'u', 's', 'c', 'n', 'g', 'r', 'f', ' ', 'p', 'o', 'c', 'd', 'c', 'n', 'n', 'n', ' ', ' ', ' ', ' ', 'c', 'm', 's', 't', 'u', 'd', ' ', 'l', 'l', ' ', 'u', 'r', 'u', 'p', 'n', 's', 'l', 'l', 'r', 'l', 'c', 'e', 'l', ' ', ' ', ' ', 'l', 'a', 'a', 'l', 'e', 'e', 'u', 'u', 'o', 'i', 'o', 'o', 'o', 'o', 'u', 'l', 'o', 'i', 'u', 'u', 'i', 'e', 'i', 'a', 'u', ' ', 'a', 'a', ' ', 'o', 's', 'm', ' ', 'e', 'i', 'o', 'i', 'o', 'i', 'g', 'i', 'e', 'i', 'e', 'e', 'a', 'i', ' ', ' ', ' ', 'o', 'o', 'u', 'u', 'i', 'u', 'e', ' ', 'd', 'd', 'c', ' ', 'm', 'm', ' ', 'r', 'm', 'd', 'd', 'd', 'd', 'v', 'c', 'n', 'i', 'c', 'c', 'l', 'p', 'l', 'b', 'l', 'l', 'L', 'b', 'b', 'n', 'i', 'l', ' ', 'u', 'i', 'm', 'e', ' ', 'i', 'u', 'e', 'i', 'e', ' ', 'i', ' ', 'u', 'o', 'o', 'u', 'o', 'u', 'e', 'u', 'o', 'o', 'o', 'p', 'o', ' ', 'a', 'o', 'e', 'p', 't', 'o', 'e', 'i', 'i', 'i', 'i', 'i', 's', 'n', ' ', 'n', 'e', 'i', ' ', ' ', 'u', 'e', 'e', 'o', 'p', ' ', 'u', 'i', 'i', 'a', 'e', 'U', 'i', 'n', 'i', 'u', 's', 'n', 'a', 'a', 'n', 'n', 'e', 'i', 'n', 'a', 'a', 'p', 'i', 'u', 'a', ' ', 'c', 'p', 'a', 's', 'e', 'a', 'e', 'q', 'q', 'r', 'f', 'q', 'q', 'D', 'q', 'n', ' ', 'c', 's', 'l', 'r', 's', 'r', 'd', 'c', 'l', 't', 'e', 't', 'r', 'i', ' ', ' ', 'a', ' ', ' ', ' ', 'e', 'E', 'e']

class AlgsTest(unittest.TestCase):
    def testCompressEmpty(self):
        L,I = testComp('')
        self.assertEqual(None, I)
        self.assertEqual([], L)

    def testDecompressEmpty(self):
        L=[]
        I=None
        text=''.join(testDecomp(L, I))
        self.assertEqual('', text)

    def testCompressOneChar(self):
        L,I = testComp('a')
        self.assertEqual(0, I)
        self.assertEqual(['a'], L)

    def testDecompressOneChar(self):
        L=['a']
        I=0
        text=''.join(testDecomp(L, I))
        self.assertEqual('a', text)

    def testCompressNormal(self):
        L,I = testComp('abraca')
        self.assertEqual(1, I)
        self.assertEqual(['c', 'a', 'r', 'a', 'a', 'b'], L)

    def testDecompressNormal(self):
        L=['c', 'a', 'r', 'a', 'a', 'b']
        I=1
        text=''.join(testDecomp(L, I))
        self.assertEqual('abraca', text)

    def testDecompressNormal(self):
        L=['c', 'a', 'r', 'a', 'a', 'b']
        I=1
        text=''.join(testDecomp(L, I))
        self.assertEqual('abraca', text)

    def testCompressLong(self):
        L,I = testComp(longText)
        print I
        print L
        self.assertEqual(78, I)
        self.assertEqual(longTransformed, L)

    def testDecompressLong(self):
        I=78
        L=longTransformed
        text=''.join(testDecomp(L, I))
        self.assertEqual(longText, text)




if __name__ == '__main__':
    unittest.main()
