print('\nЗадача 10-5 - Наибольшая сумма цифр (среди введенных натуральных чисел, найдите наибольшее по сумме цифр).\n')

Sequence = input('Введите последовательность чисел через запятую и/или пробел: ')
ListSequence = []

if Sequence.find(', '):
    ListSequence = Sequence.split(', ')
elif Sequence.find(','):
    ListSequence = Sequence.split(',')
elif Sequence.find(' '):
    ListSequence = Sequence.split(' ')

SumElements = 0
ListSumElements = []

for elem in ListSequence:
    elem = int(elem)
    while elem > 0:
        SumElements += elem % 10
        elem = elem // 10
    ListSumElements.append(SumElements)
    SumElements = 0

#print('Заданная последовательность: ', ListSequence)
#print('Последовательность сумм цифр', ListSumElements)
#print('Максимальная сумма цифр: ', max(ListSumElements))
#print('Индекс числа с максимальной суммой цифр: ', ListSumElements.index(max(ListSumElements)))
#print('Заданной число с этим индексом', ListSequence[ListSumElements.index(max(ListSumElements))])

print(f"Максимальная сумма цифр в последовательности чисел: {max(ListSumElements)}, число: {ListSequence[ListSumElements.index(max(ListSumElements))]}")

