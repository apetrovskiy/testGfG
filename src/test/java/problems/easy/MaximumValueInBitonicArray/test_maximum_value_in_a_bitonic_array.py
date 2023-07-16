from src.main.java.problems.easy.MaximumValueInBitonicArray.maximum_value_in_a_bitonic_array import (
    Solution,
)
from typing import List
import pytest


test_data = [(9, [1, 15, 25, 45, 42, 21, 17, 12, 11], 45), (5, [1, 45, 47, 50, 5], 50)]


@pytest.mark.parametrize("number,input_data,expected_result", test_data)
def test_maximum_value_in_a_bitonic_array(
    number: int, input_data: List[int], expected_result: int
):
    assert expected_result == Solution().findMaximum(input_data, number)
