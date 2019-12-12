#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for module static_vars
"""
from static_vars import static_vars


def test_static_vars():

    @static_vars(counter=0)
    def foo():
        foo.counter += 1

    foo()
    foo()
    assert foo.counter==2
    foo.counter = 0
    foo()
    assert foo.counter==1

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_static_vars

    print("__main__ running", the_test_you_want_to_debug)
    the_test_you_want_to_debug()
    print('-*# finished #*-')

# eof