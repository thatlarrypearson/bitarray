# bitarray/tests/test_03_methods_to_from_list.py
#
# python -m pytest tests/test_03_methods_to_from_list.py
#
# Test coverage for methods:
# - from_list()
# - to_list()

import pytest
from bitarray import bitarray

def test_instantiation_bytearray():
    assert (
        bitarray(
            bitarray(
                bytearray.fromhex("FF0000000000000000000000")
            ).to_list()
        ).to_bytearray() ==
        bitarray(bytearray.fromhex("FF0000000000000000000000")).to_bytearray()
    )

    assert (
        bitarray([0,]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,0,]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,0,0,]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,0,0,0,]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,0,0,0,0,]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,0,0,0,0,0]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,0,0,0,0,0,0,]).to_list() == [0,0,0,0,0,0,0,0,]
    )
    assert (
        bitarray([0,0,0,0,0,0,0,0,0]).to_list() == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    )

    assert (
        len([]) == len(bitarray([]).to_list())
    )

    with pytest.raises(ValueError): #
        bitarray([0, 'A',])

    with pytest.raises(ValueError): #
        bitarray([0, -1,])

    with pytest.raises(ValueError): #
        bitarray([0, 52,])

    with pytest.raises(ValueError): #
        bitarray([0, 1, None])

