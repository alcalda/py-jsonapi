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
jsonapi.base.schema
===================

This module contains the essence of *py-jsonapi*: The schema/type definition.

.. toctree::
    :maxdepth: 1

    base_property
    id
    attribute
    relationship
    to_one_relationship
    to_many_relationship
    link
    meta
    type
"""

# local
from .attribute import Attribute, BoundAttribute
from .id import ID, BoundID
from .link import Link, BoundLink
from .meta import Meta, BoundMeta
from .relationship import RelationshipNotLoaded
from .to_one_relationship import ToOneRelationship, BoundToOneRelationship
from .to_many_relationship import ToManyRelationship, BoundToManyRelationship
from .type import Type