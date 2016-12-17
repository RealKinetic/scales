from ..weighted import Function


class Hyperbolic(Function):
    """ Implements an hyperbolic based algorithm for evaluation.

    Tends to have looser drop off than exponential algorithm.
    """
    def __init__(self, scalar=1):
        """Scalar is a user-defined adjustment that can be made to the slope of the hyperbolic algorithm.
        High scalars will result in steeper drops and a shorter tail.  Small scalars (ie, .1) will result in a
        linear-looking graph with a very long tail.  The scalar can also be used to determine direction of the slope,
        ie, using a negative scalar.

        :param scalar: user-defined slope adjustment
        :type scalar: int or long
        """
        self._scalar = scalar

    def evaluate(self, value):
        """Returns 1 / (1 - scalar * value)

        :param value: value to use in the divisor
        :type value: int or long
        :return: long
        """
        return 1 / (1 - self._scalar * value)
