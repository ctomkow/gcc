#!/usr/bin/env python

import re


def get_red(line: str) -> int:

    red = 0

    l = re.split('.*: |, |; ', line)

    for cubes in l:
        row = cubes.split(' ')

        if len(row) == 2:
            if str(row[1]) == 'red':
                if int(row[0]) > red:
                    red = int(row[0])

    return red


if __name__ == "__main__":

    sample = 'Game 58: 6 blue, 1 red, 6 green; 3 red, 9 blue; 4 red, 9 blue, 5 green; 1 green, 5 red, 7 blue'

    get_red(sample)
