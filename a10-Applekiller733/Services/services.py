import random
import unittest
from Repository.ship_grid import Ship_Grid
from Repository.hit_grid import Hit_Grid

class ServicesError:
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "ServicesERROR:" + str(self.__msg)



class Services:
    def __init__(self):
        self.__player1_grid = Ship_Grid()
        self.__computer_grid = Ship_Grid()

        self.__player1_hits = Hit_Grid()
        self.__computer_hits = Hit_Grid()

        self.generate_computer_board()

    def macrocannon_tuple(self):
        """ mainly used by ui to determine weapontype being fired by command"""
        macrocannontuple = (
            "m", "M", "macro", "Macro", "macrocannon", "Macrocannon", "MACROCANNON", "MACRO"
        )
        return macrocannontuple

    def lance_tuple(self):
        """ mainly used by ui to determine weapontype being fired by command"""
        lancetuple = (
            "l", "L", "lance", "Lance", "LANCE", "lan", "LAN", "Lan"
        )
        return lancetuple

    def place_ship(self, type, direction, row, col):
        """
        Places ship on ship board
        :param type: type
        :param direction: direction ship faces
        :param row: row
        :param col: column
        :return:
        """
        self.__player1_grid.place_ship(type, direction, row, col)

    def delete_ship(self, type, direction, row, col):
        """
        Deletes ship given by params
        :param type: type of ship
        :param direction: direction ship faces
        :param row: row
        :param col: column
        """
        self.__player1_grid.delete_ship(type, direction, row, col)

    def player_board(self):
        """

        :return: player ship board
        """
        return self.__player1_grid.board

    def player_hitsboard(self):
        """

        :return: player's hits board
        """
        return self.__player1_hits.hit_board

    def player_addhit(self, row, col):
        """
        Adds hit to player hitboard
        :param row: row
        :param col: column
        """
        self.__player1_hits.add_hit(row, col)

    def computer_addhit(self, row, col):
        """
        Adds hit to computer hitboard
        :param row: row
        :param col: col
        :return:
        """
        self.__computer_hits.add_hit(row, col)
    def player_available_ships(self):
        """

        :return: number of to-be-placed ships
        """
        return self.__player1_grid.available_ships

    def computer_board(self):
        """

        :return:  computer ship board
        """
        return self.__computer_grid.board

    def computer_hitsboard(self):
        """
        :return: computer hit board
        """
        return self.__computer_hits.hit_board

    def generate_player_board(self):
        """
        Randomly generates player board
        :return:
        """
        self.__player1_grid.generate_board()

    def generate_computer_board(self):
        """
        Randomly generates computer board
        :return:
        """
        self.__computer_grid.generate_board()

    def set_ship_list(self, corv, destr, frig, cru, bship):
        """
        Sets the available ship list to something else. Generally used at 'character creation'.
        If game ever gets expanded, could be used to update available fleet list after engagements or
        choice events.
        :param corv: num of corvettes
        :param destr: num of destroyers
        :param frig: num of frigates
        :param cru: num of cruisers
        :param bship: num of battleships
        """
        self.__player1_grid.set_ship_list(corv, destr, frig, cru, bship)

    def reset_player_board(self):
        self.__player1_grid.initialize_board()
        self.__player1_grid.available_ships = self.__player1_grid.available_ships_copy.copy()

    def no_more_ships(self):
        """
        :return: 0 if player still has ships to be placed, 1 if not
        """
        for num in self.player_available_ships():
            if num != 0:
                return 0
        return 1

    def board_size(self):
        """
        :return: board size the game is played on. Player board used as refference
        """
        return self.__player1_grid.board_size

    def player_total_armament(self):
        """
        :return: player's total available armament
        """
        return self.__player1_grid.total_armament()

    def computer_total_armament(self):
        """
        :return: computer total available armament
        """
        return self.__computer_grid.total_armament()

    def player_alive_ships(self):
        """
        :return: num of alive ships in player board
        """
        return self.__player1_grid.alive_ships()

    def computer_alive_ships(self):
        """
        :return: num of alive ships in computer board
        """
        return self.__computer_grid.alive_ships()

    def computer_turn(self):
        computer_armament = self.computer_total_armament()
        while computer_armament[0] != 0 or computer_armament[1] != 0:
            while computer_armament[0] != 0:
                x = random.randint(0, self.board_size())
                y = random.randint(0, self.board_size())
                self.computer_addhit(x, y)
                computer_armament[0] -= 1
            while computer_armament[1] != 0:
                startx = random.randint(0, self.board_size())
                starty = random.randint(0, self.board_size())
                x2 = random.choice((-1, 1, 0)) + startx
                y2 = random.choice((-1, 1, 0)) + starty
                x3 = random.choice((-1, 1, 0)) + x2
                y3 = random.choice((-1, 1, 0)) + y2
                self.computer_addhit(startx, starty)
                self.computer_addhit(x2, y2)
                self.computer_addhit(x3, y3)
                computer_armament[1] -= 1


    def end_turn(self):
        """
        Handles the end turn functionality. Checks whether or not the game is won/lost. Checks and updates
        all boards with hits.
        """
        # draw the shots from hitlist and also add them to the opposing player's ship grid
        # verify if computer or player have any ships left alive.
        hitlistplayer = self.__player1_hits.hits_list
        hitlistcomputer = self.__computer_hits.hits_list
        playerboard = self.__player1_grid.board
        computerboard = self.__computer_grid.board
        for hit in hitlistplayer:
            if self.__computer_grid.is_empty(computerboard, hit[0], hit[1]) == 0:
                self.__player1_hits.successful_hits.append(hit)
                self.__player1_hits.draw_hit_on_board(hit[0], hit[1], 1)
                self.__computer_grid.draw_hit_on_board(hit[0], hit[1], 1)
            else:
                self.__player1_hits.empty_hits.append(hit)
                self.__player1_hits.draw_hit_on_board(hit[0], hit[1], 0)
                self.__computer_grid.draw_hit_on_board(hit[0], hit[1], 0)
        hitlistplayer = []

        for hit in hitlistcomputer:
            if self.__player1_grid.is_empty(playerboard, hit[0], hit[1]) == 0:
                self.__computer_hits.successful_hits.append(hit)
                self.__computer_hits.draw_hit_on_board(hit[0], hit[1], 1)
                self.__player1_grid.draw_hit_on_board(hit[0], hit[1], 1)
            else:
                self.__computer_hits.empty_hits.append(hit)
                self.__computer_hits.draw_hit_on_board(hit[0], hit[1], 0)
                self.__player1_grid.draw_hit_on_board(hit[0], hit[1], 0)
        hitlistcomputer = []

        self.__player1_grid.update_alive()
        self.__computer_grid.update_alive()

        playeralive = self.player_alive_ships()
        computeralive = self.computer_alive_ships()
        if playeralive == 0 and computeralive == 0:
            pass #technically impossible draw
        elif playeralive == 0:
            print("The Warp consumes us!")
            quit()
        elif computeralive == 0:
            print("By the Emperor, we've won!")
            quit()
        else:
            pass #game continues



class TestClass(unittest.TestCase):
    #def  __init__(self):
        #super().__init__()
        #self.__testservices = Services()



    def testinit(self):
        testservices = Services()
        shipboard = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
        ]
        self.assertEqual(testservices.player_board(), shipboard)

    def testadd(self):
        testservices = Services()
        shipboard = [
            ["<", "x", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
        ]

        testservices.place_ship("corvette", "l", 0, 0)
        self.assertEqual(testservices.player_board(), shipboard)

#tests = TestClass()
#unittest.main()

"""
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()"""