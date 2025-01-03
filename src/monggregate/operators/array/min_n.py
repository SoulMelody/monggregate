"""
Module defining an interface to $minN operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------

Last Updated (in this package) : 12/11/2022
Source : https://www.mongodb.com/docs/manual/reference/operator/aggregation/minN-array-element/#mongodb-expression-exp.-minN

Definition
------------------------
$minN
New in version 5.2.

Returns the n smallest values in an array.

Syntax
------------------------
$minN has the following syntax:

    >>> { $minN: { n: <expression>, input: <expression> } }

        Field           Description
    *   n               An expression that resolves to a positive integer.
                        The integer specifies the number of array elements
                        that $minN returns.
    *   input           An expression that resolves to the array from which to return
                        the maximal n elements.

Behavior
-----------------------
    * You cannot specify a value of n less than 1.

    * $minN filters out null values found in the input array.

    * If the specified n is greater than or equal to the number of elements in the input array,
      $minN returns all elements in the input array.

    * If input resolves to a non-array value, the aggregation operation errors.

    * If input contains both numeric and string elements,
      the string elements are sorted before numeric elements according to the BSON comparison order.


"""

from typing import Any

from monggregate.base import Expression, pyd
from monggregate.operators.array.array import ArrayOperator


class MinN(ArrayOperator):
    """
    Abstraction of MongoDB $minN operator which returns the n smallest values in an array.

    Attributes
    --------------------------
        - operand, Any:Any valid expression that resolves to an array
        - limit / n , int : An expression that resolves to a positive integer.
                            The integer specifies the number of array elements taht $maxN returns.

    Online MongoDB documentation
    ----------------------------
    Returns the n smallest values in an array.

    [Source](https://www.mongodb.com/docs/manual/reference/operator/aggregation/minN-array-element/#mongodb-expression-exp.-minN)
    """

    operand: Any = pyd.Field(alias="input")
    limit: Any = pyd.Field(1, alias="n")

    @property
    def expression(self) -> Expression:
        return self.express({"$minN": {"n": self.limit, "input": self.operand}})


def min_n(operand: Any, limit: Any = 1) -> MinN:
    """Returns a $minN operator"""

    return MinN(operand=operand, limit=limit)
