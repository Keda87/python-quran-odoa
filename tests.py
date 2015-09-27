import unittest
from odoa import get_random_surah


class ODOATest(unittest.TestCase):

    def test_get_surah(self):
        surah = get_random_surah()

        self.assertTrue(surah)
        self.assertEquals(type({}), type(surah))

    def test_not_supported_language(self):
        with self.assertRaises(ValueError):
            get_random_surah('fr')
