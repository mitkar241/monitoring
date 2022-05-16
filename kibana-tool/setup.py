#!/usr/bin/python3

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='kibanatool',
    version='1.0.0',
    author='Raktim Halder', 
    author_email='raktimhalder241@gmail.com',
    packages=find_packages(),
    long_description=open('README.md').read()
)
