# bitarray/tests/test_10_list_operations.py
#
# python -m pytest tests/test_10_list_operations.py
#
# Test coverage for list operations
#   - __setitem__(self, key, value) - in-place changing value
#   - __delitem__(self, key) - in-place deleting
#   - extend(iterable) - in-place extending
#   - clear() - in-place clearing
#   - insert(index, element) - in place insert
#   - append(element) - in-place append
#   - reverse() - in-place reversal of elements
#   - reversed() - returns a reverse iterator - use list(thing.reversed()) to get to reversed list

import pytest
from bitarray import bitarray

def test_list_operations():
    b = bitarray(0xFFFFFFFF, max_int_bits=32)
    b[:8] = [0, 0, 0, 0, 0, 0, 0, 0, ]
    assert b == bitarray(0xFFFFFF00, max_int_bits=32)

    b = bitarray(0xFFFFFFFF, max_int_bits=32)
    b[24:] = [0, 0, 0, 0, 0, 0, 0, 0, ]
    assert b == bitarray(0x00FFFFFF, max_int_bits=32)

    b = bitarray(0xFF, max_int_bits=8)
    b[-1] = 0
    assert b == 255 - 2**7

    b = bitarray(0xFF, max_int_bits=8)
    del b[6]
    assert b == 255 - 2**7

    b = bitarray(0xFFFF, max_int_bits=16)
    del b[:4]
    assert b == 0x0FFF

#   - extend(iterable) - in-place extending
    b = bitarray(0xFF, max_int_bits=8)
    b.extend([1 for _ in range(8)])
    assert b == 0xFFFF

#   - clear() - in-place clearing
    b = bitarray(0xFFFF)
    b.clear()
    assert len(b) == 0

#   - insert(index, element) - in place insert
    b = bitarray(0xFFFF)
    b.insert(0, 1)
    assert b == (0xFFFF * 2) + 1

    b = bitarray(0x00, max_int_bits=8)
    b.insert(0, bytearray.fromhex("FF"))
    assert len(b) == 8
    assert b.to_int() == 255

    b = bitarray(0x00, max_int_bits=8)
    b.insert(0, [1, 1, 1, 1, 1, 1, 1, 1, ])
    assert len(b) == 8
    assert b.to_int() == 255

    with pytest.raises(ValueError):
        b = bitarray(0x00, max_int_bits=8)
        b.insert(0, [1, 1, 1, 1, 5, 1, 1, 1, ])

    b = bitarray(0x00, max_int_bits=8)
    b.insert(0, bitarray(0xFF, max_int_bits=8))
    assert len(b) == 8
    assert b.to_int() == 255

    # now supports bitarray, bytearray, int
    # with pytest.raises(TypeError):
    #     bitarray(0xFFFF).insert(0, bytearray.fromhex("FFFF"))

    with pytest.raises(ValueError):
        bitarray(0XFFFF).insert(0, 3)

#   - append(element) - in-place append
    b = bitarray(0xFF, max_int_bits=8)
    b.append(1)
    assert b == 255 + 256

    with pytest.raises(ValueError):
        b.append(2)

    with pytest.raises(TypeError):
        b.append(3.14151)

    b = bitarray(0xFF, max_int_bits=8)
    b.append(bitarray(0xFF, max_int_bits=8))
    assert b == 0xFFFF

    with pytest.raises(TypeError):
        b.append("ABCD")

#   - reverse() - in-place reversal of elements
    b = bitarray(0x0F, max_int_bits=8)
    b.reverse()
    assert b == 0xF0
    b.reverse()
    assert b == 0x0F

#   - reversed() - returns a reverse iterator - use list(thing.reversed()) to get to reversed list
    b = bitarray(0x0F, max_int_bits=8)
    c = b.reversed()
    assert b == 0x0F and c == 0xF0
    d = c.reversed()
    assert c == 0xF0 and d == 0x0F
