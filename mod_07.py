def task_7_1():
    print('\nЗадача 7-1 - Должники (при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными).\n')
    count = 0
    for i in range(10):
        number = int(input('Введите число: '))
        if number % 2 == 0 and number > 0:
            count += 1
    print('Четных и положительных чисел: ', count)



def task_7_2():
    print('\nЗадача 7-2 - Посчитай чужую зарплату... (принимает от пользователя зарплату сотрудника за каждый из 12 месяцев и выводит на экран среднюю зарплату за год).\n')
    medium_salary = 0
    for i in range(12):
        print('Введите зарплату за: ', i + 1, '-й месяц: ')
        salary = int(input())
        medium_salary += salary
    medium_salary /= 12
    print()
    print('Средняя зарплата за 12 месяцев: ', medium_salary)


def task_7_3():
    print('\nЗадача 7-3 - Факториал\n')
    my_factorial = 1
    n = int(input('Введите число: '))
    import math
    math_factor = math.factorial(n)
    print('Проверка модулем: ', n, '! = ', math_factor)
    for i in range(1, n):
        my_factorial = n * my_factorial
        n -= 1
    print('Мой алгоритм: n! = ', my_factorial)



def task_7_4():
    print('\nЗадача 7-4 - Успеваемость в классе (вводим 3, 4 или 5, и считаем, каких чисел больше).\n')
    string_mark = input('Введите оценки учеников подряд без разделителей: ')
    
    list_mark = []
    flag = False
    
    for i in string_mark:
        i = int(i)
        list_mark.append(i)
        if i != 3 and i != 4 and i != 5:
            flag = True
    if flag is True:
        print('В классе не должно быть учеников с отметками, отличными от 3, 4 или 5. Поэтому их мы не засчитываем.')
   
    normal = list_mark.count(3)
    good = list_mark.count(4)
    excellent = list_mark.count(5)
    
    if normal > good and normal > excellent:
        print('Сегодня больше всего троешников, их', normal)
    elif good > normal and good > excellent:
        print('Сегодня больше всего хорошистов: их', good)
    elif excellent > normal and excellent > good:
        print('Сегодня больше всего отличников: их', excellent)
    elif normal == good and good == excellent:
        print('Сегодня всех по', normal)
    else:
        if normal == good:
            print('Троешников и хорошистов по', normal)
        elif normal == excellent:
            print('Троешников и отличников по', normal)
        else:
            print('Хорошистов и отличников по', good)
   
    print('Подробно:')
    print('Сегодня получили оценки', n, 'учеников.')
    list_mark.sort()
    print(list_mark)
    print('Троешников: ', list_mark.count(3))
    print('Хорошистов: ', list_mark.count(4))
    print('Отличников: ', list_mark.count(5))



def task_7_4_2():
    print('Задача 7-4 (2) - Успеваемость в классе (альтернативное решение).')
    string = input('Введите оценки учеников подряд без разделителей: ')
    
    n = len(string)
    list_mark = []
    flag = False
    
    for i in range (0,n):
        list_mark.insert(i, string[i])
        if int(string[i]) != 3 and int(string[i]) != 4 and int(string[i]) != 5:
            flag = True
    if flag is True:
        print('В классе не должно быть учеников с отметками, отличными от 3, 4 или 5. Поэтому их мы не засчитываем.')
        
    normal = list_mark.count('3')
    good = list_mark.count('4')
    excellent = list_mark.count('5')
    
    if normal > good and normal > excellent:
        print('Сегодня больше всего троешников, их', normal)
    elif good > normal and good > excellent:
        print('Сегодня больше всего хорошистов: их', good)
    elif excellent > normal and excellent > good:
        print('Сегодня больше всего отличников: их', excellent)
    elif normal == good and good == excellent:
        print('Сегодня всех по', normal)
    else:
        if normal == good:
            print('Троешников и хорошистов по', normal)
        elif normal == excellent:
            print('Троешников и отличников по', normal)
        else:
            print('Хорошистов и отличников по', good)
            
    print('Подробно:')
    print('Сегодня получили оценки', n,'учеников.')
    list_mark.sort()
    print(list_mark)
    print('Троешников: ', list_mark.count('3'))
    print('Хорошистов: ', list_mark.count('4'))
    print('Отличников: ', list_mark.count('5'))



def task_7_5():
    print('\nЗадача 7-5 - Отрезок (среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3).\n')
    
    a = int(input('Введите начало отрезка: '))
    b = int(input('Введите конец отрезка: '))
    multiple_three, count = 0, 0
    
    for n in range(a, b + 1):
        if n % 3 == 0:
            multiple_three += n
            count += 1
    print('Среднее арифметическое чисел, кратных трем на данном отрезке: ', multiple_three / count)



def task_7_6():
    print('\nЗадача 7-6 - Замечательные числа (находит и выводит все двузначные числа, равные утроенному произведению своих цифр).\n')
    for n in range(10, 100):
        if n == (n // 10) * (n % 10) * 3:
            print(n)



def task_7_7():
    print('\nЗадача 7-7 - Пропавшая карточка (найти потерянную карточку с номерами от 1 до N, если номера оставшихся известны).\n')
    string_card = input('Введите через запятую без пробела номера оставшихся карточек: ')
    sum_available_cards = int(0)
    sum_all_card = int(0)
    list_card = []
    list_card = string_card.split(',')
    available_cards = int(len(list_card))
    for i in range(0, available_cards):
        i = int(i)
        sum_available_cards += int(list_card[i])
    for i in range(1, available_cards + 2):
        sum_all_card += i
    print('Потерянная карточка имеет номинал: ', int(sum_all_card - sum_available_cards))



task_7_1()
task_7_2()
task_7_3()
task_7_4()
task_7_4_2()
task_7_5()
task_7_6()
task_7_7()
