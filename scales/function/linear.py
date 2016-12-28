from ..weighted import Function


class Linear(Function):
    """ Implements an linear-based algorithm for evaluation.

    Tends to have the lightest drop-off of all.
    """
    def __init__(self, slope=1, y_intercept=0):
        """Initialize defining the slope of the line and the y-intercept.  In this form, the weight = mx + b.  Using
        a slope of 0 effectively makes this a constant function that returns the y-intercept.

        :param slope: defines how drastic the curve weights items.
        :type slope: int or long
        :param y_intercept: defines some constant offset to apply to the resulting value
        :type y_intercept: int or long or float
        """
        self._slope = slope
        self._y_intercept = y_intercept

    def evaluate(self, value):
        """Evaluates the resulting value on a simple y = mx + b line.

        :param value: the value for x
        :type value: int or long
        :return: y
        :rtype: float
        """
        return float(self._slope) * value + self._y_intercept
