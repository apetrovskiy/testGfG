from src.main.java.problems.medium.MinimumSpanningTree.minimum_spanning_tree import Solution
import pytest


test_data = [
    # dubious data
    (2, [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]], 0)
]


@pytest.mark.parametrize("vertices,matrix,expected_result", test_data)
def test_minimum_spanning_tree(vertices, matrix, expected_result):
    assert expected_result == Solution().spanningTree(vertices, matrix)


'''
Input:
4 5
0 1 6
0 2 3
1 3 9
0 3 1
2 3 6

Its Correct output is:
10

And Your Code's output is:
3
'''
