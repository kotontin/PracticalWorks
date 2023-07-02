import math


def is_negative(x: float) -> bool:
    return x < 0


def is_float(x: float) -> bool:
    return isinstance(x, float)


def factorial_number(x: int):
    if is_negative(x):
        raise ValueError(f"Факториал вычисляется только от натурального числа, а это отрицательное!")
    elif is_float(x):
        raise ValueError(f"Факториал вычисляется только от натурального числа, а это дробное!")

    return math.factorial(x)


def abs_number(x: float):
    return abs(x)


def floor_number(x: float):
    return math.floor(x)


def ceil_number(x: float):
    return math.ceil(x)


def sqrt_number(x: float):
    if is_negative(x):
        raise ValueError(f"Не будем сейчас извлекать корень из отрицательного числа.")

    return math.sqrt(x)


def exp_number(x: float):
    return math.exp(x)


def log_number(x: float):
    if is_negative(x) or x == 0:
        raise ValueError(f"Натуральный логарифм от отрицательного числа не существует, а нуля - это неопределенность!")
    return math.log(x)


def log2_number(x: float):
    if is_negative(x) or x == 0:
        raise ValueError(f"Логарифм по основанию 2 от отрицательного числа не существует, а от нуля - это неопределенность!")
    return math.log2(x)


def log10_number(x: float):
    if is_negative(x) or x == 0:
        raise ValueError(f"Десятичный логарифм от отрицательного числа не существует, а от нуля - это неопределенность!")
    return math.log10(x)


def sin_x(x: float):
    x /= 57.2958

    return math.sin(x)


def cos_x(x: float):
    x /= 57.2958

    return math.cos(x)


if __name__ == '__main__':
    test_cases = [
        (-1),
        (0),
        (1),
        (3),
        (1.5),
        (5),
        (250),
        (-12.0964)
    ]

    for x in test_cases:

        result_abs = abs_number(x)
        print(f"Модуль {x} = {result_abs}\n")

        result_floor = floor_number(x)
        print(f"Округленный в пол {x} = {result_floor}\n")

        result_ceil = ceil_number(x)
        print(f"Округленный в потолок {x} = {result_ceil}\n")

        result_sin = sin_x(x)
        print(f"sin({x}) = {result_sin}\n")

        result_cos = cos_x(x)
        print(f"cos({x}) = {result_cos}\n")

        result_exp = exp_number(x)
        print(f"Число e в степени x, e^{x} = {result_exp}\n")

        try:
            result_sqrt = sqrt_number(x)
            print(f"Квадратный корень из {x} = {result_sqrt}\n")

            result_log = log_number(x)
            print(f"Натуральный логарифм (по основанию e) числа {x} = {result_log}\n")

            result_log2 = log2_number(x)
            print(f"Двоичный логарифм числа {x} = {result_log2}\n")

            result_log10 = log10_number(x)
            print(f"Десятичный логарифм числа {x} = {result_log10}\n")

            result_factorial = factorial_number(x)
            print(f"{x}! = {result_factorial}\n")

        except ValueError as err:
            print(err)
        finally:
            print(f"Число e = {math.e}, число Пи = {math.pi}\n")
