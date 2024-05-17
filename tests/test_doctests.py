#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_doctests.py
#
"""
Tests src/readdoctest.
"""
import os, shutil, unittest
from . import log, doctests
test = doctests.test

# Set up logging.
logger = log.log(__name__, 'tests')


class TestReaddoctest(unittest.TestCase):

    def setUp(self):
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        dot = os.path.dirname(os.path.realpath(__file__))
        self.remove = os.path.join(dot, REMOVE)
        os.makedirs(self.remove, exist_ok=True)
        self.data = os.path.realpath(os.path.join(dot, '../data/informal.txt'))

        self.n = 10
        self.list = list(range(self.n))
        pass

    def tearDown(self):
        """Clean up pathnames and any added directories."""
        shutil.rmtree(self.remove)
        pass


    def test_testdict(self):
        for k, v in doctests.testdict(self.data).items():
            logger.info(f"{k} doctest(s):\n{v}")
        pass

    def test_test(self):
        tests = {'sample': f">>> sample(10)\n{repr(self.list)}"}
        logger.info(f"@test: {tests}")
        @test(tests)
        def sample(n):
            """Sample function with tests."""
            return self.list
        logger.info(f"sample({self.n}): {sample(self.n)}")
        pass
