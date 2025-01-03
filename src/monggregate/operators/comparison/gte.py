"""
Module defining an interface to MongoDB $gte operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------------------------------------
Last Updated (in this package) : 19/11/2022
Source : https://www.mongodb.com/docs/manual/reference/operator/aggregation/gte/#mongodb-expression-exp.-gte

$gte
Compares two values and returns:

    * true when the first value is greater than  or equivalent the second value.

    * false when the first value is less than to the second value.

The $gte compares both value and type, using the specified BSON comparison order for values of different types.

$gt has the following syntax:

    >>> { $gte: [ <expression1>, <expression2> ] }

For more information on expressions, see Expressions.
"""

from typing import Any

from monggregate.base import Expression
from monggregate.operators.comparison.comparator import Comparator


class GreatherThanOrEqual(Comparator):
    """
    Abstraction of MongoDB $gte operator which compares two values and
    returns true when the first value is greater than or equivalent to the
    second value and false otherwise.

    Attributes
    -------------------
        - left, Any :Left operand. Can be any valid expression.
        - right, Any :Right operand. Can be any valid expression.

    Online MongoDB documentation
    ----------------------------
    Compares two values and returns:

        * true when the first value is greater than  or equivalent the second value.

        * false when the first value is less than to the second value.

    The $gte compares both value and type, using the specified BSON comparison order for values of different types.

    $gt has the following syntax:

        >>> { $gte: [ <expression1>, <expression2> ] }

    For more information on expressions, see Expressions.

    [Source](https://www.mongodb.com/docs/manual/reference/operator/aggregation/gte/#mongodb-expression-exp.-gt)
    """

    @property
    def expression(self) -> Expression:
        return self.express({"$gte": [self.left, self.right]})


Gte = GreatherThanOrEqual


def grether_than_or_equal(left: Any, right: Any) -> GreatherThanOrEqual:
    """Returns a $gte operator"""

    return GreatherThanOrEqual(left=left, right=right)


gte = grether_than_or_equal
