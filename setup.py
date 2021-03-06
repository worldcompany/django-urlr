#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-urlr',
    version='1.0.0',
    description='Use the bit.ly API to quickly create short links from an objects get_absolute_url method.',
    author='Adam Fast',
    author_email='adamfast@gmail.com',
    url='https://github.com/worldcompany/django-urlr',
    packages=find_packages(),
    package_data={
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    test_suite='runtests.runtests',
)
