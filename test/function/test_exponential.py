# Copyright 2017 Real Kinetic, LLC. All Rights Reserved.

import unittest

from scales.function import Exponential


class TestExponential(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(403.428793492735123, Exponential(2).evaluate(3))
        self.assertEqual(0.0024787521766663585, Exponential(-2).evaluate(3))
        self.assertEqual(1.822118800390509, Exponential(.2).evaluate(3))
