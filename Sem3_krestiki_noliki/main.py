"""Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера.
"""

arr = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player1 = 'X'
player2 = 0

def print_arr(arr):
    for row in arr:
        for col in row:
            print(col, end='  ')
        print()

def move(player):
    flag = False
    while flag == False:
        i = int(input("Выберите строку: ")) - 1
        j = int(input("Выберите столбец: ")) - 1
        if arr[i][j] == '_':
            arr[i][j] = player
            flag = True
            print_arr(arr)
        else:
            print("Этот ход невозможен, повторите ход")
            flag = False

def win_line(arr):
    for i in range(len(arr)):
        if (arr[i][0] == arr[i][1] == arr[i][2] and arr[i][0] != '_') or (arr[0][i] == arr[1][i] == arr[2][i] and arr[0][i] != '_'):
            return True

print_arr(arr)
winner = False
player = player1
count = 0
while winner == False and count < 9:
    print(f"Ходит игрок, играющий за {player}")
    move(player)
    if (arr[0][0] == arr[1][1] == arr[2][2] or
            arr[0][2] == arr[1][1] == arr[2][0]) and arr[1][1] != '_':
        winner = True
    elif win_line(arr) == True:
        winner = True
    else:
        if player == player1:
            player = player2
        else:
            player = player1
    count += 1

if winner == True:
    print(f"Победил игрок, играющий за {player}")
else:
    print("Ничья")