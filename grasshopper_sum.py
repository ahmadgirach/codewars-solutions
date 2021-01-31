"""
Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""


def grasshopper_summation(number: int) -> int:
    total = sum([n for n in range(number + 1)])
    return total


print(grasshopper_summation(8))
