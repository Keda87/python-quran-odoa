import asyncio
import unittest
from unittest import mock

from odoa import ODOA, ODOAException

LOOP = asyncio.get_event_loop()


class ODOATest(unittest.TestCase):

    def setUp(self) -> None:
        self.odoa = ODOA()

    def test_get_surah(self):
        coro = self.odoa.get_random_surah()
        surah = LOOP.run_until_complete(coro)
        self.assertIsNotNone(surah)

    def test_get_surah_english(self):
        coro = self.odoa.get_random_surah(lang='en')
        surah = LOOP.run_until_complete(coro)
        self.assertIsNotNone(surah)

    def test_not_supported_language(self):
        with self.assertRaises(ODOAException):
            coro = self.odoa.get_random_surah('fr')
            LOOP.run_until_complete(coro)

    # TODO: fix this test.
    # def test_exception_handling_getting_surah(self):
    #     with mock.patch('odoa.get_random_surah') as execMock:
    #         execMock.side_effect = IOError(mock.Mock(), 'Error')
    #         with self.assertRaises(ODOAException):
    #             coro = self.odoa.get_random_surah()
    #             LOOP.run_until_complete(coro)


if __name__ == '__main__':
    unittest.main()
