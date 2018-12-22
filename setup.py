#! /usr/bin/env python

# System imports
from distutils.core import *
from distutils      import sysconfig

from setuptools import setup, Extension
from Cython.Distutils import build_ext
import os

os.environ["CC"] = "gcc"
os.environ["CXX"] = "g++"


# Third-party modules - we depend on numpy for everything
import numpy

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

# command line arguments. used for compiling and linking
extra_cmd_args = ["-std=c++11", "-fopenmp"]

# crop extension module
_statmechtools = Extension("_statmechtools",
                   ["convolution.i","src/convolution.cpp"],
                   include_dirs = [numpy_include],
                   libraries=[],
                   language="c++",  # so that the compiler knows about the language
                   extra_compile_args = extra_cmd_args,                 
                   extra_link_args= extra_cmd_args,
                   swig_opts=['-c++']
                   )

# NumyTypemapTests setup
setup(  name        = "Statistical Mechanics Tools",
        description = "A program to compute convolution of data",
        author      = "M. S. Rahman",
        author_email= "shahnoor3pl@gmail.com",
        version     = "1.0",
        ext_modules = [_statmechtools]
        )