===========
static_vars
===========

A decorator for adding static variables to a method.

Typical use:

.. code-block:: python

    from static_vars import static_vars

    # Add static variable <counter> to foo, to count the number of foo calls.
    #   Initialize to 0
    # Add static variable args, which keeps a list of the arguments with which
    #   foo was called. Initialize to []
    @static_vars(counter=0, args=[])
    def foo(arg=None):
        foo.counter += 1
        foo.args.append(arg)

    foo()
    foo()
    assert foo.counter==2
    assert foo.args== [None,None]

    foo.counter = 0
    foo('bar')
    assert foo.counter==1
    assert foo.args==[None,None,'bar']


* Free software: MIT license
* Documentation: https://static-vars.readthedocs.io.

