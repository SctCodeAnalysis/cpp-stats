'''
Contains utilities for testing clang related code.
'''

import os

import clang.cindex
from functools import lru_cache

@lru_cache
def clang_index():
    try:
        clang.cindex.Config.set_library_file(os.getenv('LIBCLANG_LIBRARY_PATH'))
        print("(os.getenv('LIBCLANG_LIBRARY_PATH'): ", os.getenv('LIBCLANG_LIBRARY_PATH'))
        return clang.cindex.Index.create()
    except Exception:
        return None
