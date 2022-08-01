"""An example Python module"""

from typing import List


def total(xs: List[float]) -> float:
    """Total returns the sum of xs"""
    result: float = 0.0
    # For each x float in xs, add it to result
    for x in xs:
        result += x
    return result


def join(xs: List[int], delimeter: str) -> str:
    """Produce a string where subsequent items are separated by delimeter"""
    return delimeter.join([str(x) for x in xs])