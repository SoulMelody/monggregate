"""
Module defining an interface to $maxN operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------

Last Updated (in this package) : 12/11/2022
Source : https://www.mongodb.com/docs/manual/reference/operator/aggregation/maxN-array-element/#mongodb-expression-exp.-maxN

Definiiton
-------------------------
New in version 5.2.

Returns the n largest values in an array.

Syntax
-------------------------
$maxN has the following syntax:

    >>> { $maxN: { n: <expression>, input: <expression> } }

        Field           Description
    *   n               An expression that resolves to a positive integer.
                        The integer specifies the number of array elements
                        that $maxN returns.
    *   input           An expression that resolves to the array from which to return
                        the maximal n elements.

Behavior
----------------------------
    * You cannot specify a value of n less than 1.

    * $maxN filters out null values found in the input array.

    * If the specified n is greater than or equal to the number of elements in the input array,
      $maxN returns all elements in the input array.

    * If input resolves to a non-array value, the aggregation operation errors.

    * If input contains both numeric and string elements,
      the string elements are sorted before numeric elements according to the BSON comparison order.



"""

from typing import Any

from monggregate.base import Expression, pyd
from monggregate.operators.array.array import ArrayOperator


class MaxN(ArrayOperator):
    """
    Abstraction of MongoDB $maxN operator which returns the n largest
    values in an array.

    Attributes
    --------------------------
        - operand, Any:Any valid expression that resolves to an array
        - limit / n , int : An expression that resolves to a positive integer.
                            The integer specifies the number of array elements taht $maxN returns.

    Online MongoDB documentation
    ----------------------------
    Returns the n largest values in an array.

    [Source](https://www.mongodb.com/docs/manual/reference/operator/aggregation/maxN-array-element/#mongodb-expression-exp.-maxN)
    """

    operand: Any = pyd.Field(alias="input")
    limit: Any = pyd.Field(1, alias="n")

    @property
    def expression(self) -> Expression:
        return self.express({"$maxN": {"n": self.limit, "input": self.operand}})


def max_n(operand: Any, limit: Any = 1) -> MaxN:
    """Returns a $maxN operator"""

    return MaxN(operand=operand, limit=limit)
