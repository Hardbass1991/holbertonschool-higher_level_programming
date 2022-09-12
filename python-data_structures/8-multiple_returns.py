#!/usr/bin/python3
def multiple_returns(sentence):
    n = 0
    m = None
    if sentence:
        n += len(sentence)
        m = sentence[0]
    return n, m
