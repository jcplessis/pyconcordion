#!/usr/bin/env python
from distutils.core import setup

setup(name='PyConcordion',
      version='0.10.0',
      description='Concordion python port',
      author='Plessis Jean-Christophe',
      author_email='jcplessis@gmail.com',
      url='http://code.google.com/p/pyconcordion/',
      packages=['concordion', 'concordion.impl'],
      package_data={'concordion': ['*.ini', 'lib/*.jar']},
      scripts=['scripts/concordion_folder_runner', 'scripts/concordion_file_runner', ],
      data_file=[('bin/', ['scripts/concordion_folder_runner', 'scripts/concordion_file_runner', ])]
)
