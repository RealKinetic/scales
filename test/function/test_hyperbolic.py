# Copyright 2017 Real Kinetic, LLC. All Rights Reserved.

import unittest

from scales.function import Hyperbolic


class TestHyperbolic(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(0.14285714285714285, Hyperbolic(2).evaluate(3))
        self.assertEqual(-0.2, Hyperbolic(-2).evaluate(3))
