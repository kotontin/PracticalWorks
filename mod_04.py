def task_4_1():
    print('\nЗадача 4-1 - Датчик погоды\n')
    rain = int(input('На улице идёт дождь? Если да, введите 1: '))
    if rain == 1:
        print('Пошёл дождь. Возьмите зонтик!')
    else:
        print('Дождя нет!')


def task_4_2():
    print('\nЗадача 4-2 - Поступление\n')
    discipline1 = int(input('Введите количество баллов по русскому языку: '))
    discipline2 = int(input('Введите количество баллов по математике: '))
    discipline3 = int(input('Введите количество баллов по информатике: '))
    passing_grade = 120
    if discipline1 + discipline2 + discipline3 >= passing_grade:
        print('Поздравляю, ты поступил на бюджет!')
    else:
        print('К сожалению, ты не прошёл на бюджет.')


def task_4_3():
    print('\nЗадача 4-3 - Следим за расписанием\n')
    num = int(input('Какое сегодня число? '))
    if (num % 2) == 0:
        print('Вася, надо работать!')
    else:
        print('Вася, надо отдыхать!')


def task_4_4():
    print('\nЗадача 4-4 - Калькулятор скидки\n')
    chair1 = int(input('Введите стоимость первого стула: '))
    chair2 = int(input('Введите стоимость второго стула: '))
    chair3 = int(input('Введите стоимость третьего стула: '))
    sum = (chair1 + chair2 + chair3)
    print (sum)
    min = 10000
    if sum >= min:
        sale = sum * 10 / 100
        print ('Размер скидки: ', sale)
    else:
        print ('Сумма покупки для скидки недостаточная! Докупите еще на', min -sum)


def task_4_5():
    print('\nЗадача 4-5 - Модуль числа\n')
    num = int(input('Введите число: '))
    if num < 0:
        num = -num
    print('Модуль числа:', num)


def task_4_6():
    print('\nЗадача 4-6 - Игра в кубики\n')
    num1 = int(input('Введите баллы владельца: '))
    num2 = int(input('Введите баллы игрока: '))
    if num1 >= num2:
        print('Разница в баллах:', num1 - num2)
        print('Игрок платит')
    else:
        print('Разница в баллах:', num2 - num1)
        print('Владелец платит')
    print('Игра окончена!')


def task_4_7():
    print('\nЗадача 4-7 - Хватит ли зарплаты\n')
    hours = int(input('Количество отработанных часов: '))
    credit = int(input('Остаток по кредиту: '))
    eat = int(input('Сколько нужно денег на еду: '))
    salary = 200 * hours / 2**3 + hours
    print(f"Ваша зарплата: {salary}")
    if salary >= (credit + eat):
        print('Часов хватает. Можно отдохнуть')
    else:
        print('Часов не хватает. Придётся работать еще', round(((credit + eat) - salary) * hours / salary) + 1, 'часов')
    print()


def task_4_8():
    print('\nЗадача 4-8 - Максимальное число\n')
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    num3 = int(input('Введите третье число: '))
    if num1 > num2 and num1 > num3:
        print('Максимальное число: ', num1)
    elif num2 > num1 and num2 > num3:
        print('Максимальное число: ',num2)
    else:
        print('Максимальное число: ',num3)


task_4_1()
task_4_2()
task_4_3()
task_4_4()
task_4_5()
task_4_6()
task_4_7()
task_4_8()
