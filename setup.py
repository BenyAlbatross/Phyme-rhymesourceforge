#!/usr/bin/env python

from setuptools import setup
from Phyme import version

setup(name='Phyme',
      packages=['Phyme'],
      version=version,
      description='Python rhyming dictionary for songwriting',
      author='James Wenzel',
      author_email='wenzel.james.r@gmail.com',
      url='https://github.com/jameswenzel/Phyme',
      download_url=('https://github.com/jameswenzel/Phyme/tarball/' + version),
      license='MIT License',
      keywords=['songwriting', 'rhyme', 'rhyming', 'dictionary', 'slant',
                'rhymes', 'song', 'writing'],
      classifiers=[])