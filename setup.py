from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from codecs import open
from os import path
import os
import subprocess

version = '0.0.1'
description = 'A program that does nothing'
url = 'https://github.com/kostrahb'
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='nothing',
	version=version,
	description=description,
	long_description=long_description,
	url=url,
	author='Kostrahb',
	author_email='vojta.kletecka@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
	],
	keywords='nothing',
	packages=['nothing'],
	entry_points={
		'console_scripts': [
			'nothing1 = nothing.nothing:functionThatDoesNothing1',
			'nothing2 = nothing.nothing:functionThatDoesNothing2',
		],
	},
)
