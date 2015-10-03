import sys
import json
import random
import urllib2
import traceback


class ODOA(object):

    TOTAL_PAGES = 159
    BASE_API = 'https://raw.githubusercontent.com/semarketir/quranjson/master/source'
    SUPPORTED_LANGUAGES = ['id']

    def get_random_surah(self, lang='id'):
        """
        Perform http request to get random surah.

        Parameter:
            :lang       --  String contains language code.

        Return:
            :dict       --  Paired ayat with the translation.
        """

        # Ensure the language supported.
        if lang not in self.SUPPORTED_LANGUAGES:
            raise ValueError('Currently your selected language not yet supported.')

        # Get random surah and construct the url.
        random_pages = random.randint(1, self.TOTAL_PAGES)
        surah_url = '{base}/surah/surah_{pages}.json'.format(base=self.BASE_API,
                                                             pages=random_pages)

        try:
            response = urllib2.urlopen(surah_url)  # Fetch data from given url.
            data = json.loads(response.read())     # Get response and convert to dict.
        except IOError:
            traceback.print_exc(file=sys.stdout)
            return {}
        else:
            # Get random ayat.
            random_ayat = random.randint(1, int(data.get('count')))
            ayat_key = 'verse_{index}'.format(index=random_ayat)
            ayat = data['verse'][ayat_key]

            translation = self.__get_translation(surah=data.get('index'), ayat=ayat_key, lang=lang)

            return {'ayat': ayat, 'translate': translation}

    def __get_translation(self, surah, ayat, lang):
        """
        Perform http request to from given surah.

        Parameter:
            :surah      --  Surah index from API pages.
            :ayat       --  Ayat key.
            :lang       --  Language code.

        Return:
            :string     --  Translation from given surah and ayat.
        """

        # Construct url to fetch translation data.
        translation_url = '{base}/translations/{lang}/{lang}_translation_{surah}.json'\
                          .format(base=self.BASE_API, lang=lang, surah=int(surah))

        try:
            response = urllib2.urlopen(translation_url)  # Fetch data from give url.
            data = json.loads(response.read())           # Get response and convert to dict.
            translation = data['verse'][ayat]
        except IOError:
            return None
        else:
            return translation