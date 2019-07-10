#!/usr/bin/env python

import os
import re

from setuptools import setup
from setuptools import find_packages


def get_version(*file_paths):
    """Retrieves the version from annotation/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("sock", "__init__.py")

requirements = [
    'Django',
    'channels',
    'channels_redis',
]

test_requirements = [
    "pytest",
]

setup(
    name="sock",
    version=VERSION,
    description="django channels tutorial",
    author="nmaekawa",
    author_email="nmaekawa@g.harvard.edu",
    url="https://github.com/nmaekawa/sock",
    packages=find_packages(exclude=["docs", "tests*"]),
    package_dir={'hxarc': 'hxarc'},
    include_package_data=True,
    keywords="hxpy",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Inteded audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=[],
    tests_requires=test_requirements,
    zip_safe=False,
)
