#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_doctests.py
#
import copy, functools, doctest, re
"""
Read and parse doctest strings from .TXT files and use results with @test 
decorator to add complicated or verbose doctest strings to functions also for
use in https://colab.research.google.com/ notebooks. Useful links:
https://realpython.com/primer-on-python-decorators/#decorating-functions-with-arguments
https://stackoverflow.com/questions/5929107/decorators-with-parameters
https://www.artima.com/weblogs/viewpost.jsp?thread=240845
"""


def testdict(pathname):
    """Return dictionary of tests where key is function name and tests are
     doctest-style tests parsed from pathname. Each doctest starts with
     '>>> ' and includes 'function(' for function to test."""
    with open(pathname) as f:
        regex, lines = re.compile(r'[>]+\s+([^(]+)'), f.readlines()
        td, tn, test = dict(), None, None
        for i, line in enumerate(lines):
            match = regex.match(line)
            if match:
                if tn:
                    td[tn] = test
                test = td.get(tn := match.groups()[0], list())
            test.append(line)
    return {k: ''.join(v).strip() for k, v in td.items()}


def test(tests):
    """Decorator that takes doctest string dictionary and suns doctests
    associated with named function."""
    def decorator(function):
        globs = copy.copy(globals())
        globs.update({function.__name__: function})
        function.__doc__ = tests.get(function.__name__, '')
        doctest.run_docstring_examples(function, globs, name=function.__name__,
            verbose=True)
        @functools.wraps(decorator)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
    return decorator
