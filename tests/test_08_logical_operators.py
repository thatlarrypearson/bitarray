# bitarray/tests/test_08_logical_operators.py
#
# python -m pytest tests/test_08_logical_operators.py
#
# Test coverage for logical operators
#   - & and (__and__/__rand__) 
#   - | or  (__or__/__ror__)
#   - ^ xor (__xor__/__rxor__)
#   - ~ not (__invert__)

import pytest
from bitarray import bitarray

def test_logical_operators():
    assert bitarray(2**3) & bitarray(2**1) == 0
    assert bitarray(2**3 + 2**1) & bitarray(2**1) == 2**1
    assert bitarray(2**10 + 2**5) & bitarray(2**10) == 2**10

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) &
        bitarray(bytearray.fromhex("F000000000000000000000"))
    ) == 0xF000000000000000000000

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) &
        0xF000000000000000000000
    ) == 0xF000000000000000000000

    assert (
        bytearray.fromhex("F000000000000000000001") &
        bitarray(bytearray.fromhex("F000000000000000000000"))
    ) == 0xF000000000000000000000

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) &
        bytearray.fromhex("F000000000000000000000")
    ) == 0xF000000000000000000000



    assert bitarray(2**3) | bitarray(2**1) == 2**3 + 2**1
    assert bitarray(2**3 + 2**1) | bitarray(2**1) == 2**3 + 2**1
    assert bitarray(2**10 + 2**5) | bitarray(2**10) == 2**10 + 2**5

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) |
        bitarray(bytearray.fromhex("F000000000000000000000"))
    ) == 0xF000000000000000000001

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) |
                                  0xF000000000000000000000
    ) ==                          0xF000000000000000000001

    assert (
        bytearray.fromhex(         "F000000000000000000001") |
        bitarray(bytearray.fromhex("F000000000000000000000"))
    ) ==                          0xF000000000000000000001

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) |
        bytearray.fromhex("F000000000000000000000")
    ) == 0xF000000000000000000001


    assert bitarray(2**3) ^ bitarray(2**1) == 2**3 + 2**1
    assert bitarray(2**3 + 2**1) ^ bitarray(2**1) == 2**3
    assert bitarray(2**10 + 2**5) ^ bitarray(2**10) == 2**5

    assert (
        bitarray(bytearray.fromhex("0000000000000000000000")) ^
        bitarray(bytearray.fromhex("F000000000000000000001"))
    ) == 0xF000000000000000000001

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) ^
                                  0x0000000000000000000000
    ) ==                          0xF000000000000000000001

    assert (
        bytearray.fromhex(         "F000000000000000000001") ^
        bitarray(bytearray.fromhex("F000000000000000000000"))
    ) ==                          0x0000000000000000000001

    assert (
        bitarray(bytearray.fromhex("F000000000000000000001")) ^
        bytearray.fromhex(         "0000000000000000000000")
    ) ==                          0xF000000000000000000001

    assert ~bitarray(0x0F, max_int_bits=8) == 0xF0

    assert ~bitarray(0x00FF, max_int_bits=16) == 0xFF00