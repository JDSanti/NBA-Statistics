# -*- coding: utf-8 -*-

# Learn more: https://github.com/JDSanti/NBA-Statistics

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='NBA-Statistics',
    version='0.1.0',
    description='NBA Statistics executable written in python',
    long_description=readme,
    author='Jose Santiago',
    author_email='jduhamel.santiago@outlook.com',
    url='https://github.com/JDSanti/NBA-Statistics',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
