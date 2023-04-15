
from function import sum_of_price
import pytest


@pytest.mark.parametrize("orange, mango, watermelon, expected_result", [
    (5, 5, 5, 1025),
    (0, 0, 0, 0),
    (1, 0, 1, 125),
    (1.5, 2.5, 3, 462.5),
    (-1, -2, 5, "Not valid"),
    ("2", "a", 5, "input number"),
    (2, "", 0, "input number"),
])
def test_display_sum_price(orange, mango, watermelon, expected_result):
    actual_result = sum_of_price(orange, mango, watermelon)
    assert actual_result == expected_result
