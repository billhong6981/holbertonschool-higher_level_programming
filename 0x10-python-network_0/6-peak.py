#!/usr/bin/python3
"""my module"""

def find_peak(list_of_integers):
    """my function"""
    if list_of_integers:
        peak = list_of_integers[0]
        for i in range(len(list_of_integers)):
            if peak < list_of_integers[i]:
                peak = list_of_integers[i]
        return (peak)
    return (None)
