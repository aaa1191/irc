#!/usr/bin/env python
# Generated by jaraco.develop 2.17.1
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools

with io.open('README.txt', encoding='utf-8') as readme:
    long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []

setup_params = dict(
    name='irc',
    use_scm_version=True,
    author="Joel Rosdahl",
    author_email="joel@rosdahl.net",
    maintainer="Jason R. Coombs",
    maintainer_email="jaraco@jaraco.com",
    description="IRC (Internet Relay Chat) protocol client library for Python",
    long_description=long_description,
    url="https://bitbucket.org/jaraco/irc",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'six',
        'jaraco.collections',
        'jaraco.text',
        'jaraco.itertools',
        'jaraco.logging',
        'jaraco.functools>=1.4',
    ],
    setup_requires=[
        'setuptools_scm>=1.5.3',
    ] + pytest_runner + sphinx,
    tests_require=[
        'pytest',
        'backports.unittest_mock',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    entry_points={
    },
)
if __name__ == '__main__':
    setuptools.setup(**setup_params)
