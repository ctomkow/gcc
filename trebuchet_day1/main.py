#!/usr/bin/env python

# # function
# # todo: open file
# # todo: read by line break
# # main loop
# # feed into paring functions
# # take outputs and feed into combining function for result
#
# # function
# # todo: parse from left
# input: str(line)
# output: dict
#     - key: line number
#     - value: str(int) found
#
# # function
# # todo: parse from right
# input: str(line)
# output: dict
#     - key: line number
#     - value: str(int) found
#
# # function
# # todo: combine dicts from parse left and right and do math
# input: dict(left), dict(right)
# print final int tota

with open(os.path.join(sys.path[0],"starmap"),'r') as txtlines:
    lines = txtlines.readlines()
    
    for line in lines:
        line = line.strip()
        find_from_left(line: str)
        find_from_right(line: str)
