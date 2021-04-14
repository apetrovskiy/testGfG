from src.main.java.problems.easy.FrequenciesOfLimitedRangeArrayElements.\
    frequencies_of_limited_range_array_elements import frequencycount
from typing import List
import pytest

test_data = [
    (5, [2, 3, 2, 3, 5], [0, 2, 2, 0, 1]),
    (4, [3, 3, 3, 3], [0, 0, 4, 0])
]


@pytest.mark.parametrize("number,input_data,expected_result", test_data)
def test_frequencies_of_limited_range_array_elements(
        number: int, input_data: List[int], expected_result: List[int]):
    frequencycount(input_data, number)
    assert expected_result == input_data
