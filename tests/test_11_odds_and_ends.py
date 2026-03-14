# bitarray/tests/test_11_odds_and_ends.py
#
# python -m pytest tests/test_11_odds_and_ends.py
#
# Test coverage for other stuff
#   - __repr__(self)
#   - __str__(self)

import pytest
from bitarray import bitarray

def test_odds_and_ends():

    assert isinstance(str(bitarray(0xFFFF)), str)

    assert isinstance(str(bitarray(0xFFFF).__repr__()), str)
