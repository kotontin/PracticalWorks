print('Задача 5-7 - Почта (получает на вход время в часах — число от 0 до 23 — и пишет, можно ли в этот час получить посылку).')

hour = int(input("Введите время в часах: "))

work_hours = (8, 22)
start_work = 8
end_work = 22
lunch_break_hours = [14, 15, 10, 18]

def chat_options():
    print("chat version")
    if hour < 8 or hour >= 22:
        print("Посылку получить нельзя")
    elif hour == 14:
        print("Посылку получить нельзя")
    elif hour == 15:
        print("Посылку получить нельзя")
    elif hour == 10:
        print("Посылку получить нельзя")
    elif hour == 18:
        print("Посылку получить нельзя")
    else:
        print("Можно получить посылку")

def first_option():
    print("first version")   
    if hour >= 8 and hour < 18 and hour != 10 and hour != 11 and hour != 12 and hour != 14 and hour != 15:
      print('Можно получить посылку.')
    else:
      print('Посылку получить нельзя.')
    print()

def other_option():
    print("other version")      
    is_too_late = hour >= end_work
    is_too_early = hour < start_work

    if is_too_early or is_too_late:
        print("Посылку получить нельзя")
    elif hour in lunch_break_hours:
        print("Посылку получить нельзя")
    else:
        print("Можно получить посылку")


if __name__ == '__main__':
    chat_options()
    first_option()
    other_option()
