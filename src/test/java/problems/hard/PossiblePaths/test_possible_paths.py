from src.main.java.problems.hard.PossiblePaths.possible_paths import Solution
from typing import List
import pytest


test_data = [
    # TODO
    # (7, [[1, 2, 3], [2, 3, 1], [2, 4, 9], [3, 6, 7],
    #    [3, 5, 8], [5, 7, 4]], 3, [1, 3, 5], [1, 3, 4]),
    (3, [[1, 2, 1], [2, 3, 4]], 1, [3], [1])
]


@pytest.mark.parametrize("n,edges,q,queries,expected_result", test_data)
def test_possible_paths(
    n: int,
    edges: List[List[int]],
    q: int,
    queries: List[int],
    expected_result: List[int],
):
    assert expected_result == Solution().maximumWeight(n, edges, q, queries)
