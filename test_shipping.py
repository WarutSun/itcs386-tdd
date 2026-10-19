import pytest
from shipping import shipping_fee


# Rule 1: weight must be > 0
@pytest.mark.parametrize("weight", [0, -1])
def test_invalid_weight_is_rejected(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)


@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),    # Rule 2: inside block
    (1, 40),      # Rule 2: boundary, "up to 1 kg"
    (3, 60),      # Rule 3: inside block
    (5, 60),      # Rule 3: boundary, "up to 5 kg"
    (5.2, 70),    # Rule 4: example from the docstring
    (6, 70),      # Rule 4: exactly 1 kg above 5
    (7.5, 90),    # Rule 4: 2.5 kg above 5, so 3 started kg
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected