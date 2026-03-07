# bitarray/tests/test_06_comparison.py
#
# python -m pytest tests/test_06_comparison.py
#
# Test coverage for comparison operators >, >=, <, <=

import pytest
from bitarray import bitarray

def test_comparison():  # sourcery skip: de-morgan, extract-duplicate-method, flip-comparison
    assert          0xF0000000000000000000000F  >= bitarray(0xF0000000000000000000000F)
    assert          0xF0000000000000000000000F  > bitarray( 0xF00000000000000000000000)
    assert bitarray(0xF0000000000000000000000F) >= bitarray(0xF0000000000000000000000F)
    assert bitarray(0xF0000000000000000000000F) > bitarray( 0xF00000000000000000000000)
    assert bitarray(0xF0000000000000000000000F) >=          0xF0000000000000000000000F
    assert bitarray(0xF0000000000000000000000F) >           0xF00000000000000000000000

    assert          0xF0000000000000000000000F  <= bitarray(0xFF000000000000000000000F)
    assert          0xF0000000000000000000000F  < bitarray( 0xF0F000000000000000000000)
    assert bitarray(0xF0000000000000000000000F) <= bitarray(0xF0000000000000000000000F)
    assert bitarray(0xF0000000000000000000000F) < bitarray( 0xF000F0000000000000000000)
    assert bitarray(0xF0000000000000000000000F) <=          0xF0000000000000000000000F
    assert bitarray(0xF0000000000000000000000F) <           0xF00000F00000000000000000

    with pytest.raises(ValueError):
        bitarray(255) < bitarray(None)

    with pytest.raises(ValueError):
        bitarray(255) > bitarray(None)

    with pytest.raises(ValueError):
        bitarray(255) >= bitarray(None)

    with pytest.raises(ValueError):
        bitarray(255) <= bitarray(None)

    with pytest.raises(ValueError):
        bitarray(None) < bitarray(None)

    with pytest.raises(ValueError):
        bitarray(None) > bitarray(None)

    with pytest.raises(ValueError):
        bitarray(None) >= bitarray(None)

    with pytest.raises(ValueError):
        bitarray(None) <= bitarray(None)

    with pytest.raises(ValueError):
        bitarray(None) < bitarray(255)

    with pytest.raises(ValueError):
        bitarray(None) > bitarray(255)

    with pytest.raises(ValueError):
        bitarray(None) >= bitarray(255)

    with pytest.raises(ValueError):
        bitarray(None) <= bitarray(255)

    with pytest.raises(ValueError):
        bitarray(None) != bitarray(None)

    with pytest.raises(ValueError):
        bitarray(255) != bitarray(None)

    with pytest.raises(ValueError):
        bitarray(None) != bitarray(255)

    # looking for not True
    assert not (         0xF0000000000000000000000F  >= bitarray(0xFF000000000000000000000F))
    assert not (         0xF0000000000000000000000F  > bitarray( 0xFF0000000000000000000000))
    assert not (bitarray(0xF0000000000000000000000F) >= bitarray(0xFF000000000000000000000F))
    assert not (bitarray(0xF0000000000000000000000F) > bitarray( 0xFF0000000000000000000000))
    assert not (bitarray(0xF0000000000000000000000F) >=          0xFF000000000000000000000F)
    assert not (bitarray(0xF0000000000000000000000F) >           0xFF0000000000000000000000)

    assert not (         0xFF000000000000000000000F  <= bitarray(0xF0000000000000000000000F))
    assert not (         0xFF000000000000000000000F  < bitarray( 0xF0F000000000000000000000))
    assert not (bitarray(0xFF000000000000000000000F) <= bitarray(0xF0000000000000000000000F))
    assert not (bitarray(0xFF000000000000000000000F) < bitarray( 0xF000F0000000000000000000))
    assert not (bitarray(0xFF000000000000000000000F) <=          0xF0000000000000000000000F)
    assert not (bitarray(0xFF000000000000000000000F) <           0xF00000F00000000000000000)

    assert not (bitarray(0xFF000000000000000000000F) !=          0xFF000000000000000000000F)
    assert not (         0xFF000000000000000000000F  != bitarray(0xFF000000000000000000000F))
