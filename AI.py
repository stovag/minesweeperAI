from string import ascii_lowercase
import random


def mineAI(board, size):
    #Check if there are open blocks
    S_open = 0;
    for i in range(size):
        for j in range(size):
            if(board[i][j] != ' '):
                S_open += 1;

    if(S_open == 0): #If all blocks are closed open the first one
        return 'a1'
    else:
        #For every block try to solve it
        for i in range(size):
            for j in range(size):
                if(board[i][j] != ' ') and (board[i][j] != 'F') and (board[i][j] != '0'):
                    #Check all neighbors
                    hidden_neighbors = check_neighbors(board,i,j,size);
                    flagged_neighbors = check_flags(board, i, j, size);

                    #Flagging
                    if(hidden_neighbors == int(board[i][j])):
                        print(flag_neighbors(board, i, j, size))
                        return flag_neighbors(board,i,j,size);
                    #Open safe closed
                    elif(flagged_neighbors == int(board[i][j])) and (hidden_neighbors != 0):
                        print(open_neighbors(board, i, j, size));
                        return open_neighbors(board, i, j, size);
                    else:
                        while(True):
                            y = random.randrange(j-1, j+1)
                            x = random.randrange(i-1, i+1)
                            if((x > 0) and (x < size) and (y > 0) and (y < size)):
                                return '{}{}'.format(ascii_lowercase[y], x)
                                break;

#Check for every neighbor if they're blank
def check_neighbors(board, i, j, size):
    s_hidden = 0;
    for x in range(i-1,i+1):
        for y in range(j-1,j+1):
            if((x >= 0) and (x <= size) and (y >= 0) and (y <= size)):
                if(board[x][y] == ' '):
                    s_hidden += 1;
    return s_hidden;

#Check for every neighborif they're flagged
def check_flags(board, i, j, size):
    s_flagged = 0;
    for x in range(i-1,i+1):
        for y in range(j-1,j+1):
            if((x >= 0) and (x <= size) and (y >= 0) and (y <= size)):
                if(board[x][y] == 'F'):
                    s_flagged += 1;
    return s_flagged;

#Flag near blank neighbors
def flag_neighbors(board,i,j,size):
    for x in range(i-1,i+1):
        for y in range(j-1, j+1):
            if((x >= 0) and (x <= size) and (y >= 0) and (y <= size)):
                if(board[x][y] == ' '):
                    print('{}{}f'.format(ascii_lowercase[y],x));
                    return '{}{}f'.format(ascii_lowercase[y],x);

#Open safe closed
def open_neighbors(board,i,j,size):
    for x in range(i-1,i+1):
        for y in range(j-1, j+1):
            if((x >= 0) and (x <= size) and (y >= 0) and (y <= size)):
                if(board[x][y] == ' '):
                    print('{}{}'.format(ascii_lowercase[y],x));
                    return '{}{}'.format(ascii_lowercase[y],x);
