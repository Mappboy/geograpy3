"""Setup script for Geograpy Library."""
from setuptools import setup

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()

setup(name='geograpy3',
      version='1.0.0',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      url='https://github.com/mappboy/geograpy3',
      download_url='https://github.com/mappboy/geograpy3',
      author='Cameron Poole',
      author_email='cameron@mammothgeospatial.com',
      license='MIT',
      packages=['geograpy3'],
      tests_require=['pytest', ],
      install_requires=['numpy', 'nltk', 'jellyfish', 'pycountry', 'newspaper3k', 'spacy'],
      package_data={'geograpy3': ['data/*.csv']},
      zip_safe=False)
