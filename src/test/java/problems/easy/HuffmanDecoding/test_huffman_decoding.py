from src.main.java.problems.easy.HuffmanDecoding.huffman_decoding import MinHeapNode, decodeHuffmanData
import pytest


test_data = [
    ("0000000000001100101010101011111111010101010", None, "AAAAAABCCCCCCDDEEEEE"),
    ("01110100011111000101101011101000111", None, "geeksforgeeks")
]


@pytest.mark.parametrize("binaryString,root,expected_result", test_data)
def test_huffman_decoding(binaryString: str, root: MinHeapNode, expected_result: str):
    assert expected_result == decodeHuffmanData(root, binaryString)
