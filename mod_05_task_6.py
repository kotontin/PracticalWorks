print('Задача 5-6 - Новоселье ( получает на вход стоимость квартиры и её площадь и выводит сообщение, подходит ли она).')

num1 = int(input('Введите 1-е число: '))
num2 = int(input('Введите 2-е число: '))
num3 = int(input('Введите 3-е число: '))

all_equal = 3
some_equal = 2
not_equal = 0

def foo() -> int:
  is_equal_12 = (num1 == num2)
  is_equal_13 = (num1 == num3)
  is_equal_23 = (num2 == num3)

  if is_equal_12 and is_equal_13:
    return all_equal
  elif is_equal_12 or is_equal_13 or is_equal_23:
    return some_equal
  else:
    return not_equal

def main(inputs: list[int]) -> int:
  set_inputs = set(inputs)

  if len(set_inputs) == 1:
    return all_equal
  elif len(set_inputs) == 3:
    return not_equal
  else:
    return some_equal


if __name__ == '__main__':
  result_foo = foo()
  result_main = main([num1, num2, num3])

  print(result_foo)
  print(result_main)
  assert result_foo == result_main
