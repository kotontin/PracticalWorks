import math

land_volume = 1.08321 * 10 ** 12
land_R = (land_volume / 3 * math.pi / 4) ** (1/3)
print(f"Радиус Земли: {land_R} \n")


def is_exist(planet_R: float) -> bool:
    return planet_R <= 0


def compare_volume_planets(planet_R: float) -> float:
    if is_exist(planet_R):
        raise ValueError(f"Нет решения.\n")

    planet_volume = 4 * math.pi / 3 * (planet_R ** 3)

    print(f"Объем Земли {land_volume}, объем планеты: {planet_volume}")

    if planet_volume < land_volume:
        compare_volume = land_volume / planet_volume
    elif planet_volume > land_volume:
        compare_volume = planet_volume / land_volume
    else:
        compare_volume = 1

    return round(compare_volume, 3)


if __name__ == '__main__':
    test_cases = [
        (6569.2),
        (6569.925261403126),
        (6570),
        (6572.495424),
        (16789),
        (5.43789 * 10 ** 12),
        (0),
        (0.08321),
        (10),
        (-16789)
    ]

    for planet_R in test_cases:
        try:
            result_compare = compare_volume_planets(planet_R)
            if land_R > planet_R:
                print(f"Земля больше потенциальной планеты радиуса {planet_R} в {result_compare} раз.\n")
            elif land_R < planet_R:
                print(f"Земля меньше потенциальной планеты радиуса {planet_R} в {result_compare} раз.\n")
            else:
                print(f"Объем Земляи равен объему потенциальной планеты радиуса {planet_R}.\n")
        except ValueError as err:
            print(err)