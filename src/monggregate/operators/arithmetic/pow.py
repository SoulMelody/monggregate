"""
Module defining an interface to the $pow operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------------------------------------
Last Updated (in this package) : 14/08/2023
Source : https://docs.mongodb.com/manual/reference/operator/aggregation/pow/#mongodb-expression-exp.-pow

Definition
-------------------
$pow
Raises a number to the specified exponent and returns the result.
$pow has the following syntax:.

The $pow expression has the following syntax:

    >>> { $pow: [ <expression1>, <expression2>] }

The <number> expression can be any valid expression as long as it resolves to a number.

The <exponent> expression can be any valid expression as long as it resolves to a number.

You cannot raise 0 to a negative exponent.

Behavior
-------------------

The result will have the same type as the input except when it cannot be represented accurately in that type. In these cases:

    * A 32-bit integer will be converted to a 64-bit integer if the result is representable as a 64-bit integer.

    * A 32-bit integer will be converted to a double if the result is not representable as a 64-bit integer.

    * A 64-bit integer will be converted to double if the result is not representable as a 64-bit integer.

If either argument resolves to a value of null or refers to a field that is missing, $pow returns null.
If either argument resolves to NaN, $pow returns NaN.


"""

from typing import Any

from monggregate.base import Expression
from monggregate.operators.arithmetic.arithmetic import ArithmeticOperator


class Pow(ArithmeticOperator):
    """
    Abstraction of MongoDB $pow operator which raises a number to the specified exponent.

    Attributes
    -------------------
        - number, Any : the numerator of the division
        - exponent, Any : the denominator of the division

    Online MongoDB documentation
    ----------------------------
    Raises a number to the specified exponent and returns the result.
    $pow has the following syntax:.

    The $pow expression has the following syntax:

        >>> { $pow: [ <expression1>, <expression2>] }

    The <number> expression can be any valid expression as long as it resolves to a number.

    The <exponent> expression can be any valid expression as long as it resolves to a number.

    You cannot raise 0 to a negative exponent.
    [Source](https://docs.mongodb.com/manual/reference/operator/aggregation/pow/#mongodb-expression-exp.-pow)
    """

    number: Any
    exponent: Any

    @property
    def expression(self) -> Expression:
        return self.express({"$pow": [self.number, self.exponent]})


def pow(number: Any, exponent: Any) -> Pow:
    """Returns a $pow operator"""

    return Pow(number=number, exponent=exponent)
