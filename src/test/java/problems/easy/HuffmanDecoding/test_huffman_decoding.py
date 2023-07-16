# import heapq
# from src.main.java.problems.easy.HuffmanDecoding.huffman_decoding \
#     import MinHeapNode, calcFreq, decodeHuffmanData, huffmanCodes, minheap
# import pytest


test_data = [
    ("0000000000001100101010101011111111010101010", None, "AAAAAABCCCCCCDDEEEEE"),
    ("01110100011111000101101011101000111", None, "geeksforgeeks"),
]


"""
@pytest.mark.parametrize("binaryString,root,expected_result", test_data)
def test_huffman_decoding(binaryString: str,
root: MinHeapNode, expected_result: str):
    minheap = []
    heapq.heapify(minheap)
    cnt=0
    codes = {}
    freq = {}
    t = binaryString
    while(t>0):
        strr = input()
    encodedString = ""
    decodedString = ""
    calcFreq(strr, len(strr))
    #print(freq)
    huffmanCodes(len(strr))
    #print(codes)
    for i in strr:
        encodedString += codes[i]
    huffmanCodes(expected_result)
    assert expected_result == decodeHuffmanData(minheap[0][2], binaryString)
"""
