def task_8_1():
    print('\nЗадача 8-1 - Космическая еда (выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее...)\n')
    buckwheat_start = int(input('Сколько у вас килограммов гречки на старте? '))
    buckwheat_consumption = int(input('Какой месячный расход гречки? '))
    month = int(0)

    for month_buckwheat_consumption in range(
            buckwheat_start - buckwheat_consumption, -1, -buckwheat_consumption):
        month += 1
        print('Через', month, 'у вас останется', month_buckwheat_consumption)
    print()



def task_8_2():
    print('\nЗадача 8-2 - Долги (получает данные о количестве должников, а затем спрашивает у каждого пятого, начиная с нуля, его долг).\n')
    total_debtors = int(input('Сколько всего должников? '))
    total_sum = 0

    for debtors in range(0, total_debtors, 5):
        print(debtors)
        sum = int(input('Сообщите компьютеру сумму вашего долга: '))
        print()
        total_sum += sum
    print('Сумма долга: ', total_sum)



def task_8_3():
    print('\nЗадача 8-3 - Микроволновка (таймер обратного отсчета для микроволновых печей).\n')
    reverse_timer = int(input('Ввведите время разогрева: '))
    
    pause = 0

    for sec in range(reverse_timer, 0, -1):
        print('Микроволновка греет ', reverse_timer - sec)
        print('Осталось ', sec)
        pause = int(input('Если хотите остановить разогрев, введите 1: '))
        if pause == 1:
            print('Ваша еда готова, можете забрать. Прошло секунд: ', reverse_timer - sec)
            break
        if sec == 1:
            print('Микроволновка грела ', reverse_timer)
            print('Ваша еда готова, осторожно горячo!')



def task_8_4():
    print('\nЗадача 8-4 - Среднее на отрезке (среднее арифметическое всех чисел из отрезка [a; b], кратных числу c).\n')
    
    a = int(input('Введите начало отрезка a: '))
    b = int(input('Введите конец отрезка b: '))
    c = int(input('Введите число c для вычисления всех чисел на отрезке [a, b], кратных c: '))
    
    sum, num, count = int(0), int(0), int(0)

    for num in range(a, b):
        if num % c == 0:
            sum += num
            print('Кратное число', num)
            count += 1
            print('Счетчик: ', count)
            print('')
    if b % c == 0:
        arithmetic_mean = int((sum + b) / (count + 1))
        print('Кратное число', b)
        print('Счетчик: ', count + 1)
    else:
        arithmetic_mean = int(sum / count)

    print(f"\nСреднее арифметическое чесел, кратных {c} на отрезке [{a};{b}]: {arithmetic_mean}")



def task_8_5():
    print('\nЗадача 8-5 - Функция (высчитывает f(x) на [a, b], выводит ответ с нужным шагом, начиная с конца).\n')
    
    a = int(input('Введите начало отрезка a: '))
    b = int(input('Введите конец отрезка b: '))
    
    negative_step = int(input('Введите шаг: '))
    num_list = []
    count = int(0)

    for x in range(b, a, -negative_step):
        y = int(x ** 3 + 2 * x ** 2 - 4 * x + 1)
        print('f(', x, ') = ', y)
        num_list.append(x)
        count += 1
    n = len(num_list)

    if a in num_list or (a + negative_step == num_list[n - 1]):
        y = int(a ** 3 + 2 * a ** 2 - 4 * a + 1)
        print('f(', a, ') = ', y)



def task_8_6():
    print('\nЗадача 8-6 - Стипендия (расчёт суммы денег, которую необходимо получить сразу у родителей, чтобы прожить десять месяцев).\n')
    
    educational_grant = int(input('Введите размер стипендии: '))
    expenses = int(input('Введите размер расходов: '))
    months = int(input('Сколько месяцев длится учеба: '))
    sum = int(0)
    
    for i in range(0, months):
        sum += (expenses - educational_grant)
        expenses = expenses + expenses * 0.03
    print('Чтобы хватило денег на жизнь во время обучения, возьмите у родителей: ', sum // 1, 'рублей.')



def task_8_7():
    print('\nЗадача 8-7 - Сумма ряда (вычисление суммы N элементов последовательности по формуле).\n')
    
    N = int(input('Введите N: '))
    P = []
    sumP = 0
    
    for n in range(N):
        P.append((-1) ** n * (1 / 2 ** n))
        sumP = sumP + P[n]
    print('Ряд', P)
    print('Сумма ряда:', sumP)



def task_8_8():
    print('\nЗадача 8-8 - Кинотеатр (верный алгоритм).\n')
    
    boys = int(input('Введите кол-во мальчиков: '))
    girls = int(input('Введите кол-во девочек: '))
    answer = ''

    if (boys >= 2 * girls) or (girls > 2 * boys):
        print('Нет решения.')
    elif boys >= girls:
        k = boys - girls
        for bgb in range(k):
            answer += 'BGB'
        for bg in range(girls - k):
            answer += 'BG'
    else:
        k = girls - boys
        for gbg in range(k):
            answer += 'GBG'
        for gb in range(boys - k):
            answer += 'GB'
    print(answer)



def task_8_8_2():
    print('\nЗадача 8-8 - Кинотеатр (мой алгоритм)\n')
    X = int(input('Введите кол-во девочек: '))
    Y = int(input('Введите кол-во мальчиков: '))
    XY = []

    if (X > 2 * Y) or (Y > 2 * X):
        print('Решить задачу при данных условиях невозможно.')
    else:
        for i in range(X + Y):
            while X > 0 and Y > 0:
                if X > 0:
                    XY.append('X')
                    X -= 1
                if Y > 0:
                    XY.append('Y')
                    Y -= 1
                if X > Y:
                    XY.append('X')
                    X -= 1
                if Y > X:
                    XY.append('Y')
                    Y -= 1
    if XY[len(XY) - 2] == XY[len(XY) - 1]:
        last_item = XY.pop(len(XY) - 1)
        XY.insert(0, last_item)

    print('Последовательность списком: ', XY)
    XY_str = "".join(XY)
    print('Последовательность строкой: ', XY_str)
    print('Кол-во элементов: ', len(XY))



task_8_1()
task_8_2()
task_8_3()
task_8_4()
task_8_5()
task_8_6()
task_8_7()
task_8_8()
task_8_8_2()
