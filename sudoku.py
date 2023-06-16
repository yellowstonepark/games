import numpy as np
import math
import time

# 0 represents empty cells
# 1-9 represents the numbers in the cells
# valid sudoku puzzles taken from an official sudoku app

boards = [

#super easy - board 1
np.array([
    [5, 3, 4, 0, 7, 0, 0, 0, 2],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 6, 0, 5],
    [0, 0, 0, 0, 8, 0, 1, 7, 9]
], dtype=object),

#easy - board 2
np.array([
    [0, 7, 9, 3, 0, 0, 0, 0, 0],
    [3, 0, 2, 0, 0, 0, 5, 0, 7],
    [0, 0, 0, 0, 0, 1, 0, 9, 0],
    [5, 0, 0, 1, 8, 0, 0, 0, 0],
    [1, 2, 6, 4, 9, 0, 7, 3, 0],
    [0, 8, 7, 6, 3, 0, 4, 5, 1],
    [0, 6, 0, 0, 0, 3, 1, 0, 9],
    [0, 0, 0, 5, 0, 6, 8, 7, 0],
    [2, 0, 0, 7, 0, 0, 0, 0, 0]
], dtype=object),

#medium - board 3
np.array([
    [4, 0, 0, 9, 6, 2, 0, 0, 0],
    [7, 6, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 8, 0, 7, 0, 0, 0, 1],
    [0, 5, 0, 0, 0, 6, 8, 0, 0],
    [0, 0, 4, 0, 0, 3, 1, 0, 6],
    [3, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 2, 0, 0, 0, 9, 8, 4],
    [8, 0, 0, 0, 0, 0, 2, 0, 0],
    [5, 0, 9, 0, 2, 7, 0, 0, 0]
], dtype=object),

#hard - board 4
np.array([
    [0, 4, 1, 0, 6, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 9, 0, 0, 0, 4, 5, 6, 0],
    [7, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 2, 0, 7, 5, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 3, 1, 0, 8, 0],
    [0, 8, 3, 0, 0, 0, 2, 0, 0],
    [0, 0, 4, 0, 2, 0, 0, 0, 0]
], dtype=object),

#expert - board 5
np.array([
    [0, 2, 9, 1, 0, 0, 0, 6, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 1, 3, 0, 4, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 6, 4, 0, 8, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 0, 2],
    [0, 9, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 5, 7]
], dtype=object),

#evil - board 6
np.array([
    [0, 9, 3, 4, 7, 0, 0, 6, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 3, 4, 0, 0, 9, 0, 0, 5],
    [1, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 2, 0, 0],
    [0, 6, 7, 0, 9, 0, 0, 1, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0]
], dtype=object),
    
# another evil - board 7
np.array([
    [4, 1, 0, 0, 0, 6, 0, 0, 0],
    [0, 9, 0, 0, 7, 0, 5, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 8, 0, 0, 3, 0],
    [9, 0, 0, 4, 0, 0, 2, 0, 8],
    [0, 2, 0, 0, 0, 0, 0, 7, 0],
    [0, 5, 0, 0, 1, 0, 8, 0, 9],
    [0, 0, 1, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3]
], dtype=object)

]

board_num = None

while board_num not in range(1, 9):
    board_num = input("Enter a difficulty (1-7), or 8 to make your own board: ")
    try:
        board_num = int(board_num)
    except:
        print("Please enter a number")
    if board_num == 8:
        board = np.zeros((9,9), dtype=object)
        print("The program assumes that you use a valid sudoku board.")
        for row in range(board.shape[0]):
            for number in range(board.shape[1]):
                value = None
                while value not in range(0, 10):
                    value = input("Enter a number for row " + str(row + 1) + " column " + str(number + 1) + ". You can input 0 for empty values: ")
                    try:
                        value = int(value)
                    except:
                        print("Please enter a number")
                board[row, number] = value
        break
    else:
        board = boards[board_num - 1]

original_board = board.copy()

# convert all 0s to numpy arrays
for row in range(board.shape[0]):
    for number in range(board.shape[1]):
        value = board[row, number]
        if value == 0:
            board[row, number] = np.array([0])

