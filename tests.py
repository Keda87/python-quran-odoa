import unittest
from odoa import ODOA


class ODOATest(unittest.TestCase):

    def setUp(self):
        self.odoa = ODOA()

    def test_get_surah(self):
        surah = self.odoa.get_random_surah()

        if surah:
            self.assertEquals(type({}), type(surah))
            self.assertTrue(surah)

    def test_not_supported_language(self):
        with self.assertRaises(ValueError):
            self.odoa.get_random_surah('fr')
