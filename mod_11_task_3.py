import math


def is_exist(size: float, speed: float) -> bool:
    return (size <= 0)  or (speed <= 0)

def is_fust(size: float, speed: float) -> bool:
    return size < speed


def download_speed(size: float, speed: float):
    if is_exist(size, speed):
        raise ValueError(f"Объем файла и скорость скачивания должны быть положительными.")

    if is_fust(size, speed):
        raise ValueError(f"Скасивание завершено (менее чем за 1 секунду)!")

    all_time = math.ceil(size // speed)
    download_part = 0

    for time in range(1, all_time + 2):
        download_part += speed
        if download_part < size:
            print(f"Прошло {time} сек. Скачено {round(download_part, 2)} Мб из {size} Мб. Завершено {round(download_part * 100 / size)} %")
        else:
            print(f"Прошло {time} сек. Скачено {size} Мб из {size} Мб. Завершено 100 %")

        download_time = time

    return


if __name__ == '__main__':
    test_cases = [
        (123, 27),
        (-3, 0),
        (128, 0),
        (1269.467, 4.46),
        (12.8, 0.3)
    ]

    for size, speed in test_cases:
        try:
            result_download_time = download_speed(size, speed)
            print(f"Скачивание обновления заняло: {result_download_time} сек.\n")
        except ValueError as err:
            print(err)
