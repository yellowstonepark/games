import numpy as np
import math
import time

# 0 represents empty cells
# 1-9 represents the numbers in the cells
# any valid sudoku puzzle

#super easy
board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
], dtype=object)

#easy
board = np.array([
    [0, 7, 9, 3, 0, 0, 0, 0, 0],
    [3, 0, 2, 0, 0, 0, 5, 0, 7],
    [0, 0, 0, 0, 0, 1, 0, 9, 0],
    [5, 0, 0, 1, 8, 0, 0, 0, 0],
    [1, 2, 6, 4, 9, 0, 7, 3, 0],
    [0, 8, 7, 6, 3, 0, 4, 5, 1],
    [0, 6, 0, 0, 0, 3, 1, 0, 9],
    [0, 0, 0, 5, 0, 6, 8, 7, 0],
    [2, 0, 0, 7, 0, 0, 0, 0, 0]
], dtype=object)

#medium
board = np.array([
    [4, 0, 0, 9, 6, 2, 0, 0, 0],
    [7, 6, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 8, 0, 7, 0, 0, 0, 1],
    [0, 5, 0, 0, 0, 6, 8, 0, 0],
    [0, 0, 4, 0, 0, 3, 1, 0, 6],
    [3, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 2, 0, 0, 0, 9, 8, 4],
    [8, 0, 0, 0, 0, 0, 2, 0, 0],
    [5, 0, 9, 0, 2, 7, 0, 0, 0]
], dtype=object)

#hard
board = np.array([
    [0, 4, 1, 0, 6, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 9, 0, 0, 0, 4, 5, 6, 0],
    [7, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 2, 0, 7, 5, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 3, 1, 0, 8, 0],
    [0, 8, 3, 0, 0, 0, 2, 0, 0],
    [0, 0, 4, 0, 2, 0, 0, 0, 0]
], dtype=object)

#expert

board = np.array([
    [0, 2, 9, 1, 0, 0, 0, 6, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 1, 3, 0, 4, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 6, 4, 0, 8, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 0, 2],
    [0, 9, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 5, 7]
], dtype=object)

#evil
board = np.array([
    [0, 9, 3, 4, 7, 0, 0, 6, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 3, 4, 0, 0, 9, 0, 0, 5],
    [1, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 2, 0, 0],
    [0, 6, 7, 0, 9, 0, 0, 1, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0]
], dtype=object)
    
# another evil
board = np.array([
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

for row in range(board.shape[0]):
    for number in range(board.shape[1]):
        value = board[row, number]
        if value == 0:
            board[row, number] = np.array([0])

print(type(board[0,2]))
print(type(board[0,0]))

possible_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

def elimination(possiblities):
    # check to see if any cells can be figured out by process of elimination
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
                    #print(square)
                    unique_square = np.unique(square)

                    # find all values the number cannot be
                    unique = np.unique(np.concatenate((unique_values, unique_square)))

                    # values that the number can be
                    possible = np.setdiff1d(possible_values, unique)

                    # if there is only one possible value, set it
                    if possible.shape == (1,):
                        possiblities[row, number] = possible[0]
                    else:
                        possiblities[row, number] = possible

                else:
                    print("Error")
        #print(possiblities)

        #ifnosolution = noSolution(possiblities)
        #if ifnosolution == True:
        #    return "No Solution"

        #possiblities = elimination(possiblities)

        prev_board_zeros, possibilities_zeros = convert_arrays_to_zeros(prev_board), convert_arrays_to_zeros(possiblities)
        if np.array_equal(prev_board_zeros, possibilities_zeros):
            break

        prev_board = possiblities.copy()
        

    return possiblities

# calculate solution

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

    while not arrays_equal(a, previous_a):
        previous_a = a.astype(object).copy()

        while True:
            new_a = findPossiblities(a)
            if arrays_equal(new_a, a):
                #print("ffjkldfsjflksdjflksdjflkdsfjskldjfskldjgklsdfjsdklfjdslkjfklsdjfslkdfjsdk")
                break
            a = new_a.astype(object).copy()
            #time.sleep(1)

        a = elimination(a)

    return a


def noSolution(possiblities):
    empty_arr = np.array([])
    for row in range(possiblities.shape[0]):
        for number in range(possiblities.shape[1]):
            value = possiblities[row, number]
            if np.array_equal(value, empty_arr):
                return True
    return False

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

def has_arrays(arr):
    for row in arr:
        for element in row:
            if isinstance(element, np.ndarray):
                return True
    return False


def findSolution(board, max_iterations):
    counter = 0
    orginal_possible = calculateSolution(board)
    #print(orginal_possible)
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

possibilitiess = findSolution(board, 7)

print(possibilitiess)

print("--- %s seconds ---" % (time.time() - start_time))