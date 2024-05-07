import random
#TODO: IMPLEMENTATION SEEMS TO BE WORKING PRETTY WELL,
# requires a bit more work to append to current services/repo
from Domain.Ship import Ship

class GridError:
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Grid ERROR: " + str(self.__msg)

class Ship_Grid():

    def __init__(self):
        self.EMPTY = '.'
        self.HEAD = ("<", ">", "^", "v")
        self.FULL = '#'
        self.ENGINE = 'x'
        self.HITEMPTY = '0'
        self.HITSHIP = '*'

        self.board = [] #board
        self.ships = [] #shiplist

        self.DIRECTIONS = (
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Up
        (-1, 0), # Down
        )

        self.available_ships = [5, 4, 3, 2, 1] #available ships in order: corv, destr, frigs, cruis, bships
        self.MIN_SIZE = 2 #used when randomly generating board
        self.MAX_SIZE = 6 # used when randomly generating board

        self.board_size = 10
        self.__initialize_board()

    @property
    def list_grid(self):
        return self.board

    @property
    def list_ships(self):
        return self.ships

    def type_to_size(self, type : str):
        """
        Takes the string in type and returns the size of the ship
        :param type: type of ship(str)
        :return: ship size
        """
        shiptypes = (
            "corvette", "destroyer", "frigate", "cruiser", "battleship"
        )
        ship_size = shiptypes.index(type) + 2
        return ship_size

    def direction_destringer(self, direction : str):
        if direction == "l" or direction == "left":
            truedirection = self.DIRECTIONS[0]
        elif direction == "r" or direction == "right":
            truedirection = self.DIRECTIONS[1]
        elif direction == "u" or direction == "up":
            truedirection = self.DIRECTIONS[2]
        elif direction == "d" or direction == "down":
            truedirection = self.DIRECTIONS[3]
        else:
            return 0
        return truedirection

    def armament_decider(self, ship_size):
        macrocannons = 0
        lances = 0
        if ship_size <= 4:
            macrocannons = 1
        elif ship_size == 5:
            macrocannons = 2
        else:
            macrocannons = 2
            lances = 1
        return (macrocannons, lances)

    def __initialize_board(self):
        """
        Initializes board with empty character and empties ship list
        :return:
        """
        self.board = [[self.EMPTY] * self.board_size for _ in range(self.board_size)]
        self.ships = []

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print("\n\n")

    def generate_board(self, board_size, n_ships):
        """
        Randomly generates board, placing the ships down in random directions and locations
        :param board_size: size of playboard
        :param n_ships: number of ships in fleet
        :return: updated board, updated ship list
        """
        # A board without ship information is ambiguous so return both.
        self.board = [[self.EMPTY] * board_size for _ in range(board_size)]
        ships = []
        while len(ships) < n_ships:
            row = random.randint(0, board_size - 1)
            col = random.randint(0, board_size - 1)
            direction = random.choice(self.DIRECTIONS)
            type = random.randint(0, 4)
            ship_size = type + 2
            if self.available_ships[type] != 0:
                cells = self.generate_ship(self.board, row, col, ship_size, direction)
                if cells:
                    macrocannons, lances = self.armament_decider(ship_size)
                    ship = self.create_ship(cells, direction, ship_size, macrocannons, lances)
                    ships.append(ship)
                    self.draw_ship_on_board(cells, direction, ship_size, type)
        return (self.board, ships)

    def place_ship(self, type : str, direction, row, col):
        """
        Adds ship to board and to the ship list
        :param type: ship type (str)
        :param direction: direction ship faces
        :param row: xcoordinate
        :param col: ycoordinate
        :return:
        """
        ship_size = self.type_to_size(type)
        direction = self.direction_destringer(direction)
        cells = self.generate_ship(self.board, row, col, ship_size, direction)
        if cells:
            macrocannons, lances = self.armament_decider(ship_size)
            ship = self.create_ship(cells, direction, ship_size, macrocannons, lances)
            self.ships.append(ship)
            typeindex = ship_size - 2
            self.draw_ship_on_board(cells, direction, ship_size, typeindex)
        else:
            print(GridError("Invalid ship data!"))
            raise Exception #todo: handle

    def delete_ship(self, type, direction, row, col):
        """
        Deletes a ship from the board
        :param type: ship type
        :param direction: direction ship faces
        :param row: row of head
        :param col: col of head
        :return:
        """
        ship_size = self.type_to_size(type)
        direction = self.direction_destringer(direction)
        found = 0
        for ship in self.ships:
            """print("headz: ", ship.head_row, row)
            print(ship.head_col, col)
            print("directionz: ", ship.direction, direction)
            print("sizez: ", ship.size, ship_size)
            print("")"""
            if ship.head_row == row and ship.head_col == col and ship.direction == direction and ship.size == ship_size:
                found = 1
                break
        if found == 1:
            shipindex = self.ships.index(ship)
            self.ships.pop(shipindex)
            for r, c in ship.cells:
                self.board[r][c] = self.EMPTY
            self.available_ships[ship.size-2] += 1
        else:
            print(GridError("Invalid ship position!"))
            raise Exception # todo: handle



    def draw_ship_on_board(self, cells, direction, ship_size, typeindex):
        """
        Just draws the ship on board with the available information given from params. It does not
        check any conditions.
        :param cells: cells the ship occupies
        :param direction: direction the ships faces
        :param ship_size: ship size
        :param typeindex: ship's type index
        """
        headplaced = False
        for r, c in cells:
            if headplaced == False:
                if self.DIRECTIONS.index(direction) == 0:
                    self.board[r][c] = self.HEAD[0]
                    headplaced = True
                elif self.DIRECTIONS.index(direction) == 1:
                    self.board[r][c] = self.HEAD[1]
                    headplaced = True
                elif self.DIRECTIONS.index(direction) == 2:
                    self.board[r][c] = self.HEAD[2]
                    headplaced = True
                elif self.DIRECTIONS.index(direction) == 3:
                    self.board[r][c] = self.HEAD[3]
                    headplaced = True
            elif ship_size == 1:
                self.board[r][c] = self.ENGINE
            else:
                self.board[r][c] = self.FULL
            ship_size -= 1
        self.available_ships[typeindex] -= 1

    def create_ship(self, cells, direction, size, macrocannons, lances):
        """
        Creates a ship object and returns it
        :param cells: cells occupied by ship
        :param size: size
        :param macrocannons: num of macrocannon weapons
        :param lances: num of lance weapons
        :return: ship object
        """
        ship = Ship(cells, direction, size, macrocannons, lances)
        return ship

    def generate_ship(self, board, row, col, ship_size, direction):
        """
        Checks if the ship can be placed down in given location and returns a list with the cells
        occupied by the ship if empty.
        :param board: board
        :param row: row of ship
        :param col: col of ship
        :param ship_size: size of ship
        :param direction: direction ship faces
        :return: cell list or None
        """
        r = row
        c = col
        dr, dc = direction
        cells = []
        for _ in range(ship_size):
            if self.is_empty(board, r, c):
                cells.append((r, c))
                r += dr
                c += dc
            else:
                return None
        if ship_size < 5:
            pass
        return cells

    def is_empty(self, board, row, col):
        """
        Checks if cell is empty
        :param board:  board
        :param row: row
        :param col:  col
        :return: True or False
        """
        try:
            return min(row, col) >= 0 and board[row][col] == self.EMPTY
        except IndexError:
            pass
        return False