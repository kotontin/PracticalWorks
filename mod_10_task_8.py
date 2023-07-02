def task_10_8_1(levels: int) -> list[str]:
    print('\nЗадача 10-8 - Яма\n')
    lines = []
    row, new_row, rewerse_new_row = '', '', ''

    for number in range(levels, 0, -1):
        row += str(number)

    for level in range(levels):
        width = levels - level - 1
        new_row = row[0:level + 1] + '.' * width
        rewerse_new_row = new_row[::-1]
        lines.append(f"{new_row}{rewerse_new_row}")

    return lines


def task_10_8_2(levels: int) -> list[str]:
    lines = []

    for level in range(1, levels + 1):
        row = ''
        for row_number in range(levels, levels - level, -1):
            row += str(row_number)

        ratio = 2
        points = '.' * ratio * (levels - level)
        reverse_row = row[::-1]
        lines.append(f"{row}{points}{reverse_row}")

    return lines


if __name__ == '__main__':
    result_lines = task_10_8_2(5)
    print("\n".join(result_lines))
