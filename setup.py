#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = ''
with open('pywebtasks/__init__.py', 'r', 'utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', 'r', 'utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = []
test_requirements = []

setup(
    name='pywebtasks',
    version=version,
    description="Python wrapper for Auth0's Webtask API.",
    long_description=readme + '\n\n' + history,
    author="Sebastián J. Seba",
    author_email='ssebastianj@gmail.com',
    url='https://github.com/ssebastianj/pywebtasks',
    packages=[
        'pywebtasks',
    ],
    package_dir={'pywebtasks':
                 'pywebtasks'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pywebtasks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='test_pywebtasks.py',
    tests_require=test_requirements
)
