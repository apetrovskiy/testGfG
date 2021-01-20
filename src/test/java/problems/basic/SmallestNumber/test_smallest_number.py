from src.main.java.problems.basic.SmallestNumber.smallest_number import Solution
import pytest


test_data = [
    (9, 2, 18),
    (20, 3, 299),
    (10, 1, -1),
    (6, 6, 100005)
]


@pytest.mark.parametrize("sum_of_digits,number_of_digits,expected_result", test_data)
def test_smallest_number(sum_of_digits: int, number_of_digits: int, expected_result: int):
    assert expected_result == Solution().smallestNumber(
        sum_of_digits, number_of_digits)
