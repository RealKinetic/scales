# Copyright 2017 Real Kinetic, LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import abc
import collections
import six


class WeightedBase(six.with_metaclass(abc.ABCMeta, collections.Iterable)):
    """Provides a simple iterable that takes a weight and applies it to the items
    in the iterator.  Items are given a score based on place in the iterator
    multiplied by the weight.  This is essentially a simple weighted sum
    model mixed with a Nauru count.
    """
    @abc.abstractproperty
    def weight(self):
        """Return a weight for this iterator.  This weight is applied to all
        items in the iterator.

        :return: weight of these items
        :rtype: number
        """
        pass


class WeightedIterable(WeightedBase):
    """A very simple default implementation of WeightedBase.
    """
    def __init__(self, weight, iterable):
        """Accepts a weight and any iterable which will be used to hydrate
        this iterable.

        :param weight: weight to apply to the items
        :type weight: number
        :param iterable: any iterable
        :type iterable: collections.Iterable
        """
        self._weight = weight
        self._iterable = iterable

    def __iter__(self):
        """Returns an iterator from the underlying iterable.

        :return: iterator
        :rtype: collections.Iterator
        """
        return iter(self._iterable)

    @property
    def weight(self):
        """The weight to apply to items from the iterator.

        :return: weight
        :rtype: number
        """
        return self._weight


def rank(*args):
    """Takes a list of WeightedBase and returns a sorted list of items by rank
    descending.  Items should all be of the same type.

    :return: sorted list of weighted items
    :rtype: list(object)
    """
    items = {}
    for ib in args:
        for i, item in enumerate(ib):
            if item not in items:
                items[item] = 0.0

            items[item] += 1.0/(i + 1) * ib.weight

    weighted = [(score, value) for value, score in items.iteritems()]
    weighted = sorted(weighted, key=lambda x: x[0], reverse=True)
    return map(lambda x: x[1], weighted)
