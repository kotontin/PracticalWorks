import math


def first_figure(number: float) -> int:

    # нельзя пользоваться условной инструкцией, циклом или строками.

    number = abs(number)
    figure = int(number * 10) % 10

    return figure


if __name__ == '__main__':
    test_cases = [
        (-6707567.432197408),
        (0.39555),
        (1),
        (108.102666),
        (2.5),
        (1982682.81432)
    ]

    for number in test_cases:
         result_figure = first_figure(number)
         print(f"Первая цифра вещественного числа {number} после точки: {result_figure}")
