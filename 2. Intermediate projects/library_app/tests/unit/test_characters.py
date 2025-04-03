import pytest
from src.characters import CharCreator

@pytest.fixture
def creator():
    '''
    Create a new CharCreator before each test.
    This is automatically called and passed as an argument for each test inside this file.
    '''
    return CharCreator()

# add_char()

def test_adding_char(creator):
    creator.add_char('a')
    assert creator.characters == ['a']

def test_adding_chars(creator):
    creator.add_char('a')
    creator.add_char('b')
    assert creator.characters == ['a', 'b']

def test_adding_numbers(creator):
    creator.add_char('1')
    creator.add_char('a')
    assert creator.characters == ['1', 'a']

# CharCreator.remove_char()

def test_removing_char(creator):
    creator.add_char('a')
    creator.add_char('b')
    creator.add_char('c')
    creator.remove_char()
    assert creator.characters == ['a', 'b']