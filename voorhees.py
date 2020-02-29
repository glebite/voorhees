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
        return {'incoming_json_string': self.incoming_json_string}

    def __str__(self):
        """ string - full string conversion of json_string """
        return str(f'Voorhees(json_string={self.incoming_json_string})')
    
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
        return json.loads(acc_result[:-1])

    def search(self, key, dump_as_json = False):
        """
        search - find a key and dump the sub value out or all remaining

        This is more of an exploration into types, traversal, recursion,
        and a matter of a programming exercise.

        TODO: solve what to do with redundant keys (listify them?)

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

    def del_keyvalue_pair(self, key):
        """
        """
        acc_result = ""
        def walk(obj, acc_result, key):
            """Recursively walk and replicate JSON tree without a specific key."""
            if isinstance(obj, dict):
                acc_result += '{'
                for k, v in obj.items():
                    if k == key:
                        continue
                    if isinstance(v, (dict, list)):
                        acc_result += '"' + k + '":'                    
                        acc_result = walk(v, acc_result,key)
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
                    acc_result = walk(item, acc_result,key)
                acc_result = acc_result[:-1]; acc_result += '],'
            else:
                if type(obj) == str:
                    acc_result += '"' + str(obj) + '"' + ","
                if type(obj) in [int, bool, float]:
                    acc_result += str(obj) + ","
            return acc_result
        acc_result = walk(self.incoming_json_string, acc_result,key)
        if acc_result == "},":
            # degenerate case of deleting last element
            # inelegance implies flawed logic
            acc_result = "}"
            return json.loads('' or '{}')
        return json.loads(acc_result[:-1])

    
    
if __name__ == "__main__":
    original = {"status": 3}
    # result = Voorhees(original).del_keyvalue_pair('status')
    x = Voorhees(original).del_keyvalue_pair('status')
