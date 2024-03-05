from random import randrange

def array_printer(array:list):
    cols = len(array)
    for i in range(cols):
        print(array[i])
# draft = [[0, 0, 0, 0, 1, 9, 1, 0, 0],[1, 1, 1, 0, 1, 1, 1, 0, 0],[1, 9, 1, 0, 1, 1, 1, 0, 0],[1, 1, 1, 0, 1, 9, 1, 0, 0],[0, 0, 0, 0, 1, 2, 2, 1, 0],[0, 1, 1, 2, 1, 2, 9, 1, 0],[1, 2, 9, 4, 9, 4, 2, 2, 0],[1, 9, 3, 9, 9, 3, 9, 1, 0],[1, 1, 2, 2, 2, 2, 1, 1, 0]]

class Saper_draft:
    def __init__(self, field_size : int, bombs_number : int) -> None:
        if field_size * field_size - bombs_number < 1:
            raise ValueError("Too many bombs, they won't fit in field of this size")
        self.field_size = field_size
        self.bombs_number = bombs_number

    def array_filler(self, filer) -> list:
        array = []
        for i in range(self.field_size):
            sub_array = []
            for j in range(self.field_size):
                sub_array.append(filer)
            array.append(sub_array)
        return array

    def rand_bomb_locat(self, field : list) -> list:
        for i in range(self.bombs_number):
            while True:
                x = randrange(self.field_size)
                y = randrange(self.field_size)
                if field[x][y] == 0:
                    break
            field[x][y] = 9
        return field

    def bomb_suraunding(self, field : list) -> list:
        for i in range(self.field_size):
            for j in range(self.field_size):
                if field[i][j] == 9:
                    for k in range(8):
                        h = [[i-1,j+1],[i,j+1],[i+1,j+1],[i-1,j],[i+1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
                        x = h[k][0]
                        y = h[k][1]
                        if x >=0 and x < 9 and y>=0 and y < 9:
                            if field[x][y] != 9:
                                field[x][y] = field[x][y] + 1
        return field

    def make_draft(self):
        field = self.array_filler(0)
        field = self.rand_bomb_locat(field)
        self.field = self.bomb_suraunding(field)
        return self.field
