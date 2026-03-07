import sys
import os
from setuptools import setup, Extension

EXTRA_COMPILE_ARGS = []
if sys.platform in ('darwin', 'linux', 'linux2'):
  EXTRA_COMPILE_ARGS = ['-std=c++20']

AIS_MODULE = Extension(
  '_ais',
  extra_compile_args=EXTRA_COMPILE_ARGS,
  sources=[os.path.join('src', 'libais', fn) for fn in (
    'ais_py.cpp',
    'ais.cpp',
    'ais_bitset.cpp',
    'ais1_2_3.cpp',
    'ais4_11.cpp',
    'ais5.cpp',
    'ais6.cpp',
    'ais7_13.cpp',
    'ais8.cpp',
    'ais8_1_22.cpp',
    'ais8_1_26.cpp',
    'ais8_200.cpp',
    'ais8_366.cpp',
    'ais8_367.cpp',
    'ais9.cpp',
    'ais10.cpp',
    'ais12.cpp',
    'ais14.cpp',
    'ais15.cpp',
    'ais16.cpp',
    'ais17.cpp',
    'ais18.cpp',
    'ais19.cpp',
    'ais20.cpp',
    'ais21.cpp',
    'ais22.cpp',
    'ais23.cpp',
    'ais24.cpp',
    'ais25.cpp',
    'ais26.cpp',
    'ais27.cpp'
  )]
)

setup(ext_modules=[AIS_MODULE])
