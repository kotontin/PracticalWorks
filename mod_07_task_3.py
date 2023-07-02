import math

def is_positive(number: int) -> bool:
    return number < 0

def is_float(number: int) -> bool:
    return isinstance(number, float)

def factorial_number(number: int):
    if is_positive(number):
        raise ValueError(f"Факториал вычисляется только от натурального числа, а это отрицательное!")
    elif is_float(number):
        raise ValueError(f"Факториал вычисляется только от натурального числа, а это дробное!")

    return math.factorial(number)


if __name__ == '__main__':
    test_cases = [
        (-1),
        (0),
        (1),
        (3),
        (1.5),
        (5)
    ]

    for number in test_cases:
        try:
            result_factorial = factorial_number(number)
            print(f"{number}! = {result_factorial}")
        except ValueError as err:
            print(err)
