# bitarray/tests/test_05_add_eq.py
#
# python -m pytest tests/test_05_add_eq.py
#
# Test coverage for __add__, __radd__, __eq__, __req__

import pytest
from bitarray import bitarray

def test_add_eq():
    assert 0xFF0000000000000000000000 == bitarray(0xFF0000000000000000000000).to_int()
    assert 0xF0000000000000000000000F == bitarray(0xF0000000000000000000000F).to_int()
    assert 0xF00000000000000F == bitarray(0xF00000000000000F).to_int()
    assert 0xFF00000000000000 == bitarray(0xFF00000000000000).to_int()
    assert 0xF000000000000F == bitarray(0xF000000000000F).to_int()
    assert 0xFF000000000000 == bitarray(0xFF000000000000).to_int()
    assert 0x00 == bitarray(0x00).to_int()
    assert 0x000F == bitarray(0x000F).to_int()
    assert 0x0000 == bitarray(0x0000).to_int()
    assert 0x00 == bitarray(0x00).to_int()

    with pytest.raises(ValueError): #
        bitarray(None).to_int()

    with pytest.raises(ValueError):
        bitarray(None) == bitarray(None)

    with pytest.raises(ValueError):
        bitarray(None) == bitarray(255)

    with pytest.raises(ValueError):
        bitarray(255) == bitarray(None)

    assert (
        (
            bitarray(bytearray.fromhex("FF0000000000000000000000")) + 
            bitarray(bytearray.fromhex("0000000000000000000000FF"))
        ) == bitarray(bytearray.fromhex("FF00000000000000000000FF"))
    )

    assert (
        (
            bytearray.fromhex(                     "00000000000F") +
            bitarray(bytearray.fromhex("F00000000000000000000000"))
        ) == bitarray(
            bytearray.fromhex(         "F0000000000000000000000F")
        )
    )

    assert (
        (
            bitarray(bytearray.fromhex("F00000000000000000000000")) +
            bytearray.fromhex(                     "00000000000F")
        ) == bitarray(
            bytearray.fromhex(         "F0000000000000000000000F")
        )
    )

    assert (
        (
            bytearray.fromhex(                     "00000000000F") +
            bitarray(bytearray.fromhex("F00000000000000000000000"))
        ) == bytearray.fromhex(        "F0000000000000000000000F")
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_bytearray() +
            bitarray(bytearray.fromhex(  "0000000000000000000000FF"))
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF"))
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "0000000000000000000000FF")) +
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_bytearray()
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF"))
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_int() +
            bitarray(bytearray.fromhex(  "0000000000000000000000FF"))
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF"))
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "0000000000000000000000FF")) +
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_int()
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF"))
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_bytearray() +
            bitarray(bytearray.fromhex(  "0000000000000000000000FF"))
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF")).to_bytearray()
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "0000000000000000000000FF")) +
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_bytearray()
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF")).to_bytearray()
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_int() +
            bitarray(bytearray.fromhex(  "0000000000000000000000FF"))
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF")).to_int()
    )

    assert (
        (
            bitarray(bytearray.fromhex(  "0000000000000000000000FF")) +
            bitarray(bytearray.fromhex(  "FF0000000000000000000000")).to_int()
        ) ==  bitarray(bytearray.fromhex("FF00000000000000000000FF")).to_int()
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")) !=
        bitarray(bytearray.fromhex("FF0000000000000000000000"))
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")) !=
        bitarray(bytearray.fromhex("FF0000000000000000000000")).to_int()
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")) !=
        bitarray(bytearray.fromhex("FF0000000000000000000000")).to_int()
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")) !=
        bitarray(bytearray.fromhex("FF0000000000000000000000")).to_bytearray()
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")) !=
        bitarray(bytearray.fromhex("FF0000000000000000000000")).to_bytearray()
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")).to_int() !=
        bitarray(bytearray.fromhex("FF0000000000000000000000"))
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")).to_int() !=
        bitarray(bytearray.fromhex("FF0000000000000000000000"))
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")).to_bytearray() !=
        bitarray(bytearray.fromhex("FF0000000000000000000000"))
    )

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000FF")).to_bytearray() !=
        bitarray(bytearray.fromhex("FF0000000000000000000000"))
    )
