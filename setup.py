#!/usr/bin/env python
from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
 name='TP1-Bornet-CDOF2',
 version='1.0',
 author='LambdaFr',
 license='MIT',
 long_description=open('README.md').read(),
 install_requires=required,
)
