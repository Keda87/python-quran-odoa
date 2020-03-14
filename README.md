Python Quran ODOA 
=================
[![Build Status](https://travis-ci.org/Keda87/python-quran-odoa.svg?branch=master)](https://travis-ci.org/Keda87/python-quran-odoa) 
[![pypi](https://badge.fury.io/py/python-quran-odoa.svg)](https://badge.fury.io/py/python-quran-odoa) 
[![codecov](https://codecov.io/gh/Keda87/python-quran-odoa/branch/master/graph/badge.svg)](https://codecov.io/gh/Keda87/python-quran-odoa)

Python library to display random ayah within quran surah including the translation.
Currently supports only Bahasa Indonesia and English.

This library is part of supporting ODOA (One Day One Ayat) campaign and using datasource from [quranjson](https://github.com/semarketir/quranjson).
 

Prerequisite:
-------------
- Python v3.6.+

Installation:
-------------

**Pip:**

```bash
$ pip install python-quran-odoa
```

**Usage:**

```python
from odoa import ODOA

o = ODOA()

# by default the translation using bahasa indonesia,
# pass `lang='en'` if you want english translation.
surah = await o.get_random_surah()  # odoa.get_random_surah(lang='en')

surah.ayah
surah.desc
surah.translate
surah.sound
```
