# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
import os
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    dependencies = [dep.strip() for dep in f.readlines()]

setup(
    name='python-quran-odoa',
    py_modules=['odoa'],

    install_requires=dependencies,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='2.0.0',

    description='Library to get random ayah within quran including the translation.',
    long_description='Library to get random ayah within quran including the translation.',

    # The project's main homepage.
    url='https://github.com/Keda87/python-quran-odoa',

    # Author details
    author='Keda87',
    author_email='adiyatmubarak@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='development quran',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
