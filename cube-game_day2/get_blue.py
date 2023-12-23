#!/bin/bash


import re



def get_blue(line: str) -> int:
    blue =0 
    digit_bluelookup = re.findall('\d{2} blue|\d{1} blue',line)
    for line_lookup in digit_bluelookup:
        split_lookup = line_lookup.split()
        count_blue = int(split_lookup[0])
        if count_blue >  blue:
            blue = count_blue
    
    return blue
