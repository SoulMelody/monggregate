"""
Module defining an interface to the $ifNull operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------------------------------------
Last Updated (in this package) : 14/08/2023
Source : https://docs.mongodb.com/manual/reference/operator/aggregation/ifNull/#mongodb-expression-exp.-ifNull

Definition
-------------------
$ifNull
Changed in version 5.0.

The $ifNull expression evaluates input expressions for null values and returns:

    * The first non-null input expression value found.

    * A replacement expression value if all input expressions evaluate to null.

$ifNull treats undefined values and missing fields as null.

Syntax:

    >>> {
            $ifNull: [
                <input-expression-1>,
                ...
                <input-expression-n>,
                <replacement-expression-if-null>
            ]
        }

In MongoDB 4.4 and earlier versions, $ifNull only accepts a single input expression:
$ifNull requires all three arguments (if-then-else) for either syntax.

    >>> {
            $ifNull: [
                <input-expression>,
                <replacement-expression-if-null>
            ]
        }


"""

from typing import Any

from monggregate.base import Expression
from monggregate.operators.conditional.conditional import ConditionalOperator


class IfNull(ConditionalOperator):
    """
    Abstraction of MongoDB $cond operator which evaluates input expressions
    for null values and returns the first non-null input expression value
    found or a replacement expression value if all input expressions
    evaluate to null.

    Attributes
    -------------------
        - expression, Any : the boolean expression to evaluate
        - output, Any : the expression to evaluate if expression is null

    Online MongoDB documentation
    ----------------------------
    The $ifNull expression evaluates input expressions for null values and returns:

        * The first non-null input expression value found.

        * A replacement expression value if all input expressions evaluate to null.

    $ifNull treats undefined values and missing fields as null.

    [Source](https://docs.mongodb.com/manual/reference/operator/aggregation/ifNull/#mongodb-expression-exp.-ifNull)
    """

    operand: Any  # NOTE : Maybe diverge from Mongo and do not allow multiple expressions <VM, 14/08/2023>
    output: Any

    @property
    def expression(self) -> Expression:
        return self.express({"$ifNull": [self.operand, self.output]})


def if_null(operand: Any, output: Any) -> IfNull:
    """Returns an $if_null operator"""

    return IfNull(operand=operand, output=output)
