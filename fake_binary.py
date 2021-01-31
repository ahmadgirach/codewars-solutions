"""
https://www.codewars.com/kata/57eae65a4321032ce000002d

Given a string of digits, you should replace any digit below 5 with '0' and
any digit 5 and above with '1'. Return the resulting string.
"""


def create_fake_binary(message: str) -> str:
    digits = tuple(message)
    binary_digits = [str(0) if int(digit) < 5 else str(1) for digit in digits]
    return "".join(binary_digits)


print(create_fake_binary("654152"))
