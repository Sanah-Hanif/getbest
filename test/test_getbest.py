#!/usr/bin/env python3

import unittest

import getbest


class TestExclude(unittest.TestCase):

    def test_best1(self):
        evecs=[["Student Number","Gender", "Mark"],[483288,F,67],[781294,M,54],[781395,F,80]]
        c1 = getbest.findTop(evecs,1,3)
        self.assertEqual(c1,781395, 80)

    def test_best2(self):
        evecs=[["Student Number", "Mark", "Age"],[712058,42,19],[781208,71,19],[781205,72,27]]
        c1 = getbest.findTop(evecs,1,2)
        self.assertEqual(c1,781205, 72)

if __name__ == '__main__':


    unittest.main()
