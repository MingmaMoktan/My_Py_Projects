import pytest
from src.characters import CharCreator
from src.numerical import add, random_number

def test_adding_numeric_character_to_creator():
    creator = CharCreator()
    numerical_character = str(add(1,5))
    creator.add_char(numerical_character)
    assert creator.characters == ['6']

def test_adding_random_numeric_character_to_creator():
    creator = CharCreator()
    random_numerical_character = str(random_number(1,5))
    creator.add_char(random_numerical_character)
    assert creator.characters == [random_numerical_character]