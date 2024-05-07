
from Repository.ship_grid import Ship_Grid

class ServicesError:
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "ServicesERROR:" + str(self.__msg)

class Services:
    def __init__(self):
        self.__player1_grid = Ship_Grid()
        self.__computer_grid = Ship_Grid()

    def place_ship(self, type, direction, row, col):
        self.__player1_grid.place_ship(type, direction, row, col)

    def delete_ship(self, type, direction, row, col):
        self.__player1_grid.delete_ship(type, direction, row, col)

    def player_board(self):
        return self.__player1_grid.board

    def computer_board(self):
        return self.__computer_grid.board

    def generate_computer_board(self):
        self.__computer_grid.generate_board()

    def set_ship_list(self, corv, destr, frig, cru, bship):
        self.__player1_grid.set_ship_list(corv, destr, frig, cru, bship)