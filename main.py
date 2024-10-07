from random import randint

secret_number = randint(1,10)
tryes = 3

while tryes > 0:
    user_number = int(input('Попытайтесь угадать число от 1 до 10: '))

    if user_number == secret_number:
        print(f'Вы угадали, загаданное число {secret_number}')
        break

    else:
        tryes -= 1
        print(f'Попытайтесь ещё раз, у вас осталось {tryes} попыток')
        continue
