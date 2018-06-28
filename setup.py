#!/usr/bin/env python

import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from subfinder import __version__, __author__
version = __version__
author = __author__


if not version:
    raise RuntimeError('Cannot find version information')
if not author:
    raise RuntimeError('Cannot find author information')

requires = []
with open('requirements.txt') as fp:
    for line in fp:
        line = line.strip()
        if line.startswith('#'):
            continue
        requires.append(line)

setup(name='SubFinder',
      version=version,
      description='SubFiner',
      author=author,
      url='https://github.com/ausaki/subfinder/',
      packages=['subfinder', 'subfinder.subsearcher'],
      entry_points={
            'console_scripts': [
                  'subfinder = subfinder.run_gevent:run',
                  'subutils = subfinder.utils:main'
            ]
      },
      install_requires=requires,
      setup_requires=["pytest-runner", ],
      tests_require=["pytest", ],
    )
