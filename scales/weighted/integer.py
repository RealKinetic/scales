import random


def integer(function, floor, ceiling):
    """ Returns a random integer between (and including) and the provided floor and ceiling parameters.

    The returned integer lies within the range [floor, ceiling].  The provided function determines how the values
    in the range will be weighted.  Important note, this is pseudo-random.

    :param function: defines the weight assigned to the range of integers
    :type function: Function as defined in __init__.py
    :param floor: minimum random value
    :type floor: int
    :param ceiling: maximum random value
    :rtype ceiling: int
    :return: weighted random value
    :rtype: int
    :raises: ValueError if floor > ceiling
    """
    if floor > ceiling:
        raise ValueError('floor %d must be greater than ceiling %d' % (floor, ceiling))

    # fairly simple algorithm, sums all the weights, chooses a random value between 0 and summation, and iterates
    # to find the index of the value that surpasses the random value.  That will match the choice.

    weights = [function(i) for i in xrange(floor, ceiling)]
    total = sum(weights)

    selection = random.uniform(0, total)
    agg = 0
    for i, value in enumerate(xrange(floor, ceiling)):
        agg += weights[i]
        if agg >= selection:
            return value

    assert False, "bug in weighted code"
