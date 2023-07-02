def task_6_1():
    print('\nЗадача 6-1 - Кубы чисел (возводит в третью степень каждое число от 1 до N и выводит результат на экран).\n')
    N = int(input('Введите N: '))
    count = 1
    while count <= N:
        print(count, '^3 = ', count ** 3)
        count += 1


def task_6_2():
    print('\nЗадача 6-2 - Коллекторы\n')
    debtor = input('Введите имя должника: ')
    indebted = int(input('Введите сумму долга: '))
    print(debtor, ', ваша задолженность составляет', indebted, 'рублей.')
    balance = int(0)
    while balance < indebted:
        balance = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
        if balance < indebted:
            print('Маловато,', debtor, '. Давайте ещё раз.')
        else:
            print('Отлично,', debtor, ', Вы погасили долг. Спасибо!')


def task_6_3():
    print('\nЗадача 6-3 - Слишком большие числа (сколько цифр в числе)\n')
    number = int(input('Введите число: '))
    remnant = int(0)
    count = 0
    n = int(10)
    while remnant != number:
        remnant = int(number) % n
        n = n * 10
        count += 1
    print('Цифр в числе:', count)


def task_6_4():
    print('\nЗадача 6-4 - Поставьте оценку! (находит к-во полож. и отр. чисел в последовательности, которая заканчивается на 0).\n')
    count1 = 0
    count2 = 0

    while True:
        num = int(input('Введите число от -100 до 100 (для выхода намите 0): '))
        if num == 0:
            break
        elif num > 0:
            count1 += 1
        else:
            count2 += 1

    print('Кол-во положительных чисел: ', count1)
    print('Кол-во отрицательных чисел: ', count2)


def task_6_5():
    print('\nЗадача 6-5 - Обычный день на работе (сколько задач выполнил Максим за 8 часов и нужно ли зайти в магазин?)\n')
    print()
    count = 0
    call_check = False
    print('Начался рабочий день.')

    i = 0
    while i < 8:
        i += 1
        print(i, '-й час.')
        task = int(input('Сколько задач решит Максим? '))
        count += task
        call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
        if call == 1:
            call_check = True

    print('Рабочий день закончился. Всего выполнено задач: ', count)

    if call_check == True:
        print('Нужно зайти в магазин.')
    else:
        print('Максим, перезвоните жене!')


def task_6_6():
    print('\nЗадача 6-6 - Вклады (по данным числам X, Y, P определяет, сколько лет пройдёт, прежде чем сумма достигнет значения Y).\n')
    contribution_start = int(input('Введите сумму вклада: '))
    contribution_final = int(input('Введите желаемую сумму: '))

    if contribution_final < contribution_start:
        print('Вам нужно снять деньги в размере', contribution_start - contribution_final)
    else:
        percent = int(input('Введите годовой процент по вкладу от 0 до 100: '))
        count = 1
        while contribution_start <= contribution_final:
            contribution_start = contribution_start + contribution_start * percent / 100
            contribution_start = contribution_start // 1
            print('Через', count, 'лет у вас будет: ', contribution_start)
            count += 1
        print('Нужная сумма в размере', contribution_final, 'руб. наберется через', count - 1, 'лет.')


def task_6_7():
    print('\nЗадача 6-7 - Игра «Угадай число» (запрашивает у пользователя число от 1 до 100 до тех пор, пока он его не отгадает).\n')
    hidden_number = 6
    count = 0

    while True:
        count += 1
        number = int(input('Введите число от 1 до 10: '))
        if number == hidden_number:
            print('Вы угадали! Число попыток: ', count)
            break
        elif number > hidden_number:
            print('Число больше, чем нужно. Попробуйте ещё раз!')
        else:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')


def task_6_8():
    print('\nЗадача 6-8 - Игра «Компьютер угадывает число» (пользователь задумывает натуральное число от 1 до 100, а компьютер угадывает его за 7 попыток.)')
    list_excess = []
    a, b, count = 1, 100, 0

    while True:
        count += 1
        N = (a + b) // 2
        list_excess.append(N)
        print()
        print('N =', N)
        answer = int(input('Твоё число равно(1), больше(2) или меньше(3) N?  '))
        if (answer == 2) and N == 99:
            N += 1
        if answer == 1:
            print()
            print('Я угадал! Это', N)
            print('Использовано попыток:', count)
            print(list_excess)
            break
        elif answer == 2:
            a = N + 1
        elif answer == 3:
            b = N - 1


def task_6_8_2():
    print('\nЗадача 6-8 (2) - Игра «Компьютер угадывает число» (альтернативный вариант решения)')
    count = 0
    sec = int(input('Загадайте число: '))
    mn, mx = 1, 100
    tr, key = 0, 0
    
    while True:
        count += 1
        tr = (mx + mn) // 2
        print('Твое число: 1 - равно, 2 - больше или 3 - меньше, чем число', tr)
        key = int(input('Введите ответ: '))
        if key == 1:
            print('Угадал за', count, 'попыток')
            break
        elif key == 2:
            mn = tr
        elif key == 3:
            mx = tr


task_6_1()
task_6_2()
task_6_3()
task_6_4()
task_6_5()
task_6_6()
task_6_7()
task_6_8()
task_6_8_2()
