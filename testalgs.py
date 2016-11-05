#!/usr/bin/python

from algs import *
import unittest

class AlgsTest(unittest.TestCase):
    def testCompress(self):
        L,I = testComp('abraca')
        self.assertEqual(1, I)
        self.assertEqual(['c', 'a', 'r', 'a', 'a', 'b'], L)

    def testDecompress(self):
        L=['c', 'a', 'r', 'a', 'a', 'b']
        I=1
        text=''.join(testDecomp(L, I))
        self.assertEqual('abraca', text)


if __name__ == '__main__':
    unittest.main()
