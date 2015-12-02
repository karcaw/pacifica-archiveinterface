#!/usr/bin/env python

from distutils.core import setup

setup(name='PacificaArchiveInterface',
      version='1.0',
      description='Pacifica Archive Interface',
      author='David Brown',
      author_email='david.brown@pnnl.gov',
      packages=['pacifica'],
      scripts=['scripts/server.py']
     )
