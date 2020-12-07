#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools_rust import RustExtension


setup(
    name="spacy-tokenizations",
    version="0.7.2",
    packages=["spacy_tokenizations", "spacy_tokenizations.tests"],
    rust_extensions=[RustExtension("spacy_tokenizations.tokenizations")],
)
