def print_arr(array):                                   # вывод поля
    for row in array:
        for elem in row:
            print(elem, end = ' ')
        print()

def player_x(num1, arr):                                  # ход крестиками
    if num1 == 1:
        arr[0][0] = 'X'
    elif num1 == 2:
        arr[0][1] = 'X'
    elif num1 == 3:
        arr[0][2] = 'X'
    elif num1 == 4:
        arr[1][0] = 'X'
    elif num1 == 5:
        arr[1][1] = 'X'
    elif num1 == 6:
        arr[1][2] = 'X'
    elif num1 == 7:
        arr[2][0] = 'X'
    elif num1 == 8:
        arr[2][1] = 'X'
    elif num1 == 9:
        arr[2][2] = 'X'
    return arr

def player_o(num1, arr):                                        # ход ноликами
    if num1 == 1:
        arr[0][0] = 'O'
    elif num1 == 2:
        arr[0][1] = 'O'
    elif num1 == 3:
        arr[0][2] = 'O'
    elif num1 == 4:
        arr[1][0] = 'O'
    elif num1 == 5:
        arr[1][1] = 'O'
    elif num1 == 6:
        arr[1][2] = 'O'
    elif num1 == 7:
        arr[2][0] = 'O'
    elif num1 == 8:
        arr[2][1] = 'O'
    elif num1 == 9:
        arr[2][2] = 'O'
    return arr


def game_x(arr, player_x, print_arr):                              # # Функция ходов крестиками с выводом в консоли
    num1 = int(input('Ход первого игрока: '))
    player_x(num1, arr)
    print_arr(arr)
    return arr
    
def game_o(arr, player_o, print_arr):                              # Функция ходов ноликами с выводом в консоли
    num1 = int(input('Ход второго игрока:'))
    player_o(num1, arr)
    print_arr(arr)
    return arr

def condition(arr, game1, game2, player_x, print_arr, player_o):          # Функция с условиями, при которых побеждают игроки
    hod = 2
    print_arr(arr)
    for i in range(9):
        if arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[0][0] == 'X' and arr[0][1] == 'X' and arr[0][2] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[1][0] == 'X' and arr[1][1] == 'X' and arr[1][2] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[2][0] == 'X' and arr[2][1] == 'X' and arr[2][2] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[0][0] == 'X' and arr[1][0] == 'X' and arr[2][0] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[0][1] == 'X' and arr[1][1] == 'X' and arr[2][1] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[0][2] == 'X' and arr[1][2] == 'X' and arr[2][2] == 'X':   
            print('Победил игрок, который ставил крестики')
            break
        elif arr[0][2] == 'O' and arr[1][1] == 'O' and arr[2][0] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif arr[0][0] == 'O' and arr[0][1] == 'O' and arr[0][2] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif arr[1][0] == 'O' and arr[1][1] == 'O' and arr[1][2] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif arr[2][0] == 'O' and arr[2][1] == 'O' and arr[2][2] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif arr[0][0] == 'O' and arr[1][0] == 'O' and arr[2][0] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif arr[0][1] == 'O' and arr[1][1] == 'O' and arr[2][1] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif arr[0][2] == 'O' and arr[1][2] == 'O' and arr[2][2] == 'O':   
            print('Победил игрок, который ставил нолики')
            break
        elif hod % 2 == 0:   
            game1(arr, player_x, print_arr)
            hod += 1
        else:
            game2(arr, player_o, print_arr)
            hod += 1
            
#########################################################################################################################################

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

num = int(input('Если первый игрок будет играть крестиками, введите "1". А если за нолики, то "2": '))
if num == 1:
    print('Крестики ставит первый игрок')
    condition(arr, game_x, game_o, player_x, print_arr, player_o)

else:
    print('Крестики ставит второй игрок')
    condition(arr, game_o, game_x, player_x, print_arr, player_o)

    
