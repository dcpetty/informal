#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __init__.py
#
# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path as _p
from pathlib import Path as _P
from collections import OrderedDict as _OD
# path hack: add package directory to path.
_p.insert(1, str(_P(__file__).resolve().parents[2]))
_p = list(_OD.fromkeys(_p))

from src import *

"""
__init__.py for informal/tests/.
"""

__version__ = '0.0.1'

__all__ = ['download', 'doctests',
    'test_doctests', 'test_download',
    '__version__', ]
