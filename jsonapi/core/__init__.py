#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2016 Benedikt Schmitt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
jsonapi.core
============

.. sidebar:: Asyncio Version

    You can find the base and schema for asynchronous frameworks here:
    :mod:`jsonapi.asyncio`.

This is the *base* of the *py-jsonapi* library. It contains the definitions for
interfaces (schema, handlers), which can be used to implement a JSON:API
compliant API.


.. Remember to add a .rst file for each Python module listed here in the
.. correct docs folder.

.. toctree::
    :maxdepth: 2

    api
    errors
    handler
    pagination
    request
    response
    utilities
    validation
"""

# local
from . import api
from . import errors
from . import handler
from . import request
from . import response
from . import utilities
from . import validation