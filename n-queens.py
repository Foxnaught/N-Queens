import time
import cProfile
boardCheckCount = 0

def getBoardList(testBoard, excludeList=[], row=0):
	localBoard = []
	n = len(testBoard)
	boardList = []
	#List of columns the currently placed queens occupy
	#Does not contain row information because we are only testing one queen on a row at a time in each level of recurison
	queenColList = excludeList[:]
	#Keep track of how many times we called the function
	global boardCheckCount
	boardCheckCount += 1

	for col in range(n):
		if(col not in queenColList):
			#Manual copyList function, does the function directly to avoid call time
			#Refills localBoard with the testBoard we started with.
			#This clears the new queens position in the row so that we may test the next column with our starting board
			localBoard = []
			for item in testBoard:
				localBoard.append(item[:])

			failure = False
			#Go through the board horizontally, vertically, and diagonally from this point to check for queens
			#Set failure if any true values are found in those paths
			for fig in range(row):
				#If the differences of each component match then they are diagonal
				#The second argument switches the sign to check for absolute equivalence
				if(col-queenColList[fig] == row-fig or col-queenColList[fig] == fig-row):
					failure = True
					break

			#If we didnt find any queens diagnolly from our position then make a temporary board and make this positon have a queen
			#If we aren't finished, recurse and extend the boardlist with the results
			if not failure:
				localBoard[row][col] = True
				newQueenList = queenColList[:]
				newQueenList.append(col)

				#If we have the full number of queens placed on the board and the current board is not already saved, save it and move on.
				if len(newQueenList) == n and localBoard not in boardList:
					boardList.append(localBoard)
				else:
					#We aren't done with this board so we take the new board and send it through the recursive function again
					#This may return either a single board or a list of boards so we deal with both cases
					perms = getBoardList(localBoard, newQueenList, row=row+1)
					boardList.extend(perms)
	#This is [] by default.
	#If no new valid placements on the board are found the function will return a blank list of length 0
	return boardList

def main():
	#Set the number of rows columns and queens
	n=int(input("Set nxn area: "))
	#Build a blank gameboard of dimensions (n x n)
	gameBoard = []
	for a in range(n):
		gameBoard.append([False]*n)

	#Call the recursive function that will return us a list of valid board configurations
	#True values on the board represent queens
	#False values represent blank spaces
	startTime = time.time()
	gameBoardList = getBoardList(gameBoard)
	endTime = time.time() - startTime

	#Check if we got a result, print it
	if(gameBoardList != []):
		#Dont print thousands of boards
		if(n<10):
			for a in gameBoardList:
				for t in a:
					print(t)
				print("-----")

		print('\n')
		print("Number of unique combinations: " + str(len(gameBoardList)))
	else:
		print("no result")

	print("Recursive function runtime: " + str(endTime))
	#this tells us how many times the recursive function was called
	print("Check Count: " + str(boardCheckCount))

#run the program
main()