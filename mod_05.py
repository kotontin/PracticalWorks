def task_5_1():
    print('\nЗадача 5-1 - Калькулятор опыта\n')
    experience = int(input('Введите кол-вол очков опыта: '))
    if (experience >= 1000) and (experience < 2500):
        level = 2
    elif (experience >= 2500) and (experience < 5000):
        level = 3
    elif (experience >= 5000):
        level = 4
    else:
        level = 1
    print('Уровень персонажа', level)


def task_5_2():
    print('\nЗадача 5-2 - Функция\n')
    x = int(input('Введите значение аргумента х:'))
    if x > 0:
        y = x - 12
    elif x < 0:
        y = x ** 2
    else:
        y = 5
    print('Значение функции y(х) =', y)


def task_5_3():
    print('\nЗадача 5-3 - Поступление\n')
    num = int(input('Введите место студента в списке: '))
    if (num <= 10):
        print('Студент поступил')
        point = int(input('Введите кол-во его баллов: '))
        if point >= 290:
            print('Студент будет получать стипендию')
        else:
            print('Студент не будет получать стипендию')
    else:
        print('Студент не поступил.')


def task_5_4():
    print('\nЗадача 5-4 - Опять двойка\n')
    rating = int(input('Что получил по математике? '))
    if (rating == 2) or (rating == 3):
        print('Плохо. Марш учиться!')
    elif (rating == 4) or (rating == 5):
        print('Молодец! Можешь отдохнуть.')
    else:
        print('Такой оценки не бывает!')


def task_5_5():
    print('\nЗадача 5-5 - Вася хочет выигрывать\n')
    num1 = int(input('Введите 1-е число: '))
    num2 = int(input('Введите 2-е число: '))
    num3 = int(input('Введите 3-е число: '))
    if (num1 == num2) and (num1 == num3):
        print('3')
    elif (num1 == num2) or (num1 == num3) or (num2 == num3):
        print('2')
    else:
        print('0')


def task_5_6():
    print('\nЗадача 5-6 - Новоселье\n')
    price = int(input('Введите стоимость квартиры, млн. руб: '))
    square = int(input('Введите площадь квартиры, м^2: '))
    if (square >= 100 and price <= 10) or (square >= 80 and price <= 7):
        print('Квартира подходит.')
    else:
        print('Квартира не подходит.')


def task_5_7():
    print('\nЗадача 5-7 - Почта\n')
    time = int(input('Введите время, ч: '))

    if (8 >= time < 10) or (12 >= time < 14) or (15 >= time < 18) or (20 >= time < 22):
        print("Можно получить посылку.")
    else:
        print('Посылку получить нельзя.')


def task_5_7_2():
    print('\nЗадача 5-7 - Почта (второй вариант решения)\n')
    time = int(input('Введите время, ч: '))

    if not (8 <= time < 22) or (10 <= time <= 12) or (14 <= time <= 15) or (18 <= time <= 20):
       print("Посылку получить нельзя.")
    else:
       print('Можно получить посылку.')


task_5_1()
task_5_2()
task_5_3()
task_5_4()
task_5_5()
task_5_6()
task_5_7()
task_5_7_2()
