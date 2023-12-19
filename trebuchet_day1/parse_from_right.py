#!/usr/bin/env python


def parse_from_right(line: str) -> int:

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if len(line) == 0:
        return ''
    if line[-1:] in digits:
        return str(line[-1:])

    return parse_from_right(line[:-1])
