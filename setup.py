#!/usr/bin/env python

from setuptools import setup

setup(
    name='metarng',
    version='1.0',
    description='Package to help aviators collect metar data from weather stations.',
    author='Matt York',
    author_email='matthewy@jfrog.com',
    url='https://github.com/my0373/fgmetar',
    packages=['metarng'],
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
)