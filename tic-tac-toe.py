def drawBoard(x):
	"""
	Draw the tic-tac-toe board
	"""
	print x[0]+"|"+x[1]+"|"+x[2]
	print x[3]+"|"+x[4]+"|"+x[5]
	print x[6]+"|"+x[7]+"|"+x[8]

def askInput(board):
	"""
	Get the user Input and add it to the board
	"""
	isNum = False
	
	print "It is %s's turn." % board[-1]
	while isNum == False:			
		turn = int(raw_input("Choose a square -> "))
		
		if turn not in range(1,10):
			print "That number is not on the board!"
		elif str(turn) != board[turn-1]:
			print "That choice has already been selected!"
		else:
			isNum = True

	if board[-1] == "Player 1":
		board[turn-1] = "X"
		board[-1] = "Player 2"
	elif board[-1] == "Player 2":
		board[turn-1] = "O"
		board[-1] = "Player 1"
	
	return board
	

def checkWin(x, win):
	"""
	Check for a win situation
	"""
	if (
			x[0]==x[1]==x[2] or x[0]==x[3]==x[6] or x[0]==x[4]==x[8] 
			or x[1]==x[4]==x[7] or x[2]==x[5]==x[8] or x[3]==x[4]==x[5] 
			or x[6]==x[7]==x[8] or x[6]==x[4]==x[2]
		):
		if x[-1] == "Player 2":
			drawBoard(x)				
			print ("Player 1 wins!")
			
		else:
			drawBoard(x)			
			print ("Player 2 wins!")

		win = True
	
	return win

def main(board):
	"""
	The tic-tac-toe-game
	"""
	win = False
	while win == False:
		drawBoard(board)	
		board = askInput(board)
		win = checkWin(board, win)
		
	
	print "Game Over!"

if __name__ == "__main__":
	board = ["1","2","3","4","5","6","7","8","9","Player 1"]
	main(board)
