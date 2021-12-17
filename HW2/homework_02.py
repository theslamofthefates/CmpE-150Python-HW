# Ultimate Battleships
# The file includes a minor mistake, 87/100.

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = False  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    # Since I have made naming as obvious as possible, I may not explain each variable.
    player_board = [['-' for c in range(board_size)] for l in range(board_size)]   # Creating the board
    player_empty_board = player_board[:]  # Because I used empty board a lot, I just copied it
    generalList = []  # generalList will hold the last standing of ships
    for b in range(2):  # There are 2 players
        ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        shipSize = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}
        shipUsed = []
        number_of_ships_F = 0  # Number of ships placed
        playerDone = False
        while not playerDone:  # playerDone is False unless the player places their ships and confirm the placement.
            # generalBoards has 2 sub-lists which are at the end of each for loop turns into the actual placement.
            generalBoards = [[['-' for ll in range(board_size)] for kk in range(board_size)] for z in range(2)]
            while number_of_ships_F < 5:
                print_3d_list(generalBoards)
                print_ships_to_be_placed()
                ships_Edited = [print_single_element(ship) for ship in ships]
                print_empty_line()
                print_player_turn_to_place(b + 1)
                print_to_place_ships()
                k = input().strip().split()
                # Below checks if the input is appropriate to use it or not.
                if len(k) < 4:
                    print_incorrect_input_format()
                    continue
                if not k[1].isdigit() or not k[2].isdigit():
                    print_incorrect_input_format()
                    continue
                shipName = k[0]
                shipOrnt = k[3]
                shipYAx = int(k[2])
                shipXAx = int(k[1])
                if shipYAx < 1 or shipYAx > 10 or shipXAx < 1 or shipXAx > 10:
                    print_incorrect_coordinates()
                    continue
                if shipName.title() not in ships and shipName.title() not in shipUsed:
                    print_incorrect_ship_name()
                    continue
                shipName = shipName.title()
                if shipOrnt.lower() != 'h' and shipOrnt.lower() != 'v':
                    print_incorrect_orientation()
                    continue
                if shipName in shipUsed:
                    print_ship_is_already_placed(shipName)
                    continue
                shipOrnt = shipOrnt.lower()
                # Input check is almost complete.
                # contr is the variable that checks if the new ship's coordinates include an already occupied position
                # or not
                contr = 0
                if shipOrnt == "h" and shipXAx + shipSize[shipName] > 11:  # Whether the ship stays inside is controlled
                    print_ship_cannot_be_placed_outside(shipName)
                    continue    # If there is an error, the program uses continue command.
                elif shipOrnt == "h" and shipXAx + shipSize[shipName] <= 11:
                    for ff in range(shipSize[shipName]):
                        if generalBoards[b][shipYAx - 1][shipXAx - 1 + ff] == "#":
                            contr += 1
                    if contr != 0:  # If contr is not equal to zero, then there must be a ship on that coordinates.
                        print_ship_cannot_be_placed_occupied(shipName)
                        continue
                    # If there is no error, placement starts.
                    for ff in range(shipSize[shipName]):
                        generalBoards[b][shipYAx - 1][shipXAx - 1 + ff] = "#"
                if shipOrnt == "v" and shipYAx + shipSize[shipName] > 11:  # Whether the ship stays inside is controlled
                    print_ship_cannot_be_placed_outside(shipName)
                    continue
                elif shipOrnt == "v" and shipYAx + shipSize[shipName] <= 11:
                    for ff in range(shipSize[shipName]):
                        if generalBoards[b][shipYAx - 1 + ff][shipXAx - 1] == "#":
                            contr += 1
                    if contr != 0:
                        print_ship_cannot_be_placed_occupied(shipName)
                        continue
                    # If there is no error, placement starts.
                    for ff in range(shipSize[shipName]):
                        generalBoards[b][shipYAx + ff - 1][shipXAx - 1] = "#"
                # If nothing has gone wrong, finally the ship is removed from the main list and added to the shipUsed
                ships.remove(shipName.title())
                shipUsed.append(shipName.title())
                number_of_ships_F += 1
            # If we take the last input, since we should prompt different messages I make this situation different than
            # previous four.
            if number_of_ships_F == 5:
                print_3d_list(generalBoards)
                while True:
                    print_confirm_placement()
                    k = input().strip().split()
                    if k[0].lower() == "y":
                        generalList.append(generalBoards[b])  # First iteration is done, board of the current player is added.
                        generalBoards[b] = player_empty_board[:]
                        playerDone = True  # Player done
                        break
                    elif k[0].lower() == "n":
                        number_of_ships_F = 0   # Resetting the number of ships Placed
                        ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                        shipUsed = []  # Resetting control lists
                        generalBoards[b] = player_empty_board[:]  # Resetting the boards
                        break
                    else:
                        continue
    # WAR STARTS!
    initPl = 0   # initial_Player holds the current player number
    points1 = 0  # war score of player 1
    points2 = 0  # war score of player 2
    generalBoards = [[['-' for c in range(10)] for l in range(10)] for k in range(2)]  # Board will be edited in the war
    while points1 < 17 and points2 < 17:  # Since there are 17 tiles to hit, they can gain at most 17 score.
        if initPl % 2 == 0:  # If initPl is even, then it indicates it is turn of the first player.
            print_3d_list([generalList[0], generalBoards[1]])
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            k = input().strip().split()
            """     Input control starts  """
            if len(k) < 2:
                print_incorrect_input_format()
                continue
            if not k[0].isdigit() or not k[1].isdigit():
                print_incorrect_input_format()
                continue
            x_Axis = int(k[0]) - 1  # -1 because I used list
            y_Axis = int(k[1]) - 1  # -1 because I used list
            if y_Axis > 9 or y_Axis < 0 or x_Axis > 9 or x_Axis < 0:
                print_incorrect_coordinates()
                continue
            if generalBoards[1][y_Axis][x_Axis] == "O" or generalBoards[1][y_Axis][x_Axis] == "!":
                print_tile_already_struck()
                continue
            """     Input control ends  """
            if generalList[1][y_Axis][x_Axis] == "#":  # Hit case
                print_hit()
                generalBoards[1][y_Axis][x_Axis] = "!"
                generalList[1][y_Axis][x_Axis] = "!"
                points1 += 1
                if points1 == 17:
                    print_3d_list([generalList[0], generalBoards[1]])
                    break
                continue
            else:   # If not then it must be a missing shot
                print_miss()
                generalBoards[1][y_Axis][x_Axis] = "O"
                generalList[1][y_Axis][x_Axis] = "O"
                while True:
                    print_type_done_to_yield(2)
                    k = input().strip().split()
                    if k[0].lower() == "done":
                        initPl += 1
                        break
                continue
        else:  # If initPl is odd, then it indicates it is turn of the second player
            print_3d_list([generalBoards[0], generalList[1]])
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            k = input().strip().split()
            """     Input control starts  """
            if len(k) < 2:
                print_incorrect_input_format()
                continue
            if not k[0].isdigit() or not k[1].isdigit():
                print_incorrect_input_format()
                continue
            x_Axis = int(k[0]) - 1
            y_Axis = int(k[1]) - 1
            if y_Axis > 9 or y_Axis < 0 or x_Axis > 9 or x_Axis < 0:
                print_incorrect_coordinates()
                continue
            # Checks if the tile has already been struck.
            if generalBoards[0][y_Axis][x_Axis] == "O" or generalBoards[0][y_Axis][x_Axis] == "!":
                print_tile_already_struck()
                continue
            """     Input control ends  """
            if generalList[0][y_Axis][x_Axis] == "#":   # If there is a ship part, it is hit
                print_hit()
                generalBoards[0][y_Axis][x_Axis] = "!"
                generalList[0][y_Axis][x_Axis] = "!"
                points2 += 1
                if points2 == 17:
                    print_3d_list([generalBoards[0], generalList[1]])
                    break
            else:
                print_miss()
                generalBoards[0][y_Axis][x_Axis] = "O"
                generalList[0][y_Axis][x_Axis] = "O"
                while True:
                    print_type_done_to_yield(1)
                    k = input().strip().split()
                    if k[0].lower() == "done":
                        initPl += 1
                        break
    if points2 < points1:   # Who has won is stated
        print_player_won(1)
    else:
        print_player_won(2)
    print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()