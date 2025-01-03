"""
Module defining an interface to MongoDB $lte operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------------------------------------
Last Updated (in this package) : 19/11/2022
Source : https://www.mongodb.com/docs/manual/reference/operator/aggregation/lte/#mongodb-expression-exp.-lte

$lt
Compares two values and returns:

    * true when the first value is less than or equivalent the second value.

    * false when the first value is greater than or equivalent to the second value.

The $gt compares both value and type, using the specified BSON comparison order for values of different types.

$lt has the following syntax:

    >>> { $lt: [ <expression1>, <expression2> ] }

For more information on expressions, see Expressions.
"""

from typing import Any

from monggregate.base import Expression
from monggregate.operators.comparison.comparator import Comparator


class LowerThanOrEqual(Comparator):
    """
    Abstraction of MongoDB $gt operator which compares two values and
    returns true when the first value is less than or equivalent the
    second value, and false otherwise.

    Attributes
    -------------------
        - left, Any :Left operand. Can be any valid expression.
        - right, Any :Right operand. Can be any valid expression.

    Online MongoDB documentation
    ----------------------------
    Compares two values and returns:

        * true when the first value is less than or equivalent the second value.

        * false when the first value is greater than or equivalent to the second value.

    The $gt compares both value and type, using the specified BSON comparison order for values of different types.

    $lt has the following syntax:

        >>> { $lt: [ <expression1>, <expression2> ] }

    For more information on expressions, see Expressions.

    [Source](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lte/#mongodb-expression-exp.-lte)

    """

    @property
    def expression(self) -> Expression:
        return self.express({"$lte": [self.left, self.right]})


Lte = LowerThanOrEqual


def lower_than_or_equal(left: Any, right: Any) -> LowerThanOrEqual:
    """Returns a $lt operator"""

    return LowerThanOrEqual(left=left, right=right)


lte = lower_than_or_equal
