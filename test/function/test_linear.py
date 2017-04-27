# Copyright 2017 Real Kinetic, LLC. All Rights Reserved.

import unittest

from scales.function import Linear


class TestLinear(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(6.02, Linear(slope=.34, y_intercept=5).evaluate(3))
