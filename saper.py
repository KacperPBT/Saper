from random import randrange

def array_printer(array:list):
    cols = len(array)
    for i in range(cols):
        print(array[i])
# draft = [[0, 0, 0, 0, 1, 9, 1, 0, 0],[1, 1, 1, 0, 1, 1, 1, 0, 0],[1, 9, 1, 0, 1, 1, 1, 0, 0],[1, 1, 1, 0, 1, 9, 1, 0, 0],[0, 0, 0, 0, 1, 2, 2, 1, 0],[0, 1, 1, 2, 1, 2, 9, 1, 0],[1, 2, 9, 4, 9, 4, 2, 2, 0],[1, 9, 3, 9, 9, 3, 9, 1, 0],[1, 1, 2, 2, 2, 2, 1, 1, 0]]

class Saper_draft:
    def __init__(self, field_size : tuple|int, bombs_number : int) -> None:
        if type(field_size) == int:
            field_size = (field_size,field_size)
        if field_size[0] * field_size[1] - bombs_number < 1:
            raise ValueError("Too many bombs, they won't fit in field of this size")
        self.field_size = field_size
        self.bombs_number = bombs_number

    def array_filler(self, filer, size : tuple = None) -> list:
        array = []
        if size == None:
            for i in range(self.field_size[0]):
                sub_array = []
                for j in range(self.field_size[1]):
                    sub_array.append(filer)
                array.append(sub_array)
            return array
        else:
            for i in range(size[0]):
                sub_array = []
                for j in range(size[1]):
                    sub_array.append(filer)
                array.append(sub_array)
            return array


    def rand_bomb_locat(self, field : list) -> list:
        self.bomb_cordinants = self.array_filler(0, (self.bombs_number,2))
        for i in range(self.bombs_number):
            while True:
                x = randrange(self.field_size[0])
                y = randrange(self.field_size[1])
                if field[x][y] == 0:
                    break
            field[x][y] = 9
            self.bomb_cordinants[i][0] = x
            self.bomb_cordinants[i][1] = y
        return field

    def bomb_suraunding(self, field : list) -> list:
        for i in range(self.field_size[0]):
            for j in range(self.field_size[1]):
                if field[i][j] == 9:
                    for k in range(8):
                        h = [[i-1,j+1],[i,j+1],[i+1,j+1],[i-1,j],[i+1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
                        x = h[k][0]
                        y = h[k][1]
                        if x >=0 and x < self.field_size[0] and y>=0 and y < self.field_size[1]:
                            if field[x][y] != 9:
                                field[x][y] = field[x][y] + 1
        return field

    def make_draft(self):
        field = self.array_filler(0)
        field = self.rand_bomb_locat(field)
        self.field = self.bomb_suraunding(field)
        return self.field
    
class Saper_game:
    def __init__(self, boomb_draft : list) -> None:
        self.boomb_draft = boomb_draft
        
