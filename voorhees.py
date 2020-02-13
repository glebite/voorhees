"""
voorhees.py
"""
import json

class Voorhees:
    """
    Voorhees - class to handle json slicing/dicing/mangling
    """
    def __init__(self,json_string):
        """
        """
        self.incoming_json_string = json_string
        
    def abyss_copy(self, key):
        """
        """
        acc_result = ""
        def walk(obj, acc_result, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                acc_result += '{'
                for k, v in obj.items():
                    if k == key:
                        k = key+'changed'
                    if isinstance(v, (dict, list)):
                        acc_result += '"' + k + '":'                    
                        acc_result = walk(v, acc_result, key)
                    else:
                        acc_result += '"' + k + '":'                                        
                        if type(v) == str:
                            acc_result += '"{}",'.format(v)
                        elif type(v) == int:
                            acc_result += '{},'.format(v)
                        elif type(v) == bool:
                            acc_result += '{},'.format(v)                    
                acc_result = acc_result[:-1]; acc_result += '},'
            elif isinstance(obj, list):
                acc_result += '['
                for item in obj:
                    acc_result = walk(item, acc_result, key)
                acc_result = acc_result[:-1]; acc_result += '],'
            else:
                if type(obj) == str:
                    acc_result += "'" + str(obj) +'"'; acc_result += ","
                elif type(obj) == int:
                    acc_result += str(obj); acc_result += ","
            return acc_result
        acc_result = walk(self.incoming_json_string, acc_result, key)
        return acc_result[:-1]

if __name__ == "__main__":
    data = {"what": 3}
    x = Voorhees(data)
    print(x.abyss_copy('contact'))