possible_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# array -> array
# check to see if any cells can be figured out by process of elimination
# test:
'''
[[4 1 array([2, 8]) array([2, 5, 8]) array([2, 5]) 6 3 9 7]
 [array([2, 3, 6]) 9 array([2, 3, 6]) array([2, 3]) 7 4 5 8 1]
 [5 array([3, 8]) 7 1 9 array([3, 8]) 4 2 6]
 [array([1, 6]) array([4, 6]) array([4, 6]) array([2, 5, 6, 9]) 8 7
  array([1, 9]) 3 array([4, 5])]
 [9 7 5 4 3 1 2 6 8]
 [array([1, 3, 6, 8]) 2 array([3, 4, 6, 8]) array([5, 6, 9])
  array([5, 6]) array([5, 9]) array([1, 9]) 7 array([4, 5])]
 [array([2, 3, 6, 7]) 5 array([2, 3, 6]) array([2, 3, 6]) 1 array([2, 3])
  8 4 9]
 [array([3, 8]) array([3, 8]) 1 7 4 array([3, 8, 9]) 6 5 2]
 [array([2, 6, 8]) array([4, 6, 8]) 9 array([2, 5, 6, 8])
  array([2, 5, 6]) array([2, 5, 8]) 7 1 3]]
[[4 1 array([2, 8]) array([2, 5, 8]) array([2, 5]) 6 3 9 7]
 [array([2, 3, 6]) 9 array([2, 3, 6]) array([2, 3]) 7 4 5 8 1]
 [5 array([3, 8]) 7 1 9 array([3, 8]) 4 2 6]
 [array([1, 6]) array([4, 6]) array([4, 6]) 2 8 7 array([1, 9]) 3
  array([4, 5])]
 [9 7 5 4 3 1 2 6 8]
 [array([1, 3, 6, 8]) 2 array([3, 4, 6, 8]) array([5, 6, 9])
  array([5, 6]) array([5, 9]) array([1, 9]) 7 array([4, 5])]
 [array([2, 3, 6, 7]) 5 array([2, 3, 6]) array([2, 3, 6]) 1 array([2, 3])
  8 4 9]
 [array([3, 8]) array([3, 8]) 1 7 4 array([3, 8, 9]) 6 5 2]
 [array([2, 6, 8]) array([4, 6, 8]) 9 array([2, 5, 6, 8])
  array([2, 5, 6]) array([2, 5, 8]) 7 1 3]]
'''
def elimination(possiblities):
    changed = False
    for row in range(possiblities.shape[0]):
        if changed == True:
                break
        for number in range(possiblities.shape[1]):
            if changed == True:
                break
            
            value = possiblities[row, number]

            if isinstance(value, np.ndarray) == True:

                square_row = math.ceil((row + 1) / 3)
                square_column = math.ceil((number + 1) / 3)

                position_in_square_row = row % 3
                position_in_square_column = number % 3

                square = possiblities[square_row * 3 - 3:square_row * 3, square_column * 3 - 3:square_column * 3]

                #print("Square", square)

                # find all unique values in square but not in the cell
                unique_in_square = np.array([])

                for item in range(square.shape[0]):
                    for item2 in range(square.shape[1]):
                        # for other cells in the square with a numpy array (numpy array = possibilities)
                        if [item, item2] != [position_in_square_row, position_in_square_column]:
                            if isinstance (square[item, item2], np.ndarray) == True:
                                unique_in_square = np.concatenate((unique_in_square, square[item, item2]))
                                #print("Found unique value in square", square[item, item2])
                                #print("Unique in square", unique_in_square)
                        #else:
                        #    print("")
                # all unique values in square
                unique_square = np.unique(unique_in_square)
                #print(value)
                #print(unique_square)

                # if cell has a unique value that isn't possible elsewhere in the square, set it
                unique = np.setdiff1d(value, unique_square)

                if not np.array_equal(unique, np.array([])):
                    possiblities[row, number] = unique[0]
                    #print("Found unique value", unique[0])
                    #print(possiblities)
                    changed = True
                else:
                    changed = False
                if changed == True:
                    break
    return possiblities

