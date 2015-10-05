Python Quran ODOA
=================
Python library to support ODOA (One Day One Ayat) campaign that will displaying random ayat within quran surah including the translation, currently supports only Bahasa Indonesia. 

This library using datasource from `https://github.com/semarketir/quranjson <https://github.com/semarketir/quranjson>`_
 

Suitable for your bot or web apps.

Prerequisite:
-------------
- Python v2.* & v3.*

Installation:
-------------

**Manual:**

- Clone repo : https://github.com/Keda87/python-quran-odoa.git
- Run : ``python setup.py install``

**PIP:**

- pip install python-quran-odoa

**Usage:**

    from odoa import ODOA
   
    odoa = ODOA()
  
    surah = odoa.get_random_surah()
  
    surah.get('ayat')
  
    surah.get('translate')
