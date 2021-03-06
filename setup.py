#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'flake8', 'coverage', 'pre-commit', 'flake8-future-import', 'mccabe' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Kalibrr Development Team",
    author_email='devs@kalibrr.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Pre-commit hook for flake8, with some plugins",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='flake8_precommit_hook',
    name='flake8_precommit_hook',
    packages=find_packages(include=['flake8_precommit_hook']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kalibrr/flake8_precommit_hook',
    version='0.1.0',
    zip_safe=False,
)
