# Copyright 2017 Real Kinetic, LLC. All Rights Reserved.

from distutils.core import setup

from setuptools import find_packages


setup(
    name='kinetic-scales',
    packages=find_packages(),
    version='v1.0.1',
    description='A library with some selection and weighted choice algorithms.',
    author='Real Kinetic',
    author_email='dev@realkinetic.com',
    url='https://github.com/RealKinetic/scales',
    download_url='https://github.com/RealKinetic/scales/archive/v1.0.1.tar.gz',
    keywords=['weighted', 'random', 'choice'],
    classifiers=[],
    install_requires=['fuzzywuzzy'],
)
