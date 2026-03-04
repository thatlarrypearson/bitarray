# bitarray/tests/test_04_slicing.py
#
# python -m pytest tests/test_04_slicing.py
#
# Test coverage for slicing


import pytest
from bitarray import bitarray

def test_slicing():
    assert (
        # reverse bit order
        bitarray([0, 0, 0, 0, 1, 1, 1, 1,])[::-1].to_list() == [1, 1, 1, 1, 0, 0, 0, 0,]
    )

    assert (
        # get the first 4 bits
        bitarray([0, 0, 0, 0, 1, 1, 1, 1,])[:4].to_list() == [0, 0, 0, 0, 0, 0, 0, 0,]
    )

    assert (
        # get the last 4 bits
        bitarray([0, 0, 0, 0, 1, 1, 1, 1,])[4:].to_list() == [1, 1, 1, 1, 0, 0, 0, 0,]
    )

    assert (
        # get the first bit
        bitarray([0, 0, 0, 0, 1, 1, 1, 1,])[0].to_list() == [0, 0, 0, 0, 0, 0, 0, 0,]
    )

    assert (
        # get the last bit
        bitarray([0, 0, 0, 0, 1, 1, 1, 1,])[-1].to_list() == [1, 0, 0, 0, 0, 0, 0, 0,]
    )

    assert (
        # get bits 4 and 5
        bitarray([0, 0, 0, 0, 1, 1, 1, 1,])[3:5].to_list() == [0, 1, 0, 0, 0, 0, 0, 0,]
    )
