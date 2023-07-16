from src.main.java.problems.easy.HuffmanEncoding.huffman_encoding import (
    huffman_encoding,
)
from typing import List
import pytest


test_data = [
    ("abcdef", [5, 9, 12, 13, 16, 45], ["0", "100", "101", "1100", "1101", "111"])
]


@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("text,nodes,expected_result", test_data)
def test_huffman_encoding(text: str, nodes: List[int], expected_result: List[str]):
    assert expected_result == huffman_encoding(text, nodes)
