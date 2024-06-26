#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __main__.py
#
# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path as _p
from pathlib import Path as _P
from collections import OrderedDict as _OD
# path hack: add package directory to path.
_p.insert(1, str(_P(__file__).resolve().parents[1]))
_p = list(_OD.fromkeys(_p))

import unittest

# import test modules.
from tests import *

"""
__main__.py  define run_tests and runs it.
"""

__version__ = "0.0.1"


def run_tests(verbosity=2):
    """Run all tests in test_paths."""

    # initialize the test suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(test_doctests))
    suite.addTests(loader.loadTestsFromModule(test_download))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

if __name__ == '__main__':
    run_tests()
