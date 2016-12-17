import math

from ..weighted import Function


class Exponential(Function):
    """ Implements an exponential based algorithm for evaluation.

    Tends to have tighter drop offs than hyperbolic algorithm.
    """
    def __init__(self, scalar=1):
        """Scalar is a user-defined adjustment that can be made to the slope of the exponential algorithm.
        High scalars will result in steeper drops and a shorter tail.  Small scalars (ie, .1) will result in a
        linear-looking graph with a very long tail.  The scalar can also be used to determine direction of the slope,
        ie, using a negative scalar.

        :param scalar: user-defined slope adjustment
        :type scalar: int or long
        """
        self._scalar = scalar

    def evaluate(self, value):
        """Returns e**(scalar * value).

        :param value: value to use as the exponent to e
        :type value: int or long
        :return: long
        """
        return math.exp(self._scalar * value)
