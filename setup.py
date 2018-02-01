#!/usr/bin/env python

from setuptools import setup

requirements = [
    'python-dateutil'
]

setup(name='multiply-workshop-utils',
      version='0.3',
      description='MULTIPLY Workshop Utils',
      author='MULTIPLY Team',
      packages=['multiply_workshop_utils'],
      install_requires=requirements
)
