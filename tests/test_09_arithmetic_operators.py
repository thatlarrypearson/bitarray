# bitarray/tests/test_09_arithmetic_operators.py
#
# python -m pytest tests/test_09_arithmetic_operators.py
#
# Test coverage for arithmetic operators
#   - + add (__add__/__radd__) 
#   - - subtract  (__sub__/__rsub__)
#   - - negate unary operator (__neg__)
#   - * multiply (__mul__/__rmul__)
#   - / true division resulting in floating point number (__truediv__/__rtruediv__)
#   - // floor division (__floordiv__/__rfloordiv__)
#   - % integer division remainder (__mod__/__rmod__)

import pytest
from bitarray import bitarray

def test_arithmetic_operators():

    # negation
    with pytest.raises(NotImplementedError):
        - bitarray(0x000001)

    # negative integers
    with pytest.raises(ValueError):
        -9 * bitarray(0x1234)

    with pytest.raises(ValueError):
        bitarray(0x1234) * -9

    with pytest.raises(ValueError):
        -4096 + bitarray(2048)

    with pytest.raises(ValueError):
        bitarray(2048) + -4096

    with pytest.raises(ValueError):
        bitarray(2048) - 4096

    # unsupported types
    with pytest.raises(NotImplementedError):
        9.9 + bitarray(0x1234)

    with pytest.raises(NotImplementedError):
        9.9 - bitarray(0x1234)

    with pytest.raises(NotImplementedError):
        9.9 * bitarray(0x1234)

    with pytest.raises(NotImplementedError):
        9.9 / bitarray(0x1234)

    with pytest.raises(NotImplementedError):
        9.9 // bitarray(0x1234)

    with pytest.raises(NotImplementedError):
        9.9 % bitarray(0x1234)

    # unsupported types
    with pytest.raises(NotImplementedError):
        bitarray(0x1234) + 9.9

    with pytest.raises(NotImplementedError):
        bitarray(0x1234) - 9.9

    with pytest.raises(NotImplementedError):
        bitarray(0x1234) * 9.9

    with pytest.raises(NotImplementedError):
        bitarray(0x1234) / 9.9

    with pytest.raises(NotImplementedError):
        bitarray(0x1234) // 9.9

    with pytest.raises(NotImplementedError):
        bitarray(0x1234) % 9.9

    # sourcery skip: simplify-numeric-comparison
    assert bitarray(2048) - 1024 == 1024

    assert bitarray(2048) + 2048 == 4096

    assert -1024 + bitarray(2048) == 1024

    assert 2048 + bitarray(2048) == 4096

    assert 2048 + bitarray(2048) == 4096

    assert 2048 - bitarray(2048) == 0

    assert 4096 - bitarray(2048) == 2048

    assert 2 * bitarray(2) == 4

    assert bitarray(2) * 2 == 4

    assert 2 / bitarray(4) == 0.5

    assert 4 / bitarray(2) == 2

    assert bitarray(2) / 4 == 0.5

    assert bitarray(4) / 2 == 2.0

    assert bitarray(4) % 2 == 0

    assert bitarray(2) % 4 == 2

    assert 4 / bitarray(2) == 2.0

    assert 2 / bitarray(4) == 0.5

    assert 2 // bitarray(4) == 0

    assert 4 // bitarray(2) == 2

    assert bitarray(2) // 4 == 0

    assert bitarray(4) // 2 == 2

    assert bitarray(2)**1 == 2

    assert bitarray(2)**bitarray(1) == 2

    assert bitarray(1)**10 == 1

    assert 10**bitarray(1) == 1

