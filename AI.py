import random
from string import ascii_lowercase


def mineAI(currgrid, size):

    #input()

    #Create an empty Board
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append([])

    #Fill the board with the numbers from the currgrid or with " "
    for i in range(size):
        for j in range(size):
            board[i][j] = str(currgrid[i][j])

    #Check if there are open blocks
    S_open = 0
    for i in range(size):
        for j in range(size):
            if(board[i][j] != ' '):
                S_open += 1

    if(S_open == 0): #If all blocks are closed open the first one
        return 'a1'
    else:
        while True:
            #For every block try to solve it
            for i in range(size):
                for j in range(size):
                    if(board[i][j] != ' ') and (board[i][j] != 'F') and (board[i][j] != '0'):

                        #Check all neighbors
                        print("Check in i: ", i, " j: ", j)
                        hidden_neighbors = check_neighbors(board, i, j, size)
                        flagged_neighbors = check_flags(board, i, j, size)
                        bombs = hidden_neighbors + flagged_neighbors

                        if hidden_neighbors > 0:
                            #Open safe closed
                            if(flagged_neighbors == int(board[i][j])):
                                return open_neighbors(board, i, j, size)
                            #Flagging
                            elif bombs == int(board[i][j]):
                                return flag_neighbors(board, i, j, size)
                            else:
                                print("Nothing to do in i: ", i, "j: ", j)
            return "You suck at coding 1"


#Check for every neighbor if they're blank
def check_neighbors(board, i, j, size):
    s_hidden = 0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            try:
                if((x >= 0) and (x <= size) and (y >= 0) and (y <= size)):
                    if board[x][y] == " ":
                        s_hidden += 1
            except:
                break
    return s_hidden


#Check for every neighborif they're flagged
def check_flags(board, i, j, size):
    s_flagged = 0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            try :
                if((x >= 0) and (x <= size-1) and (y >= 0) and (y <= size-1)):
                    if board[x][y] == "F":
                        s_flagged += 1
            except:
                break
    return s_flagged


#Flag near blank neighbors
def flag_neighbors(board,i,j,size):
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            try:
                if((x >= 0) and (x <= size) and (y >= 0) and (y <= size)):
                    if board[x][y] == " ":
                        return ('{}{}f'.format(ascii_lowercase[y],x+1))
            except:
                break
    return "You suck at coding 2"


#Open safe closed
def open_neighbors(board, i, j, size):
    for x in range(i-1,i+2):
        for y in range(j-1, j+2):
            try:
                if((x >= 0) and (x <= size) and (y >= 0) and (y <= size)):
                    if board[x][y] == " ":
                        return ('{}{}'.format(ascii_lowercase[y],x+1))
            except:
                break
    return "You suck at coding 3"
