"""
Module defining an interface to $or operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------------------------------------
Last Updated (in this package) : 19/11/2022
Source : https://www.mongodb.com/docs/manual/reference/operator/aggregation/or/#mongodb-expression-exp.-or

Definition
-----------------
$or
Evaluates one or more expressions and returns true if any of the expressions are true.
Otherwise, $or returns false.

$or has the following syntax:
    >>> { $or: [ <expression1>, <expression2>, ... ] }

For more information on expressions, see Expressions.

Behavior
------------------
In addition to the false boolean value,
$or evaluates as false the following: null, 0, and undefined values. The
$or evaluates all other values as true, including non-zero numeric values and arrays.

"""

from typing import Any

from monggregate.base import Expression
from monggregate.operators.boolean.boolean import BooleanOperator


class Or(BooleanOperator):
    """
    Abstraction of MongoDB $or operator evaluates one or more expressions and returns true if any of the expressions are true.

    Attributes
    -------------------
        - expressions, list[Expression] : list of valid expressions,
                                          that serve as operands for the or
                                          operation

    Online MongoDB documentation
    ----------------------------
    Evaluates one or more expressions and returns true if any of the expressions are true.
    Otherwise, $or returns false.

    $or has the following syntax:
        >>> { $or: [ <expression1>, <expression2>, ... ] }

    For more information on expressions, see Expressions.

    [Source](https://www.mongodb.com/docs/manual/reference/operator/aggregation/or/#mongodb-expression-exp.-or)

    """

    operands: list[Any]

    @property
    def expression(self) -> Expression:
        return self.express({"$or": self.operands})


def or_(*args: Any) -> Or:
    """Returns a $or operator"""

    return Or(operands=list(args))
