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
        return str(json_string)
    
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

    def search(self, key=None, dump_as_json = False):
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
        """
        acc_result = ""
        def walk(obj, acc_result):
            """Recursively search for values of key in JSON tree."""
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
    
if __name__ == "__main__":
    pass
