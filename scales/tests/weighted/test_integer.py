import mock
import unittest


from scales import function
from scales import weighted


class TestInteger(unittest.TestCase):

    @mock.patch('random')
    def test_weighted_choice(self, random):
        pass