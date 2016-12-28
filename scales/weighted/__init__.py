import abc

from .integer import integer


__all__ = [
    integer
]


class Function(object):
    """Used to define functions that can be evaluated to weight selections.

    Function defines the abstract class that must be provided to the various
    weighted capabilities available in this package.  It defines a single method
    that all provided functions must implement.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def evaluate(self, value):
        pass
