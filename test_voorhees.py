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

@pytest.mark.test_id(11)
def test_nested_dir():
    original = {'1': {'a': {'b': 3.14159}}}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(12)
def test_list_of_dicts():
    original = {'something': [{'a': 'c', 'b': 'd'}, {'c': 3}, {'d': 4}]}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(13)
def test_list_of_lists_of_ints():
    original = {'something': [[1,2,3,4], [5,6,7,8]]}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(14)
def test_negative_ints():
    original = {'what': -13}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(15)
def test_negative_floats():
    original = {'what': -5.67}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(16)
def test_list_of_lists_of_ints():
    original = {'something': [['a', 'b'], ['d', 'e', 'f']]}
    result = Voorhees(original)
    assert original == result.copy()

