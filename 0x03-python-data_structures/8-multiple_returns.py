#!/usr/bin/python3

def multiple_returns(sentence):
    len_sentence = len(sentence)
    
    if len_sentence == 0:
        first_char = None
    else:
        first_char = sentence[0]

    tuple_new = (len_sentence, first_char)

    return tuple_new
