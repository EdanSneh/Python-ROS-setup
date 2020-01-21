#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

D = generate_distutils_setup(
    packages=['my_pkg'],
    package_dir={'': 'src'},
    requires=['roscpp'],
)

setup(**D)
