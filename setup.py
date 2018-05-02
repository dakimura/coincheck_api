# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='coincheck_api',
    version='0.2.0',
    description='A simple library to use CoinCheck API',
    long_description=readme,
    author='dakimura',
    author_email='dakimura@example.com',
    url='https://github.com/dakimura/coincheck_api',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)