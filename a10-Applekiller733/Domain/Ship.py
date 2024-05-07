

class Ship:
    def __init__(self, cells, direction, size, macrocannons, lances):
        self.__size = size
        self.__cells = cells
        self.__head_row = cells[0][0]
        self.__head_col = cells[0][1]
        self.__direction = direction

        self.__macrocannons = macrocannons
        self.__lances = lances

        self.__is_dead = False

    @property
    def head_row(self):
        return self.__head_row

    @property
    def head_col(self):
        return self.__head_col

    @property
    def direction(self):
        return self.__direction

    @property
    def size(self):
        return self.__size

    @property
    def cells(self):
        return self.__cells

    @property
    def macrocannons(self):
        return self.__macrocannons

    @property
    def lances(self):
        return self.__lances

    def is_dead(self):
        if self.__is_dead == True:
            return 1
        return 0

    def death(self):
        self.__is_dead = True
