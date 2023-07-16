from src.main.java.problems.easy.WaveArray.wave_array import convertToWave
from typing import List
import pytest


test_data = [
    (5, [1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
    (6, [2, 4, 7, 8, 9, 10], [4, 2, 8, 7, 10, 9]),
    (6, [6907, 7808, 8551, 8683, 9205, 9980], [7808, 6907, 8683, 8551, 9980, 9205]),
]


@pytest.mark.parametrize("number,input_array,expected_result", test_data)
def test_wave_array(number: int, input_array: List[int], expected_result: List[int]):
    convertToWave(input_array, number)
    assert expected_result == input_array
