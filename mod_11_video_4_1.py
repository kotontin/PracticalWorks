import math


def is_exist(a: float, b: float, c: float) -> bool:
    return (a + b <= c) or (a + c <= b) or (b + c) <= a

def geron_area_triangle(a: float, b: float, c: float) -> float:
    if is_exist(a, b, c):
        raise ValueError(f"Треугольника со сторонами ({a}, {b}, {c}) не существует ")

    p = int((a + b + c) / 2)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    S = round(S, 4)
    return S


if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (10, 10, 10),
        (0, 0, 0),
        (100, 1, 1),
        (-3, 4, 5),
        (3.5, 4.5, 5.5)
    ]

    for a, b, c in test_cases:
        try:
            result_S = geron_area_triangle(a, b, c)
            print(f"Площадь треугольника со сторонами ({a}, {b}, {c}) по формуле Герона S = {result_S}")
        except ValueError as err:
            print(err)
