"""An example of a test module"""

from app.total_sum_module import total


def test_total_empty() -> None:
    assert total([]) == 0.0