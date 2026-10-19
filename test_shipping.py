import pytest
from shipping import shipping_fee


# Rule 1: weight must be > 0
@pytest.mark.parametrize("weight", [0, -1])
def test_invalid_weight_is_rejected(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)


@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),   # Rule 2: inside the block
    # เพิ่มแถวของคุณเอง ครอบคลุมกฎ 2, 3, 4
    # อย่าลืมค่าที่ขอบ: 1 kg, 5 kg และค่าที่เกิน 5 เล็กน้อย เช่น 5.2
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected