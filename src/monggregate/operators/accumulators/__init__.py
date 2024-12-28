"""Accumulator Operators Subpackage"""

from monggregate.operators.accumulators.avg import Average, Avg, average, avg  # noqa: F401
from monggregate.operators.accumulators.count import Count, count  # noqa: F401
from monggregate.operators.accumulators.first import First, first  # noqa: F401
from monggregate.operators.accumulators.last import Last, last  # noqa: F401
from monggregate.operators.accumulators.max import Max, max  # noqa: F401
from monggregate.operators.accumulators.min import Min, min  # noqa: F401
from monggregate.operators.accumulators.push import Push, push  # noqa: F401
from monggregate.operators.accumulators.sum import Sum, sum  # noqa: F401

# TODO  :
# * $accumulator
# * $addToSet
# * $bottom
# * $bottomN
# * $firstN
# * $lastN
# * $maxN
# * $mergeObjects
# * $stdDedPop
# * $stdDevSamp
# * $top
# * $topN
