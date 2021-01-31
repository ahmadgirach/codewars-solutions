"""
It's pretty straightforward. Your goal is to create a function that removes
the first and last characters of a string. You're given one parameter,
the original string. You don't have to worry with strings with less than
two characters.
"""


def remove_chars(message: str) -> str:
    if len(message) > 2:
        result = message[1:-1]
    else:
        result = message

    return result


print(remove_chars("aabrakadabra"))
