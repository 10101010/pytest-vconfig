#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = ['python-consul', 'vyper-config']

setup_requirements = ['pytest-runner', ]


setup(
    author="Ruslan Kirilyuk",
    author_email='godi4e@gmail.com',
    classifiers=[
        'Framework :: Pytest',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Simple vyper-config wrapper",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'configuration',
    ],
    name='pytest-vconfig',
    packages=find_packages(include=['pytest_vconfig']),
    setup_requires=setup_requirements,
    version='0.0.1',
    zip_safe=False,
    entry_points={
        'pytest11': [
            'pytest-vconfig = pytest_vconfig.plugin',
        ]
    }
)