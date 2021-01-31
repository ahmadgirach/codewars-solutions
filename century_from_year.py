"""
The first century spans from the year 1 up to and including the year 100,
The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
"""


def calculate_century(year: int) -> int:
    # Gives us the extra years gone past
    additional_years = (year % 1000) % 100

    # first two digits of year
    div = int(year / 100)

    if additional_years == 0:
        result = div
    else:
        result = div + 1

    return result


print(calculate_century(1705))
print(calculate_century(1900))
print(calculate_century(1601))
print(calculate_century(2000))
