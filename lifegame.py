import random
import time
import pad

def generatePopulation(board, popNumber):
	indexSample = random.sample([j for j in range(len(board)*len(board[0]))], popNumber)
	print(indexSample)
	for idx in indexSample:
		board[idx//len(board)][idx%len(board[0])] = 1
	return board

def makeBoard(number):
	board = []
	while len(board) < number:
		board.append([0]*number)
	return board

def kill(board):
	outBoard = makeBoard(len(board))
	for r in range(len(board)):
		for c in range(len(board[r])):
			if board[r][c]:
				cellNumber = -1
				for x in range(-1,2):
					for y in range(-1,2):
						idx = r + x
						idy = c + y
						if idx >= 0 and idx < len(board) and idy >= 0 and idy < len(board[r]):
							cellNumber += board[idx][idy]
				if cellNumber < 2 or cellNumber > 3:
					outBoard[r][c] = -1
	return outBoard

def populate(board):
	outBoard = makeBoard(len(board))
	for r in range(len(board)):
		for c in range(len(board[r])):
			if not board[r][c]:
				cellNumber = 0
				for x in range(-1,2):
					for y in range(-1,2):
						idx = r + x
						idy = c + y
						if idx >= 0 and idx < len(board) and idy >= 0 and idy < len(board[r]):
							cellNumber += board[idx][idy]
				if cellNumber == 3:
					outBoard[r][c] = 1
	return outBoard

def updateBoard(board): 
	populated = populate(board)
	killed = kill(board)
	for r in range(len(board)):
		for c in range(len(board[r])):
			board[r][c] += populated[r][c] + killed[r][c]
	return board

def checkBoard(board):
	checkValue = 0
	for b in board:
		checkValue += b.count(1)
	if checkValue > 0:
		return True
	else:
		return False

def showBoard(board):
	for b in board:
		print(b)

def getUserNumber():
	while True:
		try:
			num = int(input("Insert an integer: "))
			return num
		except:
			print("Wrong input! Try again.")

def main():
	midi = pad.Midi()
	with midi:
		print("Board size")
		board = makeBoard(getUserNumber())
		showBoard(board)
		print("Population size")
		board = generatePopulation(board, getUserNumber())
		generation = 0
		print(f"Generation: {generation}")
		showBoard(board)
		midi.lightBoard(board)
		while checkBoard(board):
			time.sleep(1)
			board = updateBoard(board)
			generation += 1
			print(f"Generation: {generation}")
			showBoard(board)
			midi.lightBoard(board)

if __name__ == "__main__":
	main()