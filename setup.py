#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="spacy-tokenizations",
    description="A spaCy-packaged wrapper for the Rust tokenizations library",
    version="0.7.2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Rust",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["spacy_tokenizations", "spacy_tokenizations.tests"],
    rust_extensions=[RustExtension("spacy_tokenizations.tokenizations")],
    include_package_data=True,
    zip_safe=False,
)
