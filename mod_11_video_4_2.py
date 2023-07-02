import math

def coordinates(distance: float, angle: float):

    angle /= 57.2958
    x = round(math.cos(angle) * distance, 2)
    y = round(math.sin(angle) * distance, 2)

    return (x, y)


if __name__ == '__main__':
    test_cases = [
        (-30, 180),
        (10, 90),
        (0, 370),
        (30, -30),
        (1, 30),
        (3.5, 91)
    ]

    for distance, angle in test_cases:
        result_coordinates = coordinates(distance, angle)
        print(f"Пройдено расстояние {distance} единиц под углом {angle} градусов. Новые координаты (x, y) = {result_coordinates}")

