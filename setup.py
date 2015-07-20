# Copyright 2013-2014 Synappio LLC. All rights reserved.
import os

from setuptools import setup, find_packages

setup(
    name='wildcard-redirect',
    version='0.0',
    description='Just redirect some wildcard domain to a path',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    tests_require=[],
    entry_points="""\
    [paste.app_factory]
    wildcard-redirect = wcredir.main:app_factory
    """,
)
