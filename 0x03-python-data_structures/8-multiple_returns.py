#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    if sentence:
        letter = sentence[0]
    else:
        letter = None
    return(i, letter)
