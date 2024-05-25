#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# download.py
#
from os.path import basename, exists, join, realpath

"""
Adapted from Allen Downey Think Python v3 to download files from URIs. Useful
when adding specific files to a https://colab.research.google.com/ notebook.
"""

# https://colab.research.google.com/github/AllenDowney/ThinkPython/blob/v3/chapters/chap04.ipynb


def download(uri, directory='.', name=None):
    pathname = join(realpath(directory), name if name else basename(uri))
    if not exists(pathname):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(uri, pathname)
        print("Downloaded " + str(local))
    return pathname
