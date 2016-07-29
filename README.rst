Python Quran ODOA 
=================
|pypy| |travis| |Codecov|

.. |pypy| image:: https://badge.fury.io/py/python-quran-odoa.svg
    :target: https://badge.fury.io/py/python-quran-odoa

.. |travis| image:: https://travis-ci.org/Keda87/python-quran-odoa.svg?branch=master
    :target: https://travis-ci.org/Keda87/python-quran-odoa

.. |codecov| image:: https://codecov.io/gh/Keda87/python-quran-odoa/branch/master/graph/badge.svg?branch=master
    :target: https://codecov.io/gh/Keda87/python-quran-odoa


Python library to display random ayah within quran surah including the translation. Currently supports only Bahasa Indonesia and English.

This library is part of supporting ODOA (One Day One Ayat) campaign and using datasource from `https://github.com/semarketir/quranjson <https://github.com/semarketir/quranjson>`_
 

Suitable for your bot or web apps.

Prerequisite:
-------------
- Python v2.* or Python v3.*

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
    
    surah.ayah
    surah.desc
    surah.translate
    surah.sound
