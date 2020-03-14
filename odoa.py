"""
The MIT License (MIT)

Copyright (c) 2015 Adiyat Mubarak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random

import httpx
from httpx import Response


class ODOAException(Exception):
    pass


class Quran(object):
    __slots__ = ['ayah', 'desc', 'translate', 'sound']

    def __init__(self, ayah: str, desc: str, translate: str, sound: str):
        self.ayah = ayah
        self.desc = desc
        self.translate = translate
        self.sound = sound

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.desc}>'


class ODOA(object):
    __slots__ = ['__TOTAL_SURAH', '__BASE_API', '__SUPPORTED_LANGUAGES']

    def __init__(self) -> None:
        self.__TOTAL_SURAH = 114  # https://en.wikipedia.org/wiki/List_of_surahs_in_the_Quran
        self.__BASE_API = 'https://raw.githubusercontent.com/Keda87/quranjson/master/source'
        self.__SUPPORTED_LANGUAGES = ['id', 'en']

    async def get_random_surah(self, lang: str = 'id') -> Quran:
        if lang not in self.__SUPPORTED_LANGUAGES:
            message = 'Currently your selected language not supported yet.'
            raise ODOAException(message)

        rand_surah = random.randint(1, self.__TOTAL_SURAH)
        surah_url = f'{self.__BASE_API}/surah/surah_{rand_surah}.json'
        try:
            response = await self.__fetch(surah_url)
            data = response.json()
        except IOError:
            raise ODOAException
        else:
            random_ayah = random.randint(1, int(data.get('count')))
            ayah_key = f'verse_{random_ayah}'
            ayah = data['verse'][ayah_key]
            surah_index = data.get('index')
            surah_name = data.get('name')

            translation = await self.__get_translation(surah_index, ayah_key, lang)
            sound = self.__get_sound(surah_index, random_ayah)
            desc = f'{surah_name}:{random_ayah}'
            return Quran(ayah, desc, translation, sound)

    async def __get_translation(self, surah: int, ayah, lang: str) -> str:
        url = f'{self.__BASE_API}/translations/{lang}/{lang}_translation_{int(surah)}.json'
        try:
            response = await self.__fetch(url)
            data = response.json()
            return data['verse'][ayah]
        except ODOAException as e:
            raise e

    def __get_sound(self, surah: int, ayah: int) -> str:
        format_ayah = str(ayah).zfill(3)
        return f'{self.__BASE_API}/sounds/{surah}/{format_ayah}.mp3'

    @staticmethod
    async def __fetch(url: str) -> Response:
        async with httpx.AsyncClient() as client:
            return await client.get(url)

    def __repr__(self):
        return f'<{self.__class__.__name__}>'
