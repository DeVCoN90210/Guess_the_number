import random

number = random.randint(1, 100)

while True:
    user_number = int(input('Введите число '))
    if number == user_number:
        print('Победа!!!')
        break
    elif number < user_number:
        print('Число больше загаданного.')
    else:
        print('Число меньше загаданного.')