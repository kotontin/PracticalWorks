print('\n', '-' * 8 + ' З А Д А Ч И   П О Д   В И Д Е О ' + '-' * 8, '\n')

def mod_9_video_2_2():
    print('\nЗадача v9-2 - Начальник\n')
    answer = ''

    while answer != 'Да, конечно, сделал':
        print('Выполнена ли задача?')
        answer = input()


def mod_9_video_2_3():
    print('\nЗадача v9-3 - Купи слона\n')
    user_name = input('Как тебя зовут? ')
    print(f"{user_name}, купи слона!")

    while True:
        some_phrase = input()
        print(f"Все говорят {some_phrase}, а ты купи слона!")


def mod_9_video_3_1():
    word = 'Python!'
    count = 0

    for symbol in Word:
        print(word[count] * 3)
        count += 1


def mod_9_video_3_3():
    phrase = input('Введите текст: \n')
    count_small_Letters, count_big_letters = 0, 0

    for symbol in phrase:
        if symbol == 'ы':
            count_small_letters += 1
        elif symbol == 'Ы':
            count_big_letters += 1

    print(f"\nМаленьких букв ы - {count_small_letters}, больших букв Ы - {count_big_letters}.\n")


def mod_9_video_4_1():
    print('-' * 12)
    for i in range(3):
        print('|', '0' * 8, '|')
    print('-' * 12)


def mod_9_video_4_2():
    number = int(input('Введите число: '))
    step = int(input('Введите шаг: '))
    summ = 0

    for count in range(0, 3):
        summ += number
        print(number, end = '.')
        number += step
    print(summ)


def mod_9_video_4_3():
    number = int(input('Введите число: '))

    for count in range(0, number + 10, 10):
        print('-=-', count, end=' ')
    print('-=-')


def mod_9_video_4_4():
    print('\nНаходит две одинаковые буквы подряд.\n')
    string = input('Введите строку: ')
    prev_sym = ''
    equal_sym = False
    for letter in string:
        if prev_sym == letter:
            equal_sym = True
            break
        else:
            prev_sym = letter

    if equal_sym:
        print('Есть две одинаковые буквы, идущие подряд.')
    else:
        print('Нет двух одинаковых букв, идущих подряд.')


mod_9_video_2_2()
mod_9_video_2_3()
mod_9_video_3_1()
mod_9_video_3_3()
mod_9_video_4_1()
mod_9_video_4_2()
mod_9_video_4_3()
mod_9_video_4_4()
