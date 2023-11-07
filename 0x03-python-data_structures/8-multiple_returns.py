#!/usr/bin/python3
def multiple_returns(sentence):
    my_t = ()
    if len(sentence) == 0:
        my_t = 0, "None"
    else:
        my_t = len(sentence), sentence[0]
    return my_t
