"""
https://www.codewars.com/kata/5933a1f8552bc2750a0000ed

Return the Nth Even Number

nthEven(1) //=> 0, the first even number is 0
nthEven(3) //=> 4, the 3rd even number is 4 (0, 2, 4)

nthEven(100) //=> 198
nthEven(1298734) //=> 2597466
"""


def find_nth_even(n):
    try:
        num_list = tuple(num for num in range(n * 2))
        only_evens = [n for n in num_list if n % 2 == 0]
        return only_evens[-1] if only_evens else 0
    except IndexError:
        return 0


print(find_nth_even(1))
print(find_nth_even(3))
print(find_nth_even(100))
