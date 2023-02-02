from random import randint as R

print('На столе 100 конфет. Взять можно не более 28ми конфет за ход. Победит тот, чей ход будет последний.')
num = input('Введите любой символ, чтобы провести жеребьевку')
random_player = R(0,1)
total_candy = 100
if random_player == 0:
    print('Игру начинаете Вы.')
    while total_candy > 0:
        if total_candy > 28:
            num1 = int(input('Введите колличество конфет, которое вы хотите взять: '))
            total_candy -= num1
            print(f'Осталось конфет: {total_candy}')
        else:
            total_candy = 0
            print('Вы победили.')
            break
        
        if total_candy > 57:
            total_candy -= 28
            print(f'Бот забрал 28 конфет. Осталось конфет: {total_candy}')
        elif total_candy <= 57 and total_candy > 28:
            sum = 0
            while total_candy > 28:
                total_candy -= 1
                sum += 1
            print(f'Бот забрал {sum}. Осталось конфет: {total_candy}')
        else:
            total_candy = 0
            print('Вы проиграли')
            break
else:
    print('Игру начинает бот.')
    while total_candy > 0:
        if total_candy > 57:
            total_candy -= 28
            print(f'Бот забрал 28 конфет. Осталось конфет: {total_candy}')
        elif total_candy <= 57 and total_candy > 28:
            sum = 0
            while total_candy > 29:
                total_candy -= 1
                sum += 1
            print(f'Бот забрал {sum}. Осталось конфет: {total_candy}')
        else:
            total_candy = 0
            print('Вы проиграли')
            break

        if total_candy > 28:
            num1 = int(input('Введите колличество конфет, которое вы хотите взять: '))
            total_candy -= num1
            print(f'Осталось конфет: {total_candy}')
        else:
            total_candy = 0
            print('Вы победили.')
            break
