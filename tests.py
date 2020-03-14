# TODO: update mock testing compatible with python 3
import mock

import unittest
from unittest.mock import MagicMock
from odoa import ODOA, ODOAException


class ODOATest(unittest.TestCase):

    def setUp(self):
        self.odoa = ODOA()

    def test_get_surah(self):
        surah = self.odoa.get_random_surah()
        self.assertIsNotNone(surah)
        surah = self.odoa.get_random_surah(lang='en')
        self.assertIsNotNone(surah)

    def test_not_supported_language(self):
        with self.assertRaises(ODOAException):
            self.odoa.get_random_surah('fr')

    def test_exception_handling_getting_surah(self):
        with mock.patch('odoa.get_random_surah') as execMock:
            execMock.side_effect = IOError(mock.Mock(), 'Error')
            result = odoa.get_random_surah()


if __name__ == '__main__':
    unittest.main()
