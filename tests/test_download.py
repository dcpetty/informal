#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_doctests.py
#
import os, shutil, unittest
from . import log, download

"""
Tests src/readdoctest.
"""

# Set up logging.
logger = log.log(__name__, 'tests')


class TestReaddoctest(unittest.TestCase):

    def setUp(self):
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        dot = os.path.dirname(os.path.realpath(__file__))
        self.remove = os.path.join(dot, REMOVE)
        os.makedirs(self.remove, exist_ok=True)
        pass

    def tearDown(self):
        """Clean up pathnames and any added directories."""
        shutil.rmtree(self.remove)
        pass

    def test_testdict(self):
        uri = 'https://raw.githubusercontent.com/dcpetty/informal/main/tests/data.txt'
        logger.info(download.download(uri, self.remove))
        logger.info(download.download(uri, self.remove, 'foo.txt'))
        pass
