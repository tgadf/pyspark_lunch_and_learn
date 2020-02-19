from distutils.core import setup
import setuptools

setup(
  name = 'pyspark_lunch_and_learn',
  py_modules = ['timeUtils'],
  version = '0.0.1',
  description = 'General Utility Functions',
  long_description = open('README.md').read(),
  author = 'Thomas Gadfort',
  author_email = 'tgadfort@gmail.com',
  license = "MIT",
  url = 'https://github.com/tgadf/pyspark_lunch_and_learn',
  keywords = ['utilities', 'network'],
  classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires = ['numpy>=1.15.1', 'pandas>=0.23.4', 'matplotlib>=2.2.2', 'python-dateutil>=2.7.3', 'seaborn>=0.9.0', 'pyspark', 'bs4>=0.0.1', 'scikit-learn>=0.20.3']
)
