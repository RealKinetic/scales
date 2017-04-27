# Copyright 2017 Real Kinetic, LLC. All Rights Reserved.

import unittest

from scales.weighted import rank


class RankTestCase(unittest.TestCase):
    def test_simple_rank(self):
        r1 = rank.WeightedIterable(1, ['a', 'b'])
        r2 = rank.WeightedIterable(2, ['a', 'b'])

        result = rank.sort(r1, r2)
        self.assertEqual(['a', 'b'], result)

    def test_simple_rank_reverse(self):
        r1 = rank.WeightedIterable(1, ['a', 'b'])
        r2 = rank.WeightedIterable(2, ['b', 'a'])

        result = rank.sort(r1, r2)
        self.assertEqual(['b', 'a'], result)

    def test_rank_heterogenous_lists(self):
        r1 = rank.WeightedIterable(1, ['a', 'c'])
        r2 = rank.WeightedIterable(2, ['b', 'a'])

        result = rank.sort(r1, r2)
        self.assertEqual(['a', 'b', 'c'], result)

    def test_rank_empty_list(self):
        result = rank.sort()
        self.assertEqual([], result)

    def test_rank_empty_iterable(self):
        r1 = rank.WeightedIterable(1, [])
        r2 = rank.WeightedIterable(2, ['b', 'a'])

        result = rank.sort(r1, r2)
        self.assertEqual(['b', 'a'], result)

    def test_rank_three_iterables(self):
        r1 = rank.WeightedIterable(1, ['a', 'b'])
        r2 = rank.WeightedIterable(2, ['b', 'a'])
        r3 = rank.WeightedIterable(3, ['a', 'b'])

        result = rank.sort(r1, r2, r3)
        self.assertEqual(['a', 'b'], result)


class Item(object):
    def __init__(self, value, str_):
        self.value = value
        self.str_ = str_


def key(item):
    return item.str_


class FuzzyRankTestCase(unittest.TestCase):
    def test_simple_fuzzy_rank(self):
        r1 = rank.WeightedFuzzyStringIterable(
            1, key, [Item(1, 'abcd'), Item(2, 'efgh')]
        )
        r2 = rank.WeightedFuzzyStringIterable(
            2, key, [Item(3, 'efgh'), Item(4, 'abcd')]
        )

        result = rank.fuzzy_string_sort(50, r1, r2)
        self.assertEqual(
            [2, 1],
            [result.value for result in result],
        )

    def test_matching_fuzzy_rank(self):
        r1 = rank.WeightedFuzzyStringIterable(
            1, key, [Item(1, 'abcd'), Item(2, 'efgh')]
        )
        r2 = rank.WeightedFuzzyStringIterable(
            2, key, [Item(3, 'efwx'), Item(4, 'abyz')]
        )

        result = rank.fuzzy_string_sort(50, r1, r2)
        self.assertEqual(
            [2, 1],
            [result.value for result in result],
        )

    def test_heterogenous_ranks(self):
        r1 = rank.WeightedFuzzyStringIterable(
            1, key, [Item(1, 'abcd'), Item(2, 'efgh'), Item(5, '123')]
        )
        r2 = rank.WeightedFuzzyStringIterable(
            2, key, [Item(3, 'efwx'), Item(4, 'abyz')]
        )

        result = rank.fuzzy_string_sort(50, r1, r2)
        self.assertEqual(
            [2, 1, 5],
            [result.value for result in result],
        )

    def test_three_iterables(self):
        r1 = rank.WeightedFuzzyStringIterable(
            1, key, [Item(1, 'abcd'), Item(2, 'efgh')]
        )
        r2 = rank.WeightedFuzzyStringIterable(
            2, key, [Item(3, 'efwx'), Item(4, 'abyz')]
        )
        r3 = rank.WeightedFuzzyStringIterable(
            2, key, [Item(5, 'ef12'), Item(6, 'ab34')]
        )

        result = rank.fuzzy_string_sort(50, r1, r2, r3)
        self.assertEqual(
            [2, 1],
            [result.value for result in result],
        )

    def test_empty_list(self):
        result = rank.fuzzy_string_sort(50)
        self.assertEqual([], result)

    def test_empty_iterable(self):
        r1 = rank.WeightedFuzzyStringIterable(
            1, key, [Item(1, 'abcd'), Item(2, 'efgh')]
        )
        r2 = rank.WeightedFuzzyStringIterable(
            2, key, []
        )

        result = rank.fuzzy_string_sort(50, r1, r2)
        self.assertEqual(
            [1, 2],
            [result.value for result in result],
        )

    def test_single_iterable(self):
        r1 = rank.WeightedFuzzyStringIterable(
            1, key, [Item(1, 'abcd'), Item(2, 'efgh')]
        )

        result = rank.fuzzy_string_sort(50, r1)
        self.assertEqual(
            [1, 2],
            [result.value for result in result],
        )

    def test_second_and_third_iterable_match(self):
        r1 = rank.WeightedFuzzyStringIterable(
            1, key, [Item(1, 'abcd'), Item(2, 'efgh')]
        )
        r2 = rank.WeightedFuzzyStringIterable(
            2, key, [Item(3, 'efwx'), Item(4, 'mnop')]
        )
        r3 = rank.WeightedFuzzyStringIterable(
            2, key, [Item(5, 'ef12'), Item(6, 'mn67')]
        )

        result = rank.fuzzy_string_sort(50, r1, r2, r3)
        self.assertEqual(
            [2, 4, 1],
            [result.value for result in result],
        )
