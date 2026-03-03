# bitarray/tests/test_01.py
#
# python -m pytest tests/test_01
#
# Test coverage for:
# - instantiation
# - to_<data-type>() methods

import pytest
from bitarray import bitarray

def test_instantiation_int():
    # 0xFF 00 00 00 00 00 00 00 00 00 00 00
    # 12 bytes vs 96 bits
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