# find all possible values for each cell
# numpy array -> numpy array
# test:
'''
[[array([3, 4, 5]) 2 9 1 array([5, 7, 8]) array([5, 7, 8])
  array([3, 4, 7]) 6 3]
 [array([3, 4, 6]) 7 8 9 array([2, 6]) array([2, 6]) array([1, 3, 4])
  array([1, 2, 3, 4]) 5]
 [array([5, 6]) array([5, 6]) 1 3 array([2, 5, 6, 7]) 4 array([7, 9])
  array([2, 7, 9]) 8]
 [array([1, 2, 4, 6, 7]) array([1, 4, 6, 8]) 3 array([7, 8])
  array([1, 2, 7, 8]) array([1, 2, 7, 8]) 5 array([1, 4, 7]) 9]
 [array([1, 2, 5, 7, 9]) array([1, 5]) array([5, 7]) 6 4
  array([1, 2, 7, 9]) 8 array([1, 3, 7]) array([1, 3])]
 [array([1, 4, 7, 9]) array([1, 4, 8]) array([4, 7]) 5 3
  array([1, 7, 8, 9]) 6 array([1, 4, 7]) 2]
 [array([1, 3, 4, 5, 6, 7]) 9 array([4, 5, 6, 7]) array([7, 8])
  array([1, 5, 6, 7, 8]) array([1, 3, 5, 6, 7, 8]) 2 array([1, 3, 4, 8])
  array([1, 3, 4, 6])]
 [array([1, 3, 4, 5, 6, 7]) array([1, 3, 4, 5, 6]) array([4, 5, 6, 7]) 2
  array([1, 5, 6, 7, 8, 9]) array([1, 3, 5, 6, 7, 8, 9])
  array([1, 3, 4, 9]) array([1, 3, 4, 8, 9]) array([1, 3, 4, 6])]
 [8 array([1, 3, 6]) 2 4 array([1, 6, 9]) array([1, 3, 6, 9])
  array([1, 3, 9]) 5 7]]
[[4 2 9 1 8 5 7 6 3]
 [3 7 8 9 6 2 4 1 5]
 [5 6 1 3 7 4 9 2 8]
 [6 1 3 8 2 7 5 4 9]
 [2 5 7 6 4 9 8 3 1]
 [9 8 4 5 3 1 6 7 2]
 [1 9 6 7 5 3 2 8 4]
 [7 4 5 2 1 8 3 9 6]
 [8 3 2 4 9 6 1 5 7]]
'''
def findPossiblities(board):
    possiblities = np.zeros((9,9), dtype=object)

    # while new board is not equal to old board
    prev_board = board.astype(object).copy()

    while True:
        theBoard = prev_board.copy()
        for row in range(theBoard.shape[0]):
            for number in range(theBoard.shape[1]):
                value = theBoard[row, number]
                full_row = theBoard[row, :]
                full_column = theBoard[:, number]
                if isinstance(value, np.ndarray) == True:
                    x = True
                else:
                    x = False
                #if value is a number...
                if x == False and value != 0:
                    possiblities[row, number] = value
                elif x == True or value == 0:
                    
                    # find all unique values in row and column
                    for item in range(full_row.shape[0]):
                        if isinstance (full_row[item], np.ndarray) == True:
                            full_row[item] = 0
                    for item in range(full_column.shape[0]):
                        if isinstance (full_column[item], np.ndarray) == True:
                            full_column[item] = 0
                    unique_row = np.unique(full_row)
                    unique_column = np.unique(full_column)
                    unique_values = np.unique(np.concatenate((unique_row, unique_column)))

                    # find all possible values in the 3x3 square
                    square_row = math.ceil((row + 1) / 3)
                    square_column = math.ceil((number + 1) / 3)

                    square = theBoard[square_row * 3 - 3:square_row * 3, square_column * 3 - 3:square_column * 3]

                    for item in range(square.shape[0]):
                        for item2 in range(square.shape[1]):
                            if isinstance (square[item, item2], np.ndarray) == True:
                                square[item, item2] = 0

                    unique_square = np.unique(square)

                    # find all values the number cannot be
                    unique = np.unique(np.concatenate((unique_values, unique_square)))

                    # values that the number can be
                    possible = np.setdiff1d(possible_values, unique)

                    # if there is only one possible value, set it
                    if possible.shape == (1,):
                        possiblities[row, number] = possible[0]
                    else:
                        # if there are multiple possible values, set it to an array
                        possiblities[row, number] = possible

                else:
                    print("Error")

        prev_board_zeros, possibilities_zeros = convert_arrays_to_zeros(prev_board), convert_arrays_to_zeros(possiblities)
        if np.array_equal(prev_board_zeros, possibilities_zeros):
            break

        prev_board = possiblities.copy()
    
    return possiblities

