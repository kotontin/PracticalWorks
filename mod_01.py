def task_1_1():
    print('Задача 1-1 - Приветствие')
    for row in range(8):
        if row == 0 or row == 7:
            print('=' * 30)
        elif row == 3:
            print('||', ' ' * 8, 'Привет', ' ' * 8, '||')
        elif row == 4:
            print('||', ' ' * 8, 'друг!', ' ' * 9, '||')
        else:
            print('||', ' ' * 24, '||')

task_1_1()
