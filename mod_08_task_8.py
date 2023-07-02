def no_solution(boys: int, girls: int) -> bool:
    if (boys > 2 * girls) or (girls > 2 * boys):
        return True

    return False


def arrange_seats(boys: int, girls: int) -> str:
    if no_solution(boys, girls):
        return "Нет решения"

    answer = ''

    if boys >= girls:
        for bgb in range(boys - girls):
            answer += 'BGB'
        for bg in range(2 * girls - boys):
            answer += 'BG'

    if girls >= boys:
        for gbg in range(girls - boys):
            answer += 'GBG'
        for gb in range(2 * boys - girls):
            answer += 'GB'

    return "".join(answer)


if __name__ == '__main__':
    test_cases = [
        (50, 100),
        (100, 50),
        (5, 9),
        (5, 10),
        (6, 14),
        (10, 15)
    ]

    for boys, girls in test_cases:
        result = arrange_seats(boys, girls)
        print(f"Количество мальчиков: {boys}, Количество девочек: {girls}")
        print(f"Ответ: {result}\n")
