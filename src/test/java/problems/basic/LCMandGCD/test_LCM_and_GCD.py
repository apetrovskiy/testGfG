from typing import List
from src.main.java.problems.basic.LCMandGCD.LCM_and_GCD import Solution
import pytest


test_data = [(5, 10, [10, 5]), (14, 8, [56, 2])]


@pytest.mark.parametrize("a,b,expected_result", test_data)
def test_LCM_and_GCD(a: int, b: int, expected_result: List[int]):
    assert expected_result == Solution().lcmAndGcd(a, b)
