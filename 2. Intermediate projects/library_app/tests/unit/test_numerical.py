import pytest
from unittest.mock import patch
from src.numerical import add, random_number

## add()

def test_add_basic():
    assert add(2,5) == 7
    assert add(2,8) == 10
    assert add(1,1) == 2

def test_add_large_numbers():
    assert add(1500,1500) == 3000
    assert add(162050,152723) == 314773

def test_add_negative_numbers():
    assert add(-5,100) == 95
    assert add(100,-50) == 50

def test_add_zero():
    assert add(0,0) == 0

def test_add_float():
    assert add(0.5, 0.5) == 1

def test_add_type_check():
    with pytest.raises(TypeError):
        sum("a", "b")

# random_number()

def test_random_number():
    random = random_number(10,20)
    if random >= 10 and random <= 20:
        assert True

def test_fifty_random_numbers():
    for i in range(50):
        assert random_number(i, i) == i

def test_random_number_calls_randint():
    min_val = 1
    max_val = 10
    with patch('random.randint') as mock_randint:
        random_number(min_val, max_val)
        mock_randint.assert_called_once_with(min_val, max_val)

def test_random_number_returns_fixed_value():
    # The value you want random.randint to always return
    fixed_value = 5
    with patch('random.randint', return_value=fixed_value) as mock_randint:
        assert random_number(1, 10) == fixed_value
        # Verifies random.randint was called with the correct arguments
        mock_randint.assert_called_with(1, 10)