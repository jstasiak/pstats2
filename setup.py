from os.path import abspath, dirname, join

from setuptools import setup

PROJECT_ROOT = abspath(dirname(__file__))

description = 'pstats + modifications'

module_code = open(join(PROJECT_ROOT, 'pstats2.py')).readlines()
line = [line for line in module_code if line.startswith('__version__ = ')][0]
version = line.split('=')[-1].strip().strip("'")

if __name__ == '__main__':
    setup(
        name='pstats2',
        url='http://github.com/jstasiak/pstats2',
        download_url='http://pypi.python.org/pypi/pstats2',
        version=version,
        description=description,
        license='Apache License, Version 2.0',
        platforms=['any'],
        py_modules=['pstats2'],
        author='Jakub Stasiak',
        author_email='jakub@stasiak.at',
        install_requires=[
            'setuptools >= 0.6b1',
            'six >= 1.3.0',
            'recordtype >= 1.1.0',
        ],
    )
