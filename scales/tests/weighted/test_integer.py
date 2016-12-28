import mock
import unittest

from scales import function
from scales import weighted


class TestInteger(unittest.TestCase):
    @mock.patch('random.uniform')
    def test_weighted_choice_first(self, uniform):
        f = function.Linear()
        uniform.return_value = 1

        result = weighted.integer(f, 1, 3)
        self.assertEqual(1, result)
        uniform.assert_called_once_with(0, 6.0)

    @mock.patch('random.uniform')
    def test_weighted_choice_middle(self, uniform):
        f = function.Linear()
        uniform.return_value = 2

        result = weighted.integer(f, 1, 3)
        self.assertEqual(2, result)
        uniform.assert_called_once_with(0, 6.0)

    @mock.patch('random.uniform')
    def test_weighted_choice_last(self, uniform):
        f = function.Linear()
        uniform.return_value = 5

        result = weighted.integer(f, 1, 3)
        self.assertEqual(3, result)
        uniform.assert_called_once_with(0, 6.0)

    def test_weighted_ceiling_reversed(self):
        f = function.Linear()

        self.assertRaises(ValueError, weighted.integer, f, 3, 2)

    def test_floor_not_int(self):
        f = function.Linear()

        self.assertRaises(AssertionError, weighted.integer, f, 'a', 2)

    def test_ceiling_not_int(self):
        f = function.Linear()

        self.assertRaises(AssertionError, weighted.integer, f, 2, 'a')

    def test_weighted_choice_last(self):
        f = function.Linear()

        result = weighted.integer(f, 1, 1)
        self.assertEqual(1, result)
