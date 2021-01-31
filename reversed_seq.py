"""
https://www.codewars.com/kata/5a00e05cc374cb34d100000d

Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 >> [5,4,3,2,1]
"""


def create_reverse_seq(number: int) -> []:
    seq = [n for n in range(number, 0, -1)]
    return seq


print(create_reverse_seq(5))
