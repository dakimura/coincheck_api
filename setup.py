# -*- coding: utf-8 -*-

from io import open
from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    readme = f.read()

with open('LICENSE', encoding="utf-8") as f:
    license = f.read()

setup(
    name='coincheck_api',
    version='0.8.0',
    description='A simple library to use CoinCheck API',
    long_description=readme,
    author='dakimura',
    author_email='dakimura@example.com',
    url='https://github.com/dakimura/coincheck_api',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)