# arr -> arr
# use many functions to narrow the possbilites down to one solution
# test: 
'''
[[array([3, 4, 5]) 2 9 1 array([5, 7, 8]) array([5, 7, 8])
  array([3, 4, 7]) 6 3]
 [array([3, 4, 6]) 7 8 9 array([2, 6]) array([2, 6]) array([1, 3, 4])
  array([1, 2, 3, 4]) 5]
 [array([5, 6]) array([5, 6]) 1 3 array([2, 5, 6, 7]) 4 array([7, 9])
  array([2, 7, 9]) 8]
 [array([1, 2, 4, 6, 7]) array([1, 4, 6, 8]) 3 array([7, 8])
  array([1, 2, 7, 8]) array([1, 2, 7, 8]) 5 array([1, 4, 7]) 9]
 [array([1, 2, 5, 7, 9]) array([1, 5]) array([5, 7]) 6 4
  array([1, 2, 7, 9]) 8 array([1, 3, 7]) array([1, 3])]
 [array([1, 4, 7, 9]) array([1, 4, 8]) array([4, 7]) 5 3
  array([1, 7, 8, 9]) 6 array([1, 4, 7]) 2]
 [array([1, 3, 4, 5, 6, 7]) 9 array([4, 5, 6, 7]) array([7, 8])
  array([1, 5, 6, 7, 8]) array([1, 3, 5, 6, 7, 8]) 2 array([1, 3, 4, 8])
  array([1, 3, 4, 6])]
 [array([1, 3, 4, 5, 6, 7]) array([1, 3, 4, 5, 6]) array([4, 5, 6, 7]) 2
  array([1, 5, 6, 7, 8, 9]) array([1, 3, 5, 6, 7, 8, 9])
  array([1, 3, 4, 9]) array([1, 3, 4, 8, 9]) array([1, 3, 4, 6])]
 [8 array([1, 3, 6]) 2 4 array([1, 6, 9]) array([1, 3, 6, 9])
  array([1, 3, 9]) 5 7]]
[[4 2 9 1 8 5 7 6 3]
 [3 7 8 9 6 2 4 1 5]
 [5 6 1 3 7 4 9 2 8]
 [6 1 3 8 2 7 5 4 9]
 [2 5 7 6 4 9 8 3 1]
 [9 8 4 5 3 1 6 7 2]
 [1 9 6 7 5 3 2 8 4]
 [7 4 5 2 1 8 3 9 6]
 [8 3 2 4 9 6 1 5 7]]
'''
def calculateSolution(board):
    def arrays_equal(a, b):
        for row in range(a.shape[0]):
            for number in range(a.shape[1]):
                if not np.array_equal(a[row, number], b[row, number]):
                    #print(a[row, number], b[row, number])
                    #print("Arrays not equal")
                    return False
        return True

    a = board.astype(object).copy()
    previous_a = np.zeros((9,9), dtype=object)

    # while new board is not equal to old board
    while not arrays_equal(a, previous_a):
        # save the previous board
        previous_a = a.astype(object).copy()

        # find all possible values for each cell
        while True:
            new_a = findPossiblities(a)
            if arrays_equal(new_a, a):
                break
            a = new_a.astype(object).copy()

        # find any cells that can be figured out by process of elimination
        a = elimination(a)
    return a

# arr -> bool
# check if there are any empty cells
# test: noSolution(np.array([[1, 2, 3], [4, 5, np.array()], [7, 8, 9]])) -> True
# test: noSolution(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) -> False
def noSolution(possiblities):
    empty_arr = np.array([])
    for row in range(possiblities.shape[0]):
        for number in range(possiblities.shape[1]):
            value = possiblities[row, number]
            if np.array_equal(value, empty_arr):
                return True
    return False

# arr -> arr
# convert all arrays in the array to 0s
# test: convert_arrays_to_zeros(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) -> np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# test: convert_arrays_to_zeros(np.array([[1, 2, 3], [4, np.array([5, 6]), 7], [8, 9, 10]])) -> np.array([[1, 2, 3], [4, 0, 7], [8, 9, 10]])
def convert_arrays_to_zeros(arr):
    # avoid modifying the original arrays
    arrr = arr.copy()

    # iterate over each element in the arrays
    for row in range(arrr.shape[0]):
        for column in range(arrr.shape[1]):
            # check if the element is a numpy array
            if isinstance(arrr[row, column], np.ndarray):
                # if it is an array, replace it with 0
                arrr[row, column] = 0

    return arrr

# arr -> bool
# check if there are any arrays in the array
# test: has_arrays(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) -> False
# test: has_arrays(np.array([[1, 2, 3], [4, np.array([5, 6]), 7], [8, 9, 10]])) -> True
def has_arrays(arr):
    for row in arr:
        for element in row:
            if isinstance(element, np.ndarray):
                return True
    return False

# arr + int -> arr
# find the solution by seeing what works
# test: findSolution(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1) -> np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# test: 
'''
4 1 0 | 0 0 6 | 0 0 0 
0 9 0 | 0 7 0 | 5 0 1 
0 0 0 | 0 0 0 | 0 2 0 
---------------------
0 0 0 | 0 8 0 | 0 3 0 
9 0 0 | 4 0 0 | 2 0 8 
0 2 0 | 0 0 0 | 0 7 0 
---------------------
0 5 0 | 0 1 0 | 8 0 9 
0 0 1 | 7 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 3 

 |
 v

 4 1 8 | 5 2 6 | 3 9 7 
2 9 6 | 3 7 4 | 5 8 1 
5 3 7 | 1 9 8 | 4 2 6 
---------------------
1 6 4 | 2 8 7 | 9 3 5 
9 7 5 | 4 3 1 | 2 6 8 
8 2 3 | 9 6 5 | 1 7 4 
---------------------
7 5 2 | 6 1 3 | 8 4 9 
3 8 1 | 7 4 9 | 6 5 2 
6 4 9 | 8 5 2 | 7 1 3 
'''
def findSolution(board, max_iterations):
    counter = 0
    orginal_possible = calculateSolution(board)
    after_attempt = orginal_possible.copy()
    for i in range(9):
        #if the board is solved, return it on the first try
        if has_arrays(orginal_possible) == False:
            print("Found solution")
            return calculateSolution(orginal_possible)
        for q in range(9):
            for w in range(9):
                value = orginal_possible[q, w]
                if isinstance(value, np.ndarray) == True:
                    #print(value.shape)
                    if value.shape == (i,):
                        orginal_possible[q,w] = value[0]
                        #if the board is unsolved, start again
                        if not isinstance(calculateSolution(orginal_possible), np.ndarray):
                            orginal_possible = after_attempt.copy()
                        elif has_arrays(calculateSolution(orginal_possible)) == True:
                            orginal_possible = after_attempt.copy()
                        else:
                            print("Found a solution")
                            return calculateSolution(orginal_possible)
        counter += 1
        if max_iterations == counter:
            return "No solution within one guess for each iteration"

start_time = time.time()

possibilitiess = findSolution(board, 8)

# print the board
# test: printBoard(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) -> 
# 1 2 3
# 4 5 6
# 7 8 9
def printBoard(numpy_array):
    for row in range(numpy_array.shape[0]):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for number in range(numpy_array.shape[1]):
            if number % 3 == 0 and number != 0:
                print("|", end = " ")
            value = numpy_array[row, number]
            if isinstance(value, np.ndarray) == True:
                print("0", end = " ")
            else:
                print(value, end = " ")
        print("")

if isinstance(possibilitiess, np.ndarray) == True:
    # 0s represent unknown values
    print("Original board:")
    printBoard(original_board)
    print("", end = "\n\n")

    print("Solution:")
    printBoard(possibilitiess)

    print("--- %s seconds ---" % round((time.time() - start_time), 2))
else:
    # 0s represent unknown values
    print("Original board:")
    printBoard(original_board)
    print("", end = "\n\n")
    print(possibilitiess)