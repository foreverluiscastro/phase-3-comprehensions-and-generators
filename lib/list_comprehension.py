#!/usr/bin/env python3

from logging import makeLogRecord
import ipdb

def return_evens(num_list):
    pass
    even_list = [n for n in num_list if n % 2 == 0]
    # ipdb.set_trace()
    return even_list

return_evens([1,3,5])

def make_exclamation(sentence_list):
    pass
    # ipdb.set_trace()
    exclamationed_strings = [str + "!" for str in sentence_list]
    return exclamationed_strings

make_exclamation(["Your", "Mom's", "House"])