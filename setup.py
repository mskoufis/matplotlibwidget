"""Setup module for matplotlibwidget"""

from setuptools import setup, find_packages
from codecs import open
from os import path

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='matplotlibwidget',
    description='A PyDM widget to integrate matplotlib plots.',
    long_description=long_description,
    author='Michael Skoufis',
    author_email='skoufis@slac.stanford.edu',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='pydm matplotlib',
    packages=find_packages(exclude=['contrib', 'doc', 'tests']),
    install_requires=['pydm'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
