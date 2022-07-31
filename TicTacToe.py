from re import X

game_is_on = True

winner = None

current_player = "X"

valid = True


board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
	#display initial board
	display_board()
	while game_is_on:
		handle_turn(current_player)
		check_if_gameover()
		flip_player()
	#the game is over
	if winner == "X" or winner == "O":
		print("Congratulations! Winner is " + winner )
	elif winner == None:
		print("Sorry ! the game is TIE")

#handling turn
def handle_turn(player):
	global valid
	print(player + "s turn now")
	position = input("Choose a character from 1 to 9:")

	valid = False
	while not valid:
		while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			print("Please enter a valid position")
			position = input("Choose a character from 1 to 9:")
		
		position = int(position) - 1

		if board[position] == "-":
			valid = True
		else:
			print("you can't go there, please try again!")

	board[position] = player
	#Display current board
	display_board()

#checking if the game is over
def check_if_gameover():
	#check for rows, columns for win or tie
	check_if_win()
	check_if_tie()

def check_if_win():
	global winner
	row_winner = check_rows()
	column_winner = check_columns()
	diagnol_winner = check_diagnols()


	if row_winner:
		winner = row_winner
	
	elif column_winner:
		winner = column_winner

	elif diagnol_winner:
		winner = diagnol_winner
	else:
		winner = None
	return

#rows and diagnols
def check_rows():
	global game_is_on
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"

	if row_1 or row_2 or row_3:
		game_is_on = False

	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]

	return
		

def check_columns():
	global game_is_on
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"

	if column_1 or column_2 or column_3:
		game_is_on = False

	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]
	return

def check_diagnols():
	global game_is_on
	diagnol_1 = board[0] == board[4] == board[8] != "-"
	diagnol_2 = board[2] == board[4] == board[6] != "-"
		

	if diagnol_1 or diagnol_2:
		game_is_on = False

	if diagnol_1:
		return board[0]
	elif diagnol_2:
		return board[6]
		
	return

def check_if_tie():
	global game_is_on
	if "-" not in board:
		game_is_on = False
	return


def flip_player():
	global current_player
	#change the player
	if current_player == "X":
		current_player = "O"
	elif current_player == "O":
		current_player = "X"
	return

play_game()