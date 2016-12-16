import time
import cProfile
import math


#This function will give all possible sequences for a given empty gameboard
#However because it is constantly copying a 2d board recursively, it isn't useful past 14
def getBoardList(testBoard, n, queenColList=[], row=0):
	localBoard = []
	#n = len(testBoard)
	boardList = []
	#List of columns the currently placed queens occupy
	#Does not contain row information because we are only testing one queen on a row at a time in each level of recurison
	
	#Keep track of how many times we called the function
	#global boardCheckCount
	#boardCheckCount += 1

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
				diff1 = col - queenColList[fig]
				diff2 = row - fig
				if(diff1 == diff2 or diff1 == -diff2):
					failure = True
					break

			#If we didnt find any queens diagnolly from our position then make a temporary board and make this positon have a queen
			#If we aren't finished, recurse and extend the boardlist with the results
			if not failure:
				localBoard[row][col] = True
				newQueenList = queenColList[:]
				newQueenList.append(col)

				#If we have the full number of queens placed on the board and the current board is not already saved, save it and move on.
				if row == n-1 and localBoard not in boardList:
					boardList.append(localBoard)
				else:
					#We aren't done with this board so we take the new board and send it through the recursive function again
					#This may return either a single board or a list of boards so we deal with both cases
					boardList.extend(getBoardList(localBoard, n, newQueenList, row=row+1))
	#This is [] by default.
	#If no new valid placements on the board are found the function will return a blank list of length 0
	return boardList


#This recursive function is faster but uses a 1D list
#The exclude list is a number of columns, each column holds a row position that the queen is at
#IF the column is == to -1 then a queen has not been placed in that column yet
permCount = 0
def getPerms(excludeList, listLen, row=0):
	#perms = []
	colRange = range(listLen)
	failure = False
	for col in colRange:
		
		if excludeList[col] == -1:
			for fig in colRange:
				if excludeList[fig] != -1:
					#If the column difference and the row difference are equal then they are diagnol positions
					diff1 = col - fig
					diff2 = row - excludeList[fig]
					if diff1 == diff2 or diff1 == -diff2:
						failure = True
						break
			
			if not failure:
				newExclude = excludeList[:]
				newExclude[col] = row

				if row == listLen-1:
					#If you want a list of possible combinations then save the final exclude list and return it
					#perms.append(newExclude)
					global permCount
					permCount += 1
				else:
					#perms.extend(
					getPerms(newExclude, listLen, row+1)
			else:
				failure = False

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
	getPerms([-1]*n, n)
	endTime = time.time() - startTime

	#Check if we got a result, print it
	if(permCount):
		print()
		print("Number of unique combinations: " + str(permCount))
	else:
		print("no result")

	print("Recursive function runtime: " + str(endTime))

#run the program
main()