def task_10_7(levels: int) -> None:
    current_number = 1
    lines = []

    for level in range(levels):
        spaces = " " * (levels - level - 1)
        row = ""

        for _ in range(level + 1):
            if current_number < 10:
                row += f" {current_number} "
            else:
                row += f"{current_number} "
            current_number += 2

        lines.append(f"{' '}{spaces}{row}")

    return lines


if __name__ == '__main__':
    result_lines = task_10_7(5)
    print("\n".join(result_lines))
