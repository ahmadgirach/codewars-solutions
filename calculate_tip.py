"""
Problem:

Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#
Because you're a nice person, you always round up the tip, regardless of the service.
"""


def calculate_tip(tip=0):
    tip_res = {
        "0": "Terrible",
        "5": "Poor",
        "10": "Good",
        "15": "Great",
        "20": "Excelent",
    }

    if tip in tip_res:
        message = tip_res.get(tip)
    else:
        message = "Rating not recognised"

    return message
