#!/usr/bin/env python
from setuptools import setup

setup(
    name="sklearn-crfsuite",
    version="0.5.0",
    author="Mikhail Korobov",
    author_email="kmike84@gmail.com",
    license="MIT license",
    long_description=open("README.rst").read() + "\n\n" + open("CHANGES.rst").read(),
    long_description_content_type="text/x-rst",
    description="CRFsuite (python-crfsuite) wrapper which provides interface simlar to scikit-learn",
    url="https://github.com/TeamHG-Memex/sklearn-crfsuite",
    zip_safe=False,
    packages=["sklearn_crfsuite"],
    install_requires=[
        "python-crfsuite >= 0.9.7",
        "scikit-learn >= 0.24.0",
        "tabulate >= 0.4.2",
        "tqdm >= 2.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
