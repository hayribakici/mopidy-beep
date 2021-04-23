#!/usr/bin/env python
'''
Setup script for Mopidy-Pummeluff module.
'''

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

setup(
    name='Mopidy-Beep',
    use_scm_version=True,
    url='https://github.com/hayribakici/mopidy-beep',
    license='Apache',
    author='Hayri Bakici',
    author_email='hayri.bakici@gmail.com',
    description='Beep is a Mopidy extension which allows you to receive auditive feedback for Mopidy events',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=[
        'tests',
        'tests.*',
    ]),
    zip_safe=False,
    include_package_data=True,
    
    install_requires=['setuptools'] + requirements,
    
    entry_points={
        'mopidy.ext': [
            'pummeluff = mopidy_pummeluff:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
