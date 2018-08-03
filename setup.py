#! /usr/bin/env python
import os, sys

from setuptools import setup, find_packages

# from Cython.Build import cythonize
from distutils.extension import Extension
import versioneer

from model_metadata.utils import get_cmdclass, get_entry_points




packages = find_packages(include=["pymt_frost_number"])
pymt_components = [
    (
        "BmiFrostnumberMethod=permamodel.components.bmi_frost_number:BmiFrostnumberMethod",
        "meta",
    )
]

setup(
    name="pymt_frost_number",
    author="Eric Hutton",
    description="PyMT plugin frost_number",
    version=versioneer.get_version(),

    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
