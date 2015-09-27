Python Quran ODOA
=================
Python library to support ODOA (One Day One Ayat) campaign that will displaying random ayat within quran surah including the translation. 

This project is part of `https://github.com/semarketir/quranjson-odoa <https://github.com/semarketir/quranjson-odoa>`_
 

Suitable for your bot or web apps.

Prerequisite:
-------------
- Python v2.* & v3.*

Installation:
-------------

**Manual:**

- Clone repo : https://github.com/Keda87/python-quran-odoa.git
- Run : ``python setup.py install``

**pip:**

- ``pip install python-quran-odoa``

**easy_install:**

- ``easy_install python-quran-odoa``

**Usage:**

  from odoa import get_random_surah

  surah = get_random_surah()

  surah.get('ayat')

  surah.get('translate')

