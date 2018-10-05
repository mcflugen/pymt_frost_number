#! /usr/bin/env python
import os
import sys

import numpy as np
import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension

try:
    import model_metadata
except ImportError:

    def get_cmdclass(*args, **kwds):
        return kwds.get("cmdclass", None)

    def get_entry_points(*args):
        return None


else:
    from model_metadata.utils import get_cmdclass, get_entry_points


packages = find_packages()
pymt_components = [
    (
        "BmiFrostNumberMethod=permamodel.components.bmi_frost_number:BmiFrostnumberMethod",
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
