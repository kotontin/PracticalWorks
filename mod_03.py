def task_3_1():
    print('\nЗадача 3-1 - Язык математики\n')
    a = 8
    b = 10
    c = 12
    d = 18
    res = ((-3 + a ** 2) * b - 2 ** 3) / (c - 2 * d)
    print(res)


def task_3_2():
    print('\nЗадача 3-2 - Финансовый отчёт\n')
    quarter1 = int(input('Введите доход за первый квартал: '))
    quarter2 = int(input('Введите доход за второй квартал: '))
    quarter3 = int(input('Введите доход за третий квартал: '))
    quarter4 = int(input('Введите доход за четвертый квартал: '))
    dinamika = (quarter1 + quarter2) / (quarter3 + quarter4)
    print('Динамика роста:', dinamika)


def task_3_3():
    print('\nЗадача 3-3 - Следующее и предыдущее числа\n')
    number = int(input('Введите число: '))
    print('После числа', number, 'идет число', number + 1)
    print('До числа', number, 'идет число', number - 1)


def task_3_4():
    print('\nЗадача 3-4 - Площадь треугольника\n')
    katet1 = int(input('Введите длину первого катета: '))
    katet2 = int(input('Введите длину второго катета: '))
    print('Площадь прямоугольного треугольника равна', (katet1 * katet2) / 2)


def task_3_5():
    print('\nЗадача 3-5 - Часы\n')
    min = int(input('Введите кол-во минут: '))
    print('Часов в минутах', min // 60)
    print('Минут останется', min % 60)


def task_3_6():
    print('\nЗадача 3-6 - Проверяем бухгалтера\n')
    num1 = int(input('1-е число: '))
    num2 = int(input('2-е число: '))
    last1 = num1 % 100
    last2 = num2 % 100
    answer = last1 + last2
    print(("1-й остаток: "), last1)
    print(("2-й остаток: "), last2)
    print(("Ответ: "), answer)
    num1 = str(num1)
    a = num1[0]
    b = num1[1]
    c = num1[2]
    d = num1[3]
    print(f"Строка из цифр: {d + c + b + a}")
    print(f"Сумма цифр: {int(a) + int(b) + int(c) + int(d)}")


def task_3_7():
    print('\nЗадача 3-7 - Режем число на части\n')
    number = (input('Введите четырехзначное число: '))
    for i in range(len(number)):
        print(number[i])


def task_3_8():
    print('\nЗадача 3-8 - Поменять местами: не всё так просто!\n')
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(a, b)
    a = a + b
    b = a - b
    a = a - b
    print(a, b)


task_3_1()
task_3_2()
task_3_3()
task_3_4()
task_3_5()
task_3_6()
task_3_7()
task_3_8()
