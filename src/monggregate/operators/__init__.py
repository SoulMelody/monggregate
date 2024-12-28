"""Operators Sub-package"""

# pylint: disable=redefined-builtin
from monggregate.operators.accumulators import (
    Average,  # noqa: F401
    Avg,  # noqa: F401
    Count,  # noqa: F401
    First,  # noqa: F401
    Last,  # noqa: F401
    Max,  # noqa: F401
    Min,  # noqa: F401
    Push,  # noqa: F401
    Sum,  # noqa: F401
    average,  # noqa: F401
    avg,  # noqa: F401
    count,  # noqa: F401
    first,  # noqa: F401
    last,  # noqa: F401
    max,  # noqa: F401
    min,  # noqa: F401
    push,  # noqa: F401
    sum,  # noqa: F401
)
from monggregate.operators.array import (
    ArrayToObject,  # noqa: F401
    Filter,  # noqa: F401
    #    First, first, #Commented as the array operator has the same name, syntax and does the same thing
    In,  # noqa: F401
    IsArray,  # noqa: F401
    #    Last, last,  #Commented as the array operator has the same name, syntax and does the same thing
    MaxN,  # noqa: F401
    MinN,  # noqa: F401
    Size,  # noqa: F401
    SortArray,  # noqa: F401
    array_to_object,  # noqa: F401
    filter,  # noqa: F401
    in_,  # noqa: F401
    is_array,  # noqa: F401
    max_n,  # noqa: F401
    min_n,  # noqa: F401
    size,  # noqa: F401
    sort_array,  # noqa: F401
)
from monggregate.operators.boolean import And, Not, Or, and_, not_, or_  # noqa: F401
from monggregate.operators.comparison import (
    Cmp,  # noqa: F401
    Compare,  # noqa: F401
    Eq,  # noqa: F401
    Equal,  # noqa: F401
    GreatherThan,  # noqa: F401
    GreatherThanOrEqual,  # noqa: F401
    Gt,  # noqa: F401
    Gte,  # noqa: F401
    LowerThan,  # noqa: F401
    LowerThanOrEqual,  # noqa: F401
    Lt,  # noqa: F401
    Lte,  # noqa: F401
    Ne,  # noqa: F401
    NotEqual,  # noqa: F401
    cmp,  # noqa: F401
    compare,  # noqa: F401
    eq,  # noqa: F401
    equal,  # noqa: F401
    greather_than,  # noqa: F401
    grether_than_or_equal,  # noqa: F401
    gt,  # noqa: F401
    gte,  # noqa: F401
    lower_than,  # noqa: F401
    lower_than_or_equal,  # noqa: F401
    lt,  # noqa: F401
    lte,  # noqa: F401
    ne,  # noqa: F401
    not_equal,  # noqa: F401
)
from monggregate.operators.objects import (
    MergeObjects,  # noqa: F401
    ObjectToArray,  # noqa: F401
    merge_objects,  # noqa: F401
    object_to_array,  # noqa: F401
)
from monggregate.operators.operator import Operator  # noqa: F401
from monggregate.operators.type_ import type_  # noqa: F401
