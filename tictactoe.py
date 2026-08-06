# two player game. CPU later
# board is list of lists
# [
# [0, 1, 2]
# [0, 1, 2]
# [0 ,1, 2]
# ]
# each element is an object
# playFrom: p1 or p2 (default empty string)
# value: x or o (default empty string)
# numpadNotation: 1-9

# this 3x3 grid corresponds to numpad notation
# 7 8 9
# 4 5 6
# 1 2 3

import re

p1 = 'p1'
p2 = 'p2'

boardPositions = {
    "7": {"row": 0, "col": 0},
    "8": {"row": 0, "col": 1},
    "9": {"row": 0, "col": 2},
    "4": {"row": 1, "col": 0},
    "5": {"row": 1, "col": 1},
    "6": {"row": 1, "col": 2},
    "1": {"row": 2, "col": 0},
    "2": {"row": 2, "col": 1},
    "3": {"row": 2, "col": 2},
}


def createPosition(numpadNotation: str):
    pos = {"playFrom": "", "value": "", "numpadNotation": numpadNotation}

    return pos


def createBoard():
    numpads = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]

    top = []
    middle = []
    bottom = []

    tempPos = {}
    for i in range(0, len(numpads)):
        tempPos = createPosition(numpads[i])
        if i < 3:
            top.append(tempPos)
        elif i > 2 and i < 6:
            middle.append(tempPos)
        else:
            bottom.append(tempPos)

    board = [top, middle, bottom]

    return board


def showBoard(board: list):
    print("board show:")
    print(board)
    return


def checkGameEnded(board: list):
    # scan each possible 3 element line
    # for same element
    # do 9 scans?
    # save previous scan
    # can create optimized pathing
    # 753, 357 are same lines

    return False


# check play is valid and update board if so
def checkPlayIsValidAndUpdateBoard(board: list, input: str, currentPlayer: str, currentSymbol: str):
    # play = int(input)

    boardPos = boardPositions[input]
    boardPosRow = boardPos['row']
    boardPosCol = boardPos['col']
    # 1 = 2, 2

    boardPosFinal = board[boardPosRow][boardPosCol]

    # {"playFrom": "",
    # "value": "",
    # "numpadNotation": numpadNotation}

    if boardPosFinal["playFrom"] or boardPosFinal["value"]:
        print("pos already played")
        return False
    else:
        boardPosFinal["playFrom"] = currentPlayer
        boardPosFinal["value"] = currentSymbol
        return True



# retain order of positions played?
def startPlayerTurn(board: list, whosTurnIsIt: str, currentSymbol: str):
    currentPlayer = p1

    if whosTurnIsIt == p2:
        currentPlayer = p2

    # check player input is valid, not already chosen position
    playerInputIsNotValid = True
    while playerInputIsNotValid:
        inputPosition = input("Input Prompt >")
        # regex to ensure only 1-9
        pattern = r"^[1-9]$"
        inputMatch = re.match(pattern, inputPosition)
        validatedInput = ''
        # validatedInput = inputMatch if inputMatch.group(0) else ''
        if inputMatch:
            validatedInput = inputMatch.group(0)

        isPlayValid = checkPlayIsValidAndUpdateBoard(board, validatedInput, currentPlayer, currentSymbol)

        # TODO; add command menu input support
        if inputPosition == "help":
            print("show help menu")
        elif not validatedInput:
            print("Not a valid position to play, try another position.")
            continue

        if isPlayValid:
            print("play is valid and update board and move turn to next player")
            break;
        else:
            playerInputIsNotValid = False
    # update board with playFrom and value

    if currentPlayer is p1:
        return p2
    else:
        return p1


def startGameplay():
    board = createBoard()

    p1 = "p1"
    p2 = "p2"
    ex = "x"
    circle = "o"
    # TODO; allow players to choose their symbol
    ended = "ended"

    whosTurnIsIt = p1
    currentSymbol = ex
    gameIsOngoing = True

    while gameIsOngoing:
        nextPlayer = startPlayerTurn(board, whosTurnIsIt, currentSymbol)
        # nextPlayer needs to be a string 'p1' or 'p2'

        print("after player turn")
        print(board)
        isGameEnded = checkGameEnded(board)
        if isGameEnded:
            gameIsOngoing = False

        if nextPlayer == p2:
            whosTurnIsIt = p2
            currentSymbol = circle
        elif nextPlayer == p1:
            whosTurnIsIt = p1
            currentSymbol = ex


startGameplay()
