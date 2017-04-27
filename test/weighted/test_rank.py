import unittest

from scales.weighted import rank


class RankTestCase(unittest.TestCase):
    def test_simple_rank(self):
        r1 = rank.WeightedIterable(1, ['a', 'b'])
        r2 = rank.WeightedIterable(2, ['a', 'b'])

        result = rank.rank(r1, r2)
        self.assertEqual(['a', 'b'], result)

    def test_simple_rank_reverse(self):
        r1 = rank.WeightedIterable(1, ['a', 'b'])
        r2 = rank.WeightedIterable(2, ['b', 'a'])

        result = rank.rank(r1, r2)
        self.assertEqual(['b', 'a'], result)

    def test_rank_heterogenous_lists(self):
        r1 = rank.WeightedIterable(1, ['a', 'c'])
        r2 = rank.WeightedIterable(2, ['b', 'a'])

        result = rank.rank(r1, r2)
        self.assertEqual(['a', 'b', 'c'], result)

    def test_rank_empty_list(self):
        result = rank.rank()
        self.assertEqual([], result)

    def test_rank_empty_iterable(self):
        r1 = rank.WeightedIterable(1, [])
        r2 = rank.WeightedIterable(2, ['b', 'a'])

        result = rank.rank(r1, r2)
        self.assertEqual(['b', 'a'], result)

    def test_rank_three_iterables(self):
        r1 = rank.WeightedIterable(1, ['a', 'b'])
        r2 = rank.WeightedIterable(2, ['b', 'a'])
        r3 = rank.WeightedIterable(3, ['a', 'b'])

        result = rank.rank(r1, r2)
        self.assertEqual(['b', 'a'], result)
