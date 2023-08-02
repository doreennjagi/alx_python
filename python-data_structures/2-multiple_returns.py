#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:  # Check if the sentence is empty (or None)
        return (0, None)
    else:
        return (len(sentence), sentence[0])
print(multiple_returns("Hello")) 
print(multiple_returns("")) 
