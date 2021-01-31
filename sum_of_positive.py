"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def calculate_sum(numbers):
    total = sum([number for number in numbers if number > 0])
    return total


print(calculate_sum([1, -4, 7, 12]))
