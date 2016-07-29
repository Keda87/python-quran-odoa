import unittest
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

if __name__ == '__main__':
    unittest.main()
