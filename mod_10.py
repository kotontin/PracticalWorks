def task_10_1():
    print('\nЗадача 10-1 - Тестовое задание (проанализировать таблицу, понять, как она строится, и написать программу для её вывода на экран).\n')

    for row in range(6):
        for col in range(6):
            print(col * 2 + row, "\t", end='')
        print()

    print()



def task_10_2():
    print('\nЗадача 10-2 - Лестница (выводит «лестницу» из чисел, когда пользователь вводит число N).\n')

    dim = int(input('Введите число: '))

    count = 0

    for row in range(dim + 1, 0, -1):
        for col in range(dim + 1, row, -1):
            print(count, "\t", end='')
        count += 1
        print()

    print()



def task_10_3():
    print('\nЗадача 10-3 - Рамка (рисует прямоугольную рамку с помощью символьной графики).\n')

    dim_row = int(input('Введите высоту рамки: '))
    dim_col = int(input('Введите ширину рамки: '))

    for row in range(dim_row):
        for col in range(dim_col):
            if row == 0 or row == dim_row - 1:
                print('-', end='')
            elif col == 0 or col == dim_col - 1:
                print('|', end='')
            else:
                print(' ', end='')
        print()

    print()



def task_10_4():
    print('\nЗадача 10-4 - Простые числа (считает количество простых чисел в заданной последовательности).\n')

    quant_num = int(input('Введите количество чисел: '))
    list_num = []
    quant_simple_num = 0

    for num in range(quant_num):
        num = int(input(f"Введите {num + 1}-е число: "))
        list_num.append(num)

    temp_list_num = []
    for i in range(0, quant_num):
        for j in range(2, list_num[i] + 1):
            for k in temp_list_num:
                if k > (j ** 0.5 + 1):
                    temp_list_num.append(j)
                    break
                if (j % k == 0):
                    break
            else:
                temp_list_num.append(j)
        print(f"Простые числа в числе {list_num[i]}: {temp_list_num}")
        quant_simple_num += len(temp_list_num)
        temp_list_num.clear()
    print(f"Количество простых чисел в последовательности: {quant_simple_num}")



def task_10_5():
    print('\nЗадача 10-5 - Наибольшая сумма цифр (среди введенных натуральных чисел найдите наибольшее по сумме цифр).\n')

    import math

    sequence = input('Введите последовательность чисел через запятую и/или пробел: ')
    list_sequence = []

    if sequence.find(', '):
        list_sequence = sequence.split(', ')
    elif sequence.find(','):
        list_sequence = sequence.split(',')
    elif sequence.find(' '):
        list_sequence = sequence.split(' ')

    sum_elements = 0
    list_sum_elements = []

    for elem in list_sequence:
        elem = abs(int(elem))
        while elem > 0:
            sum_elements += elem % 10
            elem = elem // 10
            print(elem)
        list_sum_elements.append(sum_elements)
        sum_elements = 0

    print(f"Максимальная сумма цифр в последовательности чисел: {max(list_sum_elements)}, число: {list_sequence[list_sum_elements.index(max(list_sum_elements))]}")



def task_10_6():
    print('\nЗадача 10-6 - Пирамидка (выводит на экран равнобедренный треугольник (пирамидку), заполненный символами хештега).\n')

    hight = int(input('Введите высоту пирамидки: '))
    print()

    for i in range(hight):
        for j in range(1, 2):
            print(' ' * (hight - i), '#' * (j + i * 2), ' ' * (hight - i), "\t", end = '')
        print()

    print()



def task_10_7(rows: int) -> None:
    print('\nЗадача 10-7 - Пирамидка-2 (получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами).\n')
    
    new_num = 1

    for line in range(rows):
        for spase in range(rows - line - 1, 0, -1):
            print(end = '   ')
        for number in range(line + 1):
            print(new_num, end = '    ')
            new_num += 2
        print()



def task_10_7_2(levels: int) -> None:
    
    current_number = 1

    for level in range(levels):
        spaces = " " * (levels - level - 1)
        row = ""
        for _ in range(level + 1):
            if current_number < 10:
                row += f" {current_number} "
            else:
                row += f"{current_number} "
            current_number += 2

        print(' ', spaces, row)



def task_10_8(levels: int) -> None:
    print('\nЗадача 10-8 - Яма (получает на вход число N и выводит на экран числа в виде ямы) - моё решение\n')

    row, new_row, rewerse_new_row = '', '', ''

    for level in range(levels, 0, -1):
        row += str(level)

    for level in range(levels):
        width = levels - level - 1
        new_row = row[0:level + 1] + '.' * width
        rewerse_new_row = new_row[::-1]
        print(new_row + rewerse_new_row)



def task_10_8_2():
    print('\nЗадача 10-8 - Яма (получает на вход число N и выводит на экран числа в виде ямы) - верное решение\n')
    
    depth = int(input('Введите глубину ямы: '))

    for line in range(depth):
        for left_number in range(depth, depth - line - 1, -1):
            print(left_number, end='')
        point_count = 2 * (depth - line - 1)
        print('.' * point_count, end='')
        for rignt_number in range(depth - line, depth + 1):
            print(rignt_number, end='')
        print()



task_10_1()
task_10_2()
task_10_3()
task_10_4()
task_10_5()
task_10_6()
task_10_7()
task_10_7_2()
task_10_8()
task_10_8_2()
