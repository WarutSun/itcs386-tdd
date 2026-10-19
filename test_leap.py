import pytest
from leap import is_leap


@pytest.mark.parametrize("year, expected", [
    (2000, True),    # divisible by 400
    (1900, False),   # divisible by 100 but not by 400
    (2024, True),    # divisible by 4 but not by 100
    (2023, False),   # not divisible by 4
    (1600, True),    # divisible by 400 (another century year)
    (2100, False),   # divisible by 100 but not by 400
])
def test_is_leap(year, expected):
    assert is_leap(year) == expected
    
def test_year_zero_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(0)
        
def test_negative_year_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(-5)