"""
pole 9x9
bomby 5
"""
from datetime import datetime
from random import randrange
NOW = datetime.now()
NOW = NOW.microsecond
def array_printer(array:list):
    cols = len(array)
    for i in range(cols):
        print(array[i])

draft = [[0, 0, 0, 0, 1, 9, 1, 0, 0],[1, 1, 1, 0, 1, 1, 1, 0, 0],[1, 9, 1, 0, 1, 1, 1, 0, 0],[1, 1, 1, 0, 1, 9, 1, 0, 0],[0, 0, 0, 0, 1, 2, 2, 1, 0],[0, 1, 1, 2, 1, 2, 9, 1, 0],[1, 2, 9, 4, 9, 4, 2, 2, 0],[1, 9, 3, 9, 9, 3, 9, 1, 0],[1, 1, 2, 2, 2, 2, 1, 1, 0]]



def array_filler(cols : int, rows : int, filer) -> list:
    array = []
    for i in range(cols):
        sub_array = []
        for j in range(rows):
            sub_array.append(filer)
        array.append(sub_array)
    return array

def rand_bomb_locat(field : list, field_size : int) -> list:
    for i in range(10):
        while True:
            x = randrange(field_size)
            y = randrange(field_size)
            if field[x][y] == 0:
                break
        field[x][y] = 9
    return field

def bomb_suraunding(field : list, field_size : int) -> list:
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == 9:
                for k in range(8):
                    h = [[i-1,j+1],[i,j+1],[i+1,j+1],[i-1,j],[i+1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
                    x = h[k][0]
                    y = h[k][1]
                    if x >=0 and x < 9 and y>=0 and y < 9:
                        if field[x][y] != 9:
                            field[x][y] = field[x][y] + 1
    return field











pole = array_filler(9,9,0)
pole = rand_bomb_locat(pole,9)
pole = bomb_suraunding(pole,9)
array_printer(pole)
hpw = datetime.now()
print(hpw.microsecond-NOW)

print("==============================")
array_printer(draft)