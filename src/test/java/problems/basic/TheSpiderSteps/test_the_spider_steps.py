from src.main.java.problems.basic.TheSpiderSteps.the_spider_steps import Solution
import pytest


test_data = [
    (200, 50, 1, 5),
    (100, 5, 3, 49),
    (10, 4, 1, 4),
    (500, 20, 15, 98),
    (25, 26, 24, 1)
]


@pytest.mark.parametrize("h,u,d,expected_result", test_data)
def test_the_spider_steps(h: int, u: int, d: int, expected_result: int):
    assert expected_result == Solution().minStep(h, u, d)
