
from colorama import Fore, Style
from Services.services import Services

class UIError:
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "UIERROR: " + str(self.__msg)

class Test:
    def __init__(self):
        #tests
        self.testservices = Services()

        self.testservices.place_ship("corvette", "l", 4, 5)
        assert(self.testservices.player_alive_ships() == 1)

        self.testservices.place_ship("battleship", "r", 0, 1)
        assert(self.testservices.player_alive_ships() == 2)

        self.testservices.delete_ship("corvette", "l", 4, 5)
        assert(self.testservices.player_alive_ships() == 0)

        self.testservices.player_addhit(4, 5)
        assert(self.testservices.player_hitsboard()[4][5] == "!")

        self.testservices.player_addhit(21, 19)
        assert(self.testservices.player_hitsboard()[21][19] == "!")

class Menu:
    def __init__(self):
        self.__services = Services()

    def ui_print_board(self, board):
        board_size = self.__services.board_size()
        for i in range(self.__services.board_size()+1):
            if i != 0:
                print("\t\t\t\t\t" + Fore.YELLOW + str(i-1) + Style.RESET_ALL, end=" ")
            else:
                print("\t\t\t\t\t", end="  ")
            for j in range(self.__services.board_size() + 1):
                if i > 0:
                    if j > 0 :
                        print(board[i-1][j-1], end=" ")
                elif i == 0:
                        if j != 0:
                            print(Fore.YELLOW + str(j-1) + Style.RESET_ALL, end=" ")
            print("")


    def __information(self):
        print("\t\t Battlefleet Gothic is a game based on the classic Battleships pen and paper game, featuring \n"
              "\t much more in terms of gameplay, with different fleet types and weaponry.\n"
              "\t\t Weapon types:\n"
              "\t 1. Macrocannons: these are the classic weapons from Battleship, targetting one tile at a time from the grid\n"
              "\t 2. Lances: these laser lances target 3 tiles in a line, though the line can be any shape.\n"
              "\t\t The game features 5 different ship types: Corvettes, Destroyers, Frigates, Cruisers and Battleships:\n"
              "\t "+Fore.LIGHTBLACK_EX+Style.BRIGHT+"@ Corvettes"+Style.RESET_ALL+" - the smallest ship type (size 2), having only one Macrocannon weapon\n"
              "\t "+Fore.LIGHTGREEN_EX+"@ Destroyers"+Style.RESET_ALL+" - these ships are still small (size 3), otherwise similar in armament to a corvette\n"
              "\t "+Fore.LIGHTYELLOW_EX+"@ Frigates"+Style.RESET_ALL+" - these ships are medium sized (size 4), though still unimpressive in firepower, similar to the smaller ships\n"
              "\t "+Fore.YELLOW+"@ Cruisers"+Style.RESET_ALL+" - these ships are medium sized (size 5), but they feature 2 Macrocannons instead of one\n"
              "\t "+Fore.RED+Style.DIM+"@ Battleships"+Style.RESET_ALL+" - these ships are large (size 6), featuring a feared Lance weapon on the prow and 2 Macrocannons.\n"
              "\n\n\t\t The game is played in turns, each player firing all of their armament in their respective turns. \n"
              "\t\t If one of your ships is destroyed (all of its tiles are hit), then your total available armament is reduced by the ship's armament \n"
              "\t\t If all of your ships are destroyed, you lose. Alternatively, destroying all your opponent's ships ensures your victory!")


    def __print_new_game(self):
        while True:
            print("\tDo you wish to skip the story? (You will be assigned the default fleet type")
            print("1. Yes")
            print("2. No")
            try:
                inp = int(input(Fore.YELLOW+"*-* "+Style.RESET_ALL))
                if inp == 1:
                    self.__setting_up()
                elif inp == 2:
                    self.__print_story()
                    self.__setting_up()
            except Exception:
                print(UIError("Invalid input!"))

    def __setting_up(self):
        while True:
            try:
                available_ships = self.__services.player_available_ships()
                print("\t Begin by placing your ships on the grid! To do so, simply write the ship's type, facing direction and"
                      " then the coordinates of its 'head'. Example:")
                print("\t \t'corvette r 4 5' - this yields a corvette placed horizontally at xcoord 4, ycoord 5, facing right ")
                print("\t \t'delete corvette r 4 5 - this deletes the previously placed corvette and places it back into your fleet\n"
                      "\t \t'generate' - this randomly places your ships on the board")
                print("\t Do note that your fleet still disposes of", available_ships[0], "Corvettes,", available_ships[1],
                        "Destroyers,", available_ships[2] ,"Frigates,", available_ships[3] ,"Cruisers and", available_ships[4] ,"Battleships")
                grid = self.__services.player_board()
                self.ui_print_board(grid)
                command = input()
                shiptype = command.split()[0]
                if shiptype == "delete":
                    shiptype = command.split()[1]
                    direction = command.split()[2]
                    row = int(command.split()[3])
                    col = int(command.split()[4])
                    self.__services.delete_ship(shiptype, direction, row, col)
                elif shiptype == "generate":
                    self.__services.generate_player_board()
                    grid = self.__services.player_board()
                    self.ui_print_board(grid)
                else:
                    direction = command.split()[1]
                    row = int(command.split()[2])
                    col = int(command.split()[3])
                    self.__services.place_ship(shiptype, direction, row, col)

                if self.__services.no_more_ships() == 1:
                    while True:
                        print("\t Do you wish to start the game with the above fleet?")
                        print("\t\t 1. Yes")
                        print("\t\t 2. No (Resets board)")
                        inp = int(input(Fore.YELLOW+"*-* "+Style.RESET_ALL))
                        if inp == 1:
                            self.game_loop()
                            break
                        elif inp == 2:
                            self.__services.reset_player_board()
                            break

            except Exception:
                print(UIError("Invalid command!"))

    def __print_story(self):
        print("\t It is the 41st Millenium, for more than a hundred centuries, the"+ Fore.YELLOW+" Emperor of Mankind"+Style.RESET_ALL+
              " has sat immobile on the" + Fore.YELLOW+ " Golden Throne of Terra"+Style.RESET_ALL+".\n He is the Master of Mankind by the will"
              " of the gods and the master of a million worlds by the might of his inexhaustible armies.\n He"
              " is a rotting carcass writhing invisibly with power from the Dark Age of Technology.\n"
              " He is the Carrion Lord of the vast "+ Fore.YELLOW+"Imperium of Man"+Style.RESET_ALL+", for whom thousands of souls "
              "are sacrificed every day, so that He may never truly die...")
        print("Press anything to continue...")
        inp = input()
        print("\t Mighty battlefleets cross the daemon-infested miasma of the Warp, the only route"
              " between distant stars, their way lit by the "+Fore.YELLOW+"Astronomican"+Style.RESET_ALL+",\n the psychic manifestation of "
              "the Emperor's will, acting as a lighthouse in the dark and twisted dimension of the "+Fore.RED+"Immaterium."+Style.RESET_ALL+
              "\n\t Vast armies give battle in his name on uncounted worlds. Crusades are launched in his sake,"
              " spanning centuries and encompassing countless worlds and space sectors.\n Greatest among his soldiers"
              " are the "+Fore.LIGHTBLACK_EX+"Adeptus Astartes"+Style.RESET_ALL+" - bioengineered superwarriors, gathered in diverse orders of "
              "warrior monks named Chapters.\n Their comrades in arms are legion - The "+Fore.GREEN+"Imperial Guard"+Style.RESET_ALL+" and"
              " innumerable Planetary Defense Forces, the ever-vigilant "+Fore.YELLOW+"Inquisition"+Style.RESET_ALL+" or the techpriests\n"
              " of the "+Fore.LIGHTRED_EX+"Adeptus Mechanicus"+Style.RESET_ALL+" to name only a few - but for all their multitudes, they are"
              " barely enough to hold off the ever-present threat to Humanity:\n from "+Fore.RED+"heretics"+Style.RESET_ALL+", "+Fore.LIGHTGREEN_EX+"mutants"+Style.RESET_ALL+" and"
              " "+Style.DIM+"far... far worse."+Style.RESET_ALL)
        print("Press anything to continue...")
        inp = input()
        print("\t To be a man in such times is to be one among untold trillions. Forget the power of technology"
              " and science, for so much has been forgotten, never to be relearned.\n Forget the promise of "
              "progress and understanding, for in the grimdark future of the 41st millenium, there is only war.\n"
              "There is no peace among the stars, only an eternity of carnage and slaughter"
              "... and the laughter of thirsting gods.")
        print("Press anything to continue...")
        inp = input()
        while True:
            print("\t You are not part of the vast, regular masses, though. You have privilege in the "
                  "Imperium of Man, acting as a beacon of light in the vast darkness of space."
                  " You are a:")
            print("\t\t"+Fore.LIGHTYELLOW_EX+"*1. Rogue Trader*"+Style.RESET_ALL+ "- a person in hold of the sacred Warrant of Trade, an artifact document"
                  " which grants enormous power and freedom to the bearer, ensuring they are allowed\n\t to explore "
                  " the stars in the name of the Imperium, colonize worlds and make use of alien artifacts and knowledge."
                  "\n\t Your fleet's power is balanced, utilizing a varied array of ship types.")
            print("\t\t"+Fore.LIGHTCYAN_EX+"*2. Chartist Captain*"+Style.RESET_ALL+" - though you are not of noble birth, you have carved your way up through"
                  " the classes of the Imperium, gaining the Merchant Charter and eventually\n\t gathering a fleet"
                  " with which to do your trade among the stars."
                  "\n\t Your fleet's power relies on a multitude of smaller, nimble ships.")
            print("\t\t"+Fore.BLUE+"*3. Imperial Navy Admiral* "+Style.RESET_ALL+"- you are a Navy Admiral, a position of great power, yet also"
                  " great responsibility. You have been tasked with aiding the latest incursion into\n\t the"
                  " tumultuous Calixis Sector. Your fleet carries several regiments of the Imperial Guard"
                  " and it is your duty to see them delivered to the wartorn world of Tyberion Prime."
                  "\n\t Your fleet's power relies on large capital ships, prepared to face the worst"
                  " challenges the Void can throw at you.")
            try:
                inp = int(input(Fore.YELLOW+"*-* "+Style.RESET_ALL))
                if inp == 1:
                    self.__services.set_ship_list(5, 4, 3, 2, 1)
                    break
                elif inp == 2:
                    self.__services.set_ship_list(8, 6, 4, 1, 0)
                    break
                elif inp == 3:
                    self.__services.set_ship_list(0, 0, 4, 4, 2)
                    break

            except Exception:
                print(UIError("Invalid input!"))


    def game_loop(self):
        #Should likely be in services
    #Implementation 1:

        #Player turn starts
        #Checks available (alive) ships
        #Calculates player available armament
        #Lets player place shots on the hit grid (must check whether or not said spots have been targetted or not)
        #Player turn ends

        #Game calculates the shots and updates all grids, checks win/lose conditions

        #Computer turn starts
        #Checks available (alive) ships
        #Calculates available armament
        #Computer places shots on their hit grid
        #Computer turn ends

        #Game calculates the shots and updates all grids, checks win/lose conditions
        #...

    #Implementation 2:
        #Similar to implementation 1, but damage is calculated after the end of both players' turns,
        # reducing 'alpha strike' potency, but also allowing for the game to have draws.
        turncnt = 0
        while True:
            #Player turn
            player_ships = self.__services.player_board()
            print("Your fleet: ")
            self.ui_print_board(player_ships)
            print("You have", self.__services.player_alive_ships(), "ships left!")
            print("\t It is your turn! To place hits on the board, insert commands: \n"
                  "\t\t Example: 'm: 1 3' - this places a macrocannon hit on xcoord 1, ycoord 3 \n"
                  "\t\t\t\t  'm: 1 3, 4 5, 1 6, 5 6 - this places multiple macrocannon hits on the given coords"
                  "\n\t\t Lances must be shot individually")
            if turncnt != 0:
                print("\t Check your hits board for any hits and then plan your next hits accordingly! The Emperor Protects!")
            player_armament = self.__services.player_total_armament()
            while True:
                try:
                    print("You have ", end = '')
                    if player_armament[0] > 0:
                        print(Fore.BLUE + str(player_armament[0]) + Style.RESET_ALL + " macrocannons ", end='')
                    if player_armament[1] > 0:
                        print(Fore.RED + str(player_armament[1]) + Style.RESET_ALL + " lances ", end='')
                    if player_armament[0] == 0 and player_armament[1] == 0:
                        print("nothing", end = '')
                    print("left to fire.")
                    #print hit board
                    playerhits = self.__services.player_hitsboard()
                    self.ui_print_board(playerhits)
                    inp = input()
                    weapontype = inp.split(':')[0]
                    if weapontype in self.__services.macrocannon_tuple():
                        coordcells = inp.split(':')[1]
                        for cell in coordcells.split(","):
                            if player_armament[0] > 0:
                                r = int(cell.split()[0].strip())
                                c = int(cell.split()[1].strip())
                                self.__services.player_addhit(r, c)
                                player_armament[0] -= 1
                            else:
                                break
                    elif weapontype in self.__services.lance_tuple():
                        coordcells = inp.split(':')[1]
                        if len(coordcells.split(",")) > 3:
                            print(UIError("Invalid lance length! (must be <= 3"))
                            raise Exception
                        else:
                            check = 1
                            prev = 0
                            lancecells = []
                            for cell in coordcells.split(","):
                                if prev == 0:
                                    prev = [int(cell.split()[0].strip()), int(cell.split()[1].strip())]
                                    lancecells.append([prev[0], prev[1]])
                                else:
                                    r = int(cell.split()[0].strip())
                                    c = int(cell.split()[1].strip())
                                    if abs(r - prev[0]) > 1 or abs(c - prev[1]) > 1:
                                        check = 0
                                        print(UIError("Invalid lance placement!"))
                                        raise Exception
                                    prev = [r, c]
                                    lancecells.append([r, c])

                            if check == 1:
                                for cell in lancecells:
                                    r = cell[0]
                                    c = cell[1]
                                    self.__services.player_addhit(r, c)
                                player_armament[1] -= 1
                    if weapontype == "pass" or (player_armament[0] == 0 and player_armament[1] == 0):
                        print("Your turn is over! Insert anything to continue...")
                        inp = input()
                        break

                except Exception:
                    print(UIError("Invalid Hit command!"))
            #verify win/lose, draw shots
            self.__services.end_turn()

            #Computer turn
            print("Enemy's turn!")

            try:
                #debug = self.__services.computer_total_armament()
                #print("Computer armament: ", debug)
                self.__services.computer_turn()
            except Exception:
                print(UIError("AI ERROR"))
            #verify win/lose, draw shots
            self.__services.end_turn()
            turncnt += 1

    def main(self):
        while True:
            print("Welcome to Battlefleet Gothic's main menu! (Battleship)")
            print("\t 1. New Game")
            print("\t 2. Information")
            print("")
            print("\t 0. Exit")
            try:
                inp = int(input(Fore.YELLOW+"*-* "+Style.RESET_ALL))
                if inp == 0:
                    quit()
                elif inp == 1:
                    self.__print_new_game()
                elif inp == 2:
                    self.__information()
            except ValueError:
                print(UIError("Invalid input!"))

menu = Menu()
menu.main()