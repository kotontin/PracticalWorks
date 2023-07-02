print('\n', '-' * 8 + ' З А Д А Ч И   П О Д    В И Д Е О ' + '-' * 8, '\n')


def mod_10_video_1_1():
    print('\nТаблица умножения\n')

    for i in range(1, 10):
        for j in range(1, 10):
            print(i * j, "\t", end = '')
        print()


def mod_10_video_1_2():
    print('\nТаблица суммы\n')
    number = int(input('Введите число: '))

    for i in range(1, number + 1):
        for j in range(1, number + 1):
            print(i * j, "\t", end = '')
        print()


def mod_10_video_1_3():
    print('\nАнализ данных\n')

    for i in range(10, 0, -1):
        for j in range(10, 0, -1):
            print(j - i, "\t", end = '')
        print()


def mod_10_video_2_1():
    print('\nКвадратная матрица\n')

    n = int(input('Введите размерность матрицы: '))

    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if row % 2 == 0:
                print(row, "\t", end = '')
            else:
                print(col, "\t", end = '')
        print()


def mod_10_video_2_2():
    print('\nЧёрный ящик\n')

    n = int(input('Введите размерность матрицы: '))

    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if col % 3 == 0:
                print(col, "\t", end = '')
            else:
                print(row, "\t", end = '')
        print()


def mod_10_video_2_3():
    print('\nКоординатные оси\n')

    for row in range(20):
        for col in range(50):
            if row == 9:
                print('-', end = '')
            elif col == 24:
                print('|', end = '')
            else:
                print(' ', end = '')
        print()


def mod_10_video_3_1():
    print('\nВрата\n')

    for row in range(20):
        for col in range(30):
            if row == 0:
                print('-', end = '')
            elif col == 0 or col == 29:
                print('|', end = '')
            else:
                print(' ', end = '')
        print()


def mod_10_video_3_2():
    print('\nДорога\n')

    for row in range(20):
        for col in range(50):
            if row == 9:
                print('-', end = '')
            elif col == 24:
                print('|', end = '')
            elif col == row + 29:
                print('\\', end = '')
            elif col == -row + 19:
                print('/', end = '')
            else:
                print(' ', end = '')
        print()


def mod_10_video_3_3():
    print('\nДиагональная матрица\n')

    n = int(input('Введите размерность матрицы: '))

    for row in range(1, n + 1):
        for col in range(n, 0, -1):
            if row > col:
                print('2', "\t", end = '')
            elif row < col:
                print('0', "\t", end = '')
            else:
                print('1', "\t", end = '')
        print()


def mod_10_video_4_1():
    print('\nЭлектронная очередь\n')

    people = int(input('Введите кол-во людей в очереди: '))

    for hour in range(people):
        print('Час', hour, '-й: ')
        for number in range(hour, people):
            print('Номер в очереди: ', number)
        print()

    print('Обслуживание завершено!')


def mod_10_video_4_2():
    print('\nЦифры больше пяти\n')

    sequence = input('Введите последовательность чисел: ')

    count = 0
    for number in sequence:
        if number == '6' or number == '7' or number == '8' or number == '9':
            count += 1

    print(f"Из них {count} - больше пяти.")


def mod_10_video_4_3():
    print('\nЛестница чисел\n')

    number = int(input('Введите число: '))
    print()

    for row in range(0, number + 1):
        for col in range(row, number + 1):
            print(col, "\t", end = '')
        print()


mod_10_video_1_1()
mod_10_video_1_2()
mod_10_video_1_3()
mod_10_video_2_1()
mod_10_video_2_2()
mod_10_video_2_3()
mod_10_video_3_1()
mod_10_video_3_2()
mod_10_video_3_3()
mod_10_video_4_1()
mod_10_video_4_2()
mod_10_video_4_3()
