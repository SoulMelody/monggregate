"""Array Operators subpackage"""

from monggregate.operators.array.array_to_object import ArrayToObject, array_to_object  # noqa: F401, I001
from monggregate.operators.array.filter import Filter, filter  # pylint: disable=redefined-builtin  # noqa: F401
from monggregate.operators.array.first import First, first  # noqa: F401
from monggregate.operators.array.in_ import In, in_  # noqa: F401
from monggregate.operators.array.is_array import IsArray, is_array  # noqa: F401
from monggregate.operators.array.last import Last, last  # noqa: F401
from monggregate.operators.array.max_n import MaxN, max_n  # noqa: F401
from monggregate.operators.array.min_n import MinN, min_n  # noqa: F401
from monggregate.operators.array.size import Size, size  # noqa: F401
from monggregate.operators.array.sort_array import SortArray, sort_array  # noqa: F401

# TODO:
# * $arrayElemAt
# * $concatArrays
# * $indexOfArray
# * $map
# * $maxN
# * $minN
# * $objectToArray
# * $range
# * $reduce
# * $reverseArray
# * $slice
# * $zip
