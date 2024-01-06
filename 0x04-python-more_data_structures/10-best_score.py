#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictonary is None:
        return None
    max_val = 0
    max_ky = None
    for k , v in a_dictionary.items():
        if v > max_val:
            max_val = v
            max_ky = k
            return max_ky
