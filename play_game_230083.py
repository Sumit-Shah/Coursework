import random

# creating the board as 3*3 matrix
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"] #board variable to store 9 string
currentPlayer = "X" #first player should move.
winner = None #No winner till now.
gameRunning = True #No winner game still running 


# game board
def printBoard(board): #print board function defined.
    print(board[0] + " | " + board[1] + " | " + board[2]) #print 1st row  in board.
    print("---------") #line to seprate the two rows.
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):  #fuction defined playeutrInput taking single argument.
    inp = int(input("Select a spot 1-9: ")) #Select spot in 3*3matrix
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.") #if input is invalid .
1

# check for win or tie
def checkHorizontle(board):
    global winner  # declares a global variable "winner" that can be accessed and modified from within the function
    if board[0] == board[1] == board[2] and board[0] != "-": # checks if the first row has the same symbol in all three cells and is not empty
        winner = board[0]  # sets the winner variable to the winning symbol
        return True   # returns True to indicate a win
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner   # declares a global variable "winner" that can be accessed and modified from within the function
    if board[0] == board[3] == board[6] and board[0] != "-":  # checks if the first column has the same symbol in all three cells and is not empty
        winner = board[0]   # sets the winner variable to the winning symbol
        winner = board[0]
        return True  # returns True to indicate a win
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner # declares a global variable "winner" that can be accessed and modified from within the function
    if board[0] == board[4] == board[8] and board[0] != "-": # checks if the left-to-right diagonal has the same symbol in all three cells and is not empty
        winner = board[0] # sets the winner variable to the winning symbol
        return True # returns True to indicate a win
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning   # Calling a global variable "gameRunning" that can be accessed and modified from within the function
    if checkHorizontle(board):   # checks if there is a horizontal win on the board
        printBoard(board)   # prints the current state of the board
        print(f"The winner is {winner}!")   # prints a message announcing the winner
        gameRunning = False  # sets the gameRunning variable to False to indicate the end of the game

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):  
    global gameRunning  # Calling a global variable "gameRunning" that can be accessed and modified from within the function
    if "-" not in board: # checks if there are no more empty squares on the board
        printBoard(board)  # prints the current state of the board
        print("It is a tie!")  # prints a message announcing that the game has ended in a tie
        gameRunning = False   # sets the gameRunning variable to False to indicate the end of the game


# switch player
def switchPlayer():
    global currentPlayer   # calling a global variable "currentPlayer" that can be accessed and modified from within the function
    if currentPlayer == "X":   # checks if the current player is X
        currentPlayer = "O"   # sets the current player to O if it was X
    else:
        currentPlayer = "X" # sets the current player to X if it was O


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
