import pytest
from voorhees import Voorhees

@pytest.mark.test_id(1)
def test_simple_copy():
    original = {'what': 3}
    result = Voorhees(original).copy()
    assert original == result

@pytest.mark.test_id(2)
def test_simple_list_copy():
    original = {'what': [1,2,3]}
    result = Voorhees(original).copy()
    assert original == result

@pytest.mark.test_id(3)
def test_simple_dict_copy():
    original = {'what': {'value': 3}}
    result = Voorhees(original).copy()
    assert original == result

@pytest.mark.test_id(4)
def test_multiple_string_entries():
    original = {'what': 'thing', 'another': 'something'}
    result = Voorhees(original).copy()
    assert original == result

@pytest.mark.test_id(5)
def test_boolean():
    original = {'what': False}
    result = Voorhees(original)
    x = result.copy()
    print(x, original)
    assert original == x
    
@pytest.mark.test_id(6)
def test_float():
    original = {'what': 5.67}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(7)
def test_multiple_floats():
    original = {'what': 3.3, 'another': 5.5}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(8)
def test_multiple_ints():
    original = {'what': 3, 'another': 4}
    result = Voorhees(original)
    assert original == result.copy()
    
@pytest.mark.test_id(9)
def test_multiple_dicts():
    original = {'1': {'a': 3, 'b': 4}, '2': {'c': 5, 'd': 6}}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(10)
def test_multiple_bools():
    original = {'1': True, '2': False}
    result = Voorhees(original)
    assert original == result.copy()

