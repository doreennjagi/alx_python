#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary)== 0:
        return None
    my_dict= list(a_dictionary.keys())[0]
    best_score= a_dictionary [my_dict]
    for k, z in a_dictionary.items():
        if z > best_score:
            best_score=z
            my_dict=k
            return (my_dict)