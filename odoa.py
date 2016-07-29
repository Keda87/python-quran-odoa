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
import sys
import json
import random
import traceback
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


class ODOAException(Exception):
    pass


class Metadata(object):

    def __init__(self, ayah, desc, translate, sound):
        self.ayah = ayah
        self.desc = desc
        self.translate = translate
        self.sound = sound


class ODOA(object):
    TOTAL_SURAH = 114  # Total surah within quran : https://en.wikipedia.org/wiki/List_of_surahs_in_the_Quran
    BASE_API = 'https://raw.githubusercontent.com/Keda87/quranjson/master/source'
    SUPPORTED_LANGUAGES = ['id', 'en']

    def get_random_surah(self, lang='id'):
        """
        Perform http request to get random surah.

        Parameter:
            :lang       --  String contains language code.

        Return:
            :dict       --  Paired ayat, sound, description and the translation.
        """
        # Ensure the language supported.
        if lang not in self.SUPPORTED_LANGUAGES:
            message = 'Currently your selected language not yet supported.'
            raise ODOAException(message)
        # Get random surah and construct the url.
        rand_surah = random.randint(1, self.TOTAL_SURAH)
        surah_url = '{base}/surah/surah_{pages}.json'.format(base=self.BASE_API,
                                                             pages=rand_surah)
        try:
            response = urlopen(surah_url)                        # Fetch data from given url.
            data = json.loads(response.read().decode('utf-8'))   # Get response and convert to dict.
        except IOError:
            traceback.print_exc(file=sys.stdout)
            raise ODOAException
        else:
            # Get random ayat.
            random_ayah = random.randint(1, int(data.get('count')))
            ayah_key = 'verse_{index}'.format(index=random_ayah)
            ayah = data['verse'][ayah_key].encode('utf-8')
            surah_index = data.get('index')
            surah_name = data.get('name')
            # Get translation and sound url.
            translation = self.__get_translation(surah=surah_index,
                                                 ayah=ayah_key,
                                                 lang=lang)
            sound = self.__get_sound(surah=surah_index, ayah=random_ayah)
            desc = '{name}:{ayah}'.format(name=surah_name, ayah=random_ayah)
            meta = Metadata(ayah, desc, translation, sound)
            return meta

    def __get_translation(self, surah, ayah, lang):
        """
        Perform http request to get translation from given surah, ayah and
        language.

        Parameter:
            :surah      --  Surah index from API pages.
            :ayat       --  Ayat key.
            :lang       --  Language code.

        Return:
            :string     --  Translation from given surah and ayat.
        """
        # Construct url to fetch translation data.
        url = '{base}/translations/{lang}/{lang}_translation_{surah}.json'.format(
            base=self.BASE_API, lang=lang, surah=int(surah)
        )
        try:
            response = urlopen(url)                             # Fetch data from give url.
            data = json.loads(response.read().decode('utf-8'))  # Get response and convert to dict.
            translation = data['verse'][ayah]
        except ODOAException:
            return None
        else:
            return translation

    def __get_sound(self, surah, ayah):
        """
        Perform http request to get sound from given surah and ayah.

        Parameter:
            :surah      --  Surah index from API pages.
            :ayat       --  Ayat key.

        Return:
            :string     --  URL for mp3 sound.
        """
        # Formatting ayah with 0 leading.
        # http://stackoverflow.com/questions/17118071/python-add-leading-zeroes-using-str-format
        format_ayah = '{0:0>3}'.format(ayah)
        sound_url = '{base}/sounds/{surah}/{ayah}.mp3'.format(
            base=self.BASE_API, surah=surah, ayah=format_ayah
        )
        return sound_url
