def task_2_1():
    print('\nЗадача 2-1 - Пропавшая переменная\n')
    client = 'Петя'
    print(client)
    print(' и ')
    pet = 'Кот'
    print(pet)


def task_2_2():
    print('\nЗадача 2-2 - Цвета\n')
    r = 'Red'
    g = 'Green'
    b = 'Blue'
    print(r, b, g, r + g + b, b, g + b)
    print()


def task_2_3():
    print('\nЗадача 2-3 - Животные\n')
    hare = 'Заяц'
    turtle = 'Черепаха'
    print(hare, 'спит,' ,turtle, 'идет')
    print()


def task_2_4():
    print('\nЗадача 2-4 - Информация о пользователе\n')
    first_name = input('Введите имя пользователя: ')
    if first_name == 'Роман' :
        greeting = 'Привет, '
        print(greeting, first_name)
        intro = "К сожалению, у Вас нет доступа к системе."
        info = "Пожалуйста, обратитесь к системному администратору."
        print(intro)
        print(info)
    else:
        error = 'Вы не Роман!'
        print(error)


def task_2_5():
    print('\nЗадача 2-5 - Вход в систему\n')
    start_position = input('Введите город вылета: ')
    end_position = input('Введите город прилета: ')
    print(start_position + ' - ' + end_position)


def task_2_6():
    print('\nЗадача 2-6 - Полёт\n')
    a = input('Введите первое слово: ')
    b = input('Введите второе слово: ')
    print(a, b)
    a, b = b, a
    print(a, b)



def task_2_7():
    print('\nЗадача 2-7 - Путь к файлу\n')
    user_name = input('Введите имя пользователя: ')
    file_name = input('Введите название файла: ')
    print('C:/' + user_name + '/docs/folder/' + file_name + '.txt')



task_2_1()
task_2_2()
task_2_3()
task_2_4()
task_2_5()
task_2_6()
task_2_7()
