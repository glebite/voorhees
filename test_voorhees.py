import pytest
from .voorhees import Voorhees

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

@pytest.mark.test_id(17)
def test_empty_strings():
    original = {'something': ''}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(18)
def test_mix_it_up():
    original = {"response_code": 200, "train_number": "12229", "position": "at Source", "route": [{"no": 1, "has_arrived": False, "has_departed": False, "scharr": "Source", "scharr_date": "15 Nov 2015", "actarr_date": "15 Nov 2015", "station": "LKO", "actdep": "22:15", "schdep": "22:15", "actarr": "00:00", "distance": "0", "day": 0}, {"actdep": "23:40", "scharr": "23:38", "schdep": "23:40", "actarr": "23:38", "no": 2, "has_departed": False, "scharr_date": "15 Nov 2015", "has_arrived": False, "station": "HRI", "distance": "101", "actarr_date": "15 Nov 2015", "day": 0}]}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(19)
def test_deeper_test():
    original = {"destination_addresses": ["Philadelphia, PA, USA"], "origin_addresses": ["New York, NY, USA"], "rows": [{"elements": [{"distance": {"text": "94.6 mi", "value": 152193}, "duration": {"text": "1 hour 44 mins", "value": 6227}, "status": "OK"}]}], "status": "OK"}
    result = Voorhees(original)
    assert original == result.copy()

@pytest.mark.test_id(20)
def test_lots_more():
    original = {"destination_addresses": ["Washington, DC, USA", "Philadelphia, PA, USA", "Santa Barbara, CA, USA", "Miami, FL, USA", "Austin, TX, USA", "Napa County, CA, USA"], "origin_addresses": ["New York, NY, USA"], "rows": [{"elements": [{"distance": {"text": "227 mi", "value": 365468}, "duration": {"text": "3 hours 54 mins", "value": 14064}, "status": "OK"}, {"distance": {"text": "94.6 mi", "value": 152193}, "duration": {"text": "1 hour 44 mins", "value": 6227}, "status": "OK"}, {"distance": {"text": "2,878 mi", "value": 4632197}, "duration": {"text": "1 day 18 hours", "value": 151772}, "status": "OK"}, {"distance": {"text": "1,286 mi", "value": 2069031}, "duration": {"text": "18 hours 43 mins", "value": 67405}, "status": "OK"}, {"distance": {"text": "1,742 mi", "value": 2802972}, "duration": {"text": "1 day 2 hours", "value": 93070}, "status": "OK"}, {"distance": {"text": "2,871 mi", "value": 4620514}, "duration": {"text": "1 day 18 hours", "value": 152913}, "status": "OK"}]}], "status": "OK"}
    result = Voorhees(original)
    assert original == result.copy()    

@pytest.mark.test_id(21)
def test_simple_search():
    original = {"what": 4}
    result = Voorhees(original).search('what')
    # TODO: fix this so we don't have to cast - it is what it is...
    assert result == 4

@pytest.mark.test_id(22)
def test_missing_key():
    original = {"what": 4}
    try:
        result = Voorhees(original).search('cannotfindthis')
        assert False
    except KeyError as e:
        assert True

@pytest.mark.test_id(23)
def test_more_depth():
    original = {"destination_addresses": ["Washington, DC, USA", "Philadelphia, PA, USA", "Santa Barbara, CA, USA", "Miami, FL, USA", "Austin, TX, USA", "Napa County, CA, USA"], "origin_addresses": ["New York, NY, USA"], "rows": [{"elements": [{"distance": {"text": "227 mi", "value": 365468}, "duration": {"text": "3 hours 54 mins", "value": 14064}, "status": "OK"}, {"distance": {"text": "94.6 mi", "value": 152193}, "duration": {"text": "1 hour 44 mins", "value": 6227}, "status": "OK"}, {"distance": {"text": "2,878 mi", "value": 4632197}, "duration": {"text": "1 day 18 hours", "value": 151772}, "status": "OK"}, {"distance": {"text": "1,286 mi", "value": 2069031}, "duration": {"text": "18 hours 43 mins", "value": 67405}, "status": "OK"}, {"distance": {"text": "1,742 mi", "value": 2802972}, "duration": {"text": "1 day 2 hours", "value": 93070}, "status": "OK"}, {"distance": {"text": "2,871 mi", "value": 4620514}, "duration": {"text": "1 day 18 hours", "value": 152913}, "status": "OK"}]}], "status": "OK"}
    result = Voorhees(original).search('destination_addresses')
    expected = ["Washington, DC, USA", "Philadelphia, PA, USA", "Santa Barbara, CA, USA", "Miami, FL, USA", "Austin, TX, USA", "Napa County, CA, USA"]
    assert result == expected

@pytest.mark.test_id(24)
def test_remove_key():
    original = {"something": 1, "somethingelse": 2}
    expected = {"somethingelse": 2}
    result = Voorhees(original).del_keyvalue_pair('something')
    assert result == expected

@pytest.mark.test_id(25)
def test_remove_last_key():
    original = {"something": 1}
    expected = {}
    result = Voorhees(original).del_keyvalue_pair('something')
    assert result == expected
