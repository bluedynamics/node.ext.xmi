# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc ="AGX XMI Input/Output"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name='agx.io.xmi',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
      ],
      keywords='AGX, Code Generator',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'https://svn.plone.org/svn/archetypes/AGX',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['agx', 'agx.io'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'agx.io.xml',
      ],
      extras_require = dict(
          test=[
            'interlude',
            'zope.configuration',
          ]
      ),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )