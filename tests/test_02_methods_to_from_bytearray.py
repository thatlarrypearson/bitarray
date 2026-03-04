# bitarray/tests/test_02_methods_to_from_bytearray.py
#
# python -m pytest tests/test_02_methods_to_from_bytearray.py
#
# Test coverage for methods:
# - from_bytearray()
# - to_bytearray()

import pytest
from bitarray import bitarray

def test_instantiation_bytearray():
    assert (
        bytearray.fromhex(         "FF0000000000000000000000") ==
        bitarray(bytearray.fromhex("FF0000000000000000000000")).to_bytearray()
    )

    assert (
        bytearray.fromhex(         "F0000000000000000000000F") ==
        bitarray(bytearray.fromhex("F0000000000000000000000F")).to_bytearray()
    )

    assert (
        bytearray.fromhex("F00000000000000F") ==
        bitarray(bytearray.fromhex("F00000000000000F")).to_bytearray()
    )

    assert (
        bytearray.fromhex("FF00000000000000") ==
        bitarray(bytearray.fromhex("FF00000000000000")).to_bytearray()
    )

    assert (
        bytearray.fromhex("F000000000000F") ==
        bitarray(bytearray.fromhex("F000000000000F")).to_bytearray()
    )

    assert (
        bytearray.fromhex("FF000000000000") ==
        bitarray(bytearray.fromhex("FF000000000000")).to_bytearray()
    )

    assert (
        bytearray.fromhex("00") ==
        bitarray(bytearray.fromhex("00")).to_bytearray()
    )

    assert (
        bytearray.fromhex("000F") ==
        bitarray(bytearray.fromhex("000F")).to_bytearray()
    )

    assert (
        bytearray.fromhex("0000") ==
        bitarray(bytearray.fromhex("0000")).to_bytearray()
    )

    assert (
        bytearray.fromhex("00") ==
        bitarray(bytearray.fromhex("00")).to_bytearray()
    )

    assert (
        len(bytearray()) == len(bitarray(None).to_bytearray())
    )

    with pytest.raises(ValueError): #
        bitarray("None").to_bytearray()

