#!/usr/bin/env python

from distutils.core import setup

setup(name='rhyme',
      version='0.1',
      description='A rhyming library',
      author='Ian Overgard',
      author_email='ian.overgard@gmail.com',
      url='http://github.com/fathat/pyrhyme',
      py_modules=['rhyme'],
      data_files=[('data', ['data/rhyme.db'])]
      )