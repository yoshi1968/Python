# the board should be stored as a three-element list, 
# so that all of the squares may be accessed using the following syntax:
# 	board[row][column]

board = [[1,2,3],[4,"X",6],[7,8,9]]

# each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)

def display_board(board):
	# The function accepts one parameter containing the board's current status
	# and prints it out to the console.
	print("+-------+-------+-------+\n|	   |	   |	   |\n|   ",
	board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],
	"   |\n|	   |	   |	   |\n+-------+-------+-------+\n|	   |	   |	   |\n|   ",
	board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],
	"   |\n|	   |	   |	   |\n+-------+-------+-------+\n|	   |	   |	   |\n|   ",
	board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],
	"""   |\n|	   |	   |	   |\n+-------+-------+-------+\n""",
	sep="")

def enter_move(board):
	# The function accepts the board current status, 
	# asks the user about their move, 
	your_move = int(input("Enter your move: ")) - 1
	# checks the input
	# 	it must be an integer, 
	# 	it must be greater than 0 and less than 10, and 
	# 	it cannot point to a field which is already occupied;
	while True:
		if type(your_move) == int and \
		your_move > 0 and your_move < 10 and \
		type(board[your_move // 3][your_move % 3]) == int:
		    break
		print("Wrong move!")
		your_move = int(input("Enter your move: ")) - 1
	# updates the board according to the user's decision.
	board[your_move // 3][your_move % 3] = "O"
	display_board(board)

def make_list_of_free_fields(board):
	# The function browses the board and builds a list of all the free squares; 
	# the list consists of tuples, while each tuple is a pair of row and column numbers.
	free_sq = []
	for row in range(3):
		for col in range(3):
			if type(board[row][col]) == int:
				free_sq.append(tuple((row,col)))
	return free_sq

def victory_for(board, sign):
	# The function analyzes the board status in order to check if 
	# the player using 'O's or 'X's has won the game
	for row in range(3):
		for col in range(3):
			if board[row][col] != sign:
				continue
			break
		

