"""An example of a test module"""

from app.total_sum_module import join, total


def test_total_empty() -> None:
    """Total of empty list should be 0.0"""
    assert total([]) == 0.0


def test_total_single_item() -> None:
    """Total of a single item list should be the first item's value"""
    assert total([110.0]) == 110.0


def test_total_many_items() -> None:
    """Total of a list with many items should be their sum"""
    assert total([1.0, 2.0, 3.0]) == 6.0


def test_join_use_case() -> None:
    """Join of a list of integers with separator should be a string separated by delimeter"""
    assert join([1, 2, 3], ", ") == "1, 2, 3"


def test_join_edge_single_item() -> None:
    """Join of a single element should return a single string element without separator"""
    assert join([1], ", ") == "1"


def test_join_edge_empty_delimeter() -> None:
    """Join of a list of integers with empty list, should return a string of integers joined without delimeter"""
    assert join([1, 2, 3], "") == "123"