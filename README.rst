Python Quran ODOA 
=================
|pypy| |travis| 

.. |pypy| image:: https://img.shields.io/badge/latest_version-v1.4-yellow.svg
    :target: https://pypi.python.org/pypi/python-quran-odoa/1.4

.. |travis| image:: https://travis-ci.org/Keda87/python-quran-odoa.svg?branch=master
    :target: https://travis-ci.org/Keda87/python-quran-odoa

Python library to support ODOA (One Day One Ayat) campaign that will displaying random ayah within quran surah including the translation, currently supports only Bahasa Indonesia and English.

This library using datasource from `https://github.com/semarketir/quranjson <https://github.com/semarketir/quranjson>`_
 

Suitable for your bot or web apps.

Prerequisite:
-------------
- Python v2.*

Installation:
-------------

**Manual**

- Clone repo : https://github.com/Keda87/python-quran-odoa.git
- Run : ``python setup.py install``

**PIP**

- ``pip install python-quran-odoa``

**easy_install**

- ``easy_install python-quran-odoa``

**Usage:**
::
    from odoa import ODOA
   
    odoa = ODOA()
   
    # by default the translation using bahasa indonesia,
    # pass `lang='en'` if you want english translation.
    surah = odoa.get_random_surah()  # odoa.get_random_surah(lang='en')
    
    surah.get('ayat')
    surah.get('translate')
    surah.get('sound')
    surah.get('description')
