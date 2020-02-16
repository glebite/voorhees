"""
voorhees.py

Accredited: (when I find the code that I used to model this from, I will
                      include it.)
"""
import json

class Voorhees:
    """
    Voorhees - class to handle json slicing/dicing/mangling
    """
    def __init__(self,json_string):
        """
        initialization method - takes a string
        """
        self.incoming_json_string = json_string

    def __repr__(self):
        """ representation - minimized output """
        return "<Voorhees {}...>".format(json_string[0:10])

    def __str__(self):
        """ string - full string conversion of json_string """
        return str(self.incoming_json_string)
    
    def copy(self):
        """
        copy - this performs a dictionary copy
        This is more of an exploration into types, traversal, recursion,
        and a matter of a programming exercise.  Refactoring to follow.
        """
        acc_result = ""
        def walk(obj, acc_result):
            """Recursively walk and replicate JSON tree."""
            if isinstance(obj, dict):
                acc_result += '{'
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        acc_result += '"' + k + '":'                    
                        acc_result = walk(v, acc_result)
                    else:
                        acc_result += '"' + k + '":'                                        
                        if type(v) == str:
                            acc_result += '"{}",'.format(v)
                        if type(v) in [int, bool, float]:
                            acc_result += '{},'.format(v).lower()
                acc_result = acc_result[:-1]; acc_result += '},'
            elif isinstance(obj, list):
                acc_result += '['
                for item in obj:
                    acc_result = walk(item, acc_result)
                acc_result = acc_result[:-1]; acc_result += '],'
            else:
                if type(obj) == str:
                    acc_result += '"' + str(obj) + '"' + ","
                if type(obj) in [int, bool, float]:
                    acc_result += str(obj) + ","
            return acc_result
        acc_result = walk(self.incoming_json_string, acc_result)
        print(acc_result[:-1])
        return json.loads(acc_result[:-1])

    def search(self, key, dump_as_json = False):
        """
        search - find a key and dump the sub value out or all remaining

        This is more of an exploration into types, traversal, recursion,
        and a matter of a programming exercise.

        Params:
            key - the key that is sought for in the dictionary
            dump_as_json - whether or not the output is a list or just the 
                                       value at the list

        Example:
            % data = {'what': 3, 'things': [1,2,3,4,5]}
            % Voorhees(data).search('what')
            3
            % Voorhees(data).search('things')
            [1,2,3,4,5]
            % Voorhees(data).search(dump_as_json = True)
            {'things': [1,2,3,4,5]}

        Return:
        acc_result - string (up to you to convert it after...)
                          - empty string if no match (might raise an Exception)
        """
        acc_result = ""
        def walk(obj, acc_result, key, dump_as_json = False):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == key:
                        if dump_as_json:
                            acc_result = json.dumps('{"' + key + '":' + str(obj[key]) + "}")
                        else:
                            acc_result = obj[key]
                        return acc_result
                    if isinstance(v, (dict, list)):
                        acc_result = walk(v, acc_result, key, dump_as_json)
            elif isinstance(obj, list):
                for item in obj:
                    acc_result = walk(item, acc_result, key, dump_as_json)
            return acc_result
        acc_result = walk(self.incoming_json_string, acc_result, key, dump_as_json)
        if acc_result == "":
            raise KeyError
        return acc_result

    
if __name__ == "__main__":
    original = {"destination_addresses": ["Washington, DC, USA", "Philadelphia, PA, USA", "Santa Barbara, CA, USA", "Miami, FL, USA", "Austin, TX, USA", "Napa County, CA, USA"], "origin_addresses": ["New York, NY, USA"], "rows": [{"elements": [{"distance": {"text": "227 mi", "value": 365468}, "duration": {"text": "3 hours 54 mins", "value": 14064}, "status": "OK"}, {"distance": {"text": "94.6 mi", "value": 152193}, "duration": {"text": "1 hour 44 mins", "value": 6227}, "status": "OK"}, {"distance": {"text": "2,878 mi", "value": 4632197}, "duration": {"text": "1 day 18 hours", "value": 151772}, "status": "OK"}, {"distance": {"text": "1,286 mi", "value": 2069031}, "duration": {"text": "18 hours 43 mins", "value": 67405}, "status": "OK"}, {"distance": {"text": "1,742 mi", "value": 2802972}, "duration": {"text": "1 day 2 hours", "value": 93070}, "status": "OK"}, {"distance": {"text": "2,871 mi", "value": 4620514}, "duration": {"text": "1 day 18 hours", "value": 152913}, "status": "OK"}]}], "status": "OK"}
    result = Voorhees(original).search('status')
    print(result)
