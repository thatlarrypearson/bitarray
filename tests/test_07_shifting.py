# bitarray/tests/test_07_shifting.py
#
# python -m pytest tests/test_07_shifting.py
#
# Test coverage for bit shift operators >>, <<

import pytest
from bitarray import bitarray

def test_shifting():
    # don't be confused about the direction of the bit shifting.
    # the bit shift operators are constructed using a big-endian
    # view of the underlying storage which in bitarray's case
    # is organized as a little-endian list.
    # In the big-endian world left-shift (<<) operator makes the integer
    # larger by moving the bits towards higher values while the
    # right-shift (>>) operator makes the integer smaller by moving
    # the bits towards lower values.  Bit shifting past a zero (0)
    # value bit makes the bits disappear.
    assert (bitarray(0x000001) << 8) == 256

    # when right shifting past the least significant
    # bit, the bits to the right of the least significant
    # bit are dropped.
    assert (bitarray(256) >> 8) == 1

    assert (bitarray(256) >> 9) == 0

    assert (bitarray(1) << 100) == 2**100

    # when trying to preserve the original number of bytes,
    # left shifting past the original number of bytes
    # just keeps automatically increasing the number of bytes
    # in the result.  when the desire is to mimic C type
    # unsigned int, the bitarray needs to be truncated to
    # match the original size as shown below.
    assert (bitarray(1) << 100)[:len(bitarray(1))].to_int() == 0

    with pytest.raises(TypeError):
        (bitarray(1) << bitarray(100)) == 2**100

    with pytest.raises(TypeError):
        (bitarray(0x000001) << bitarray(8)) == 256
