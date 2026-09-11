import sys

from enum import Enum
from typing import Optional


class CellType(Enum):
    FIELD = 1
    STORE = 2


class Cell:
    def __init__(
        self,
        marker: str,
        harvest: int,
        type: CellType,
        oppositeCell: Optional["Cell"] = None,
        nextCell: Optional["Cell"] = None,
    ):
        self.marker = marker
        self.harvest = harvest
        self.type = type
        # .type.name = FIELD/STORE OR .type.value = 1/2
        self.oppositeCell = oppositeCell
        self.nextCell = nextCell


def mancalaBoardGenerator():
    lCell = Cell("l", 4, CellType.FIELD, None, None)
    kCell = Cell("k", 4, CellType.FIELD, None, lCell)
    jCell = Cell("j", 4, CellType.FIELD, None, kCell)
    iCell = Cell("i", 4, CellType.FIELD, None, jCell)
    hCell = Cell("h", 4, CellType.FIELD, None, iCell)
    gCell = Cell("g", 4, CellType.FIELD, None, hCell)

    p2Store = Cell("p1store", 0, CellType.STORE, None, gCell)

    fCell = Cell("f", 4, CellType.FIELD, gCell, p2Store)
    eCell = Cell("e", 4, CellType.FIELD, hCell, fCell)
    dCell = Cell("d", 4, CellType.FIELD, iCell, eCell)
    cCell = Cell("c", 4, CellType.FIELD, jCell, dCell)
    bCell = Cell("b", 4, CellType.FIELD, kCell, cCell)
    aCell = Cell("a", 4, CellType.FIELD, lCell, bCell)

    p2Store = Cell("p2store", 0, CellType.STORE, None, aCell)

    lCell.oppositeCell = aCell
    lCell.nextCell = p2Store
    kCell.oppositeCell = bCell
    jCell.oppositeCell = cCell
    iCell.oppositeCell = dCell
    hCell.oppositeCell = eCell
    gCell.oppositeCell = fCell

    return p2Store


# constants
p1 = "p1"
p2 = "p2"
p1store = "p1store"
p2store = "p2store"
p1Fields = ["a", "b", "c", "d", "e", "f"]
p2Fields = ["g", "h", "i", "j", "k", "l"]
p1Prompt = "Player 1, enter a field from A to F > "
p2Prompt = "Player 2, enter a field from G to L > "

# stats
# index 0: total captures made
# index 1: sum of all capture yields
# subtract count from total to get amount truly captured
p1CaptureStats = [0, 0]
p2CaptureStats = [0, 0]
# p1CapturedCounter = 0
# p1CapturedYield = 0
# p2CapturedCounter = 0
# p2CapturedYield = 0

commandListPrompt = "Enter 'help' for a list of commands."
commandList = "show current board: 'show board' or exit menu: 'exit'"
# show capture count: 'capture count'

# display board status
def checkBoard(board: Cell, lastCheck):
    pointer = board

    stores = p1store + p2store

    if lastCheck == True:
        for i in range(14):
            if (pointer.harvest > 0) and (pointer.marker not in stores):
                print(
                    pointer.marker
                    + " - "
                    + str(pointer.harvest)
                    + " - was collected and added to store"
                )
            else:
                print(pointer.marker + " - " + str(pointer.harvest))

            pointer = pointer.nextCell
    else:
        for i in range(14):
            print(pointer.marker + " - " + str(pointer.harvest))
            pointer = pointer.nextCell


# navigate to either store and update harvest with capture
# return updated board
def getAndUpdatePlayerStore(
    currentStore: str, capturedHarvest: int, currentBoard: Cell
):
    pointer = currentBoard

    isTraversing = True

    while isTraversing:
        if pointer.marker == currentStore:
            pointer.harvest = pointer.harvest + capturedHarvest
            isTraversing = False
        else:
            pointer = pointer.nextCell

    return pointer


# update counter and yield of player after a capture
# a capture where opposite cell has zero harvest still increments counter
def updatePlayerCaptureStats(currentPlayer: str, capYield: int):
    if currentPlayer == p1:
        p1CaptureStats[0] = p1CaptureStats[0] + 1
        p1CaptureStats[1] = p1CaptureStats[1] + capYield
    elif currentPlayer == p2:
        p2CaptureStats[0] = p2CaptureStats[0] + 1
        p2CaptureStats[1] = p2CaptureStats[1] + capYield

    return {"p1CaptureStats": p1CaptureStats, "p2CaptureStats": p2CaptureStats}


# navigate to the field a player has played
# return Cell if valid
def findPlayedCell(playedCell: str, currentBoard: Cell):
    pointer = currentBoard
    playedCellFound = None
    isTraversing = True

    while isTraversing:
        if pointer.marker == playedCell:
            playedCellFound = pointer
            isTraversing = False
        else:
            pointer = pointer.nextCell

    return playedCellFound


# helper method for checking if game is ended
# return boolean indicating if a player's fields are empty
def checkEmptyFields(startCell: Cell):
    pointer = startCell
    allPlayerFieldsAreEmpty = True
    counter = 0

    while allPlayerFieldsAreEmpty and counter < 6:
        if pointer.harvest > 0:
            allPlayerFieldsAreEmpty = False
            break
        else:
            counter = counter + 1
            pointer = pointer.nextCell

    return allPlayerFieldsAreEmpty


# collect all harvest from a starting cell
def collectHarvestsOnASide(startCell: Cell):
    pointer = startCell
    counter = 0
    sum = 0
    while counter < 6:
        sum = sum + pointer.harvest
        # pointer.collected = True
        pointer = pointer.nextCell
        counter = counter + 1

    return sum


# checks game status if it should continue or is over
# returns boolean indicating game status
def checkGameEnded(currentBoard: Cell):
    p1StartCell = currentBoard.nextCell
    p2StartCell = currentBoard.nextCell.nextCell.nextCell.nextCell.nextCell.nextCell.nextCell.nextCell

    isP1FieldsEmpty = checkEmptyFields(p1StartCell)
    isP2FieldsEmpty = checkEmptyFields(p2StartCell)

    # collect logic
    if isP1FieldsEmpty or isP2FieldsEmpty:
        p1CollectionSum = collectHarvestsOnASide(p1StartCell)
        getAndUpdatePlayerStore(p1store, p1CollectionSum, currentBoard)

        p2CollectionSum = collectHarvestsOnASide(p2StartCell)
        getAndUpdatePlayerStore(p2store, p2CollectionSum, currentBoard)

    return isP1FieldsEmpty or isP2FieldsEmpty


# main method that updates board, store/harvest counts, and captures
# returns string (currentPlayer)
def startPlayerTurn(whosTurnIsIt: str, currentBoard: Cell):
    currentPlayer = p1
    currentStore = p1store
    currentFields = p1Fields
    currentPrompt = p1Prompt

    if whosTurnIsIt == p2:
        currentPlayer = p2
        currentStore = p2store
        currentFields = p2Fields
        currentPrompt = p2Prompt

    playerInputIsNotValid = True
    playedCell = ""
    playedCellFound = None

    # validate player input and show relevant prompts
    # start input logic while loop
    while playerInputIsNotValid:
        print(commandListPrompt)
        playedCell = input("{}".format(currentPrompt)).strip()
        playedCellLower = playedCell.lower()
        isPlayValid = playedCellLower in currentFields

        playerIsInHelpMenu = False

        if playedCellLower == "help":
            playerIsInHelpMenu = True
            while playerIsInHelpMenu:
                print(commandList)
                playerCommand = input("command > ").strip()
                playerCommandLower = playerCommand.lower()
                if playerCommandLower == "show board":
                    checkBoard(currentBoard, False)
                elif playerCommandLower == "test":
                    print("command test")
                elif playerCommandLower == "exit":
                    playerIsInHelpMenu = False
        elif not isPlayValid:
            print("This field is not on your side, please chose another.")
            continue

        if isPlayValid:
            playedCellFound = findPlayedCell(playedCellLower, currentBoard)
            if playedCellFound.harvest == 0:
                print("This field has no harvest, please chose another.")
                playedCellFound = None
                isPlayValid = False
                continue
            else:
                playerInputIsNotValid = False
    # end input logic while loop

    nextCellTemp = playedCellFound.nextCell
    lastCell = None

    # disperse logic
    while playedCellFound.harvest > 0:
        nextCellTemp.harvest += 1
        lastCell = nextCellTemp
        nextCellTemp = nextCellTemp.nextCell
        playedCellFound.harvest -= 1

    # TODO: fancy heatmap capture tracker of which fields are
    # td2: most often involved and have highest yield from captures
    # capture logic
    if (lastCell.marker in currentFields) and (lastCell.harvest == 1):
        capturedHarvest = lastCell.oppositeCell.harvest + lastCell.harvest

        updatePlayerCaptureStats(currentPlayer, capturedHarvest)

        lastCell.harvest = 0
        lastCell.oppositeCell.harvest = 0

        getAndUpdatePlayerStore(currentStore, capturedHarvest, currentBoard)

    # next turn logic
    if currentPlayer == p1:
        if lastCell.marker == p1store:
            currentPlayer = p1
        else:
            currentPlayer = p2
    elif currentPlayer == p2:
        if lastCell.marker == p2store:
            currentPlayer = p2
        else:
            currentPlayer = p1

    return currentPlayer


def mancala():
    board = mancalaBoardGenerator()
    print("in main - first board check ----")
    checkBoard(board, False)

    whosTurnIsIt = p1
    gameIsOngoing = True

    while gameIsOngoing:
        while whosTurnIsIt == p1:
            nextPlayer = startPlayerTurn(whosTurnIsIt, board)
            isGameEnded = checkGameEnded(board)
            # print("in main - p1 end ----")
            # checkBoard(board, False)
            if isGameEnded:
                gameIsOngoing = False
                break
            if nextPlayer == p2:
                whosTurnIsIt = p2
                break

        while whosTurnIsIt == p2:
            nextPlayer = startPlayerTurn(whosTurnIsIt, board)
            isGameEnded = checkGameEnded(board)
            # print("in main - p2 end ----")
            # checkBoard(board, False)
            if isGameEnded:
                gameIsOngoing = False
                break
            if nextPlayer == p1:
                whosTurnIsIt = p1
                break

    print("in main - last board check ----")
    checkBoard(board, True)

    # capture stats
    captureStatsAtEnd = updatePlayerCaptureStats("", 0)

    p1CapturedCounter = captureStatsAtEnd["p1CaptureStats"][0]
    p1CapturedYield = captureStatsAtEnd["p1CaptureStats"][1]
    p1CapturedActual = p1CapturedYield - p1CapturedCounter

    p2CapturedCounter = captureStatsAtEnd["p2CaptureStats"][0]
    p2CapturedYield = captureStatsAtEnd["p2CaptureStats"][1]
    p2CapturedActual = p2CapturedYield - p2CapturedCounter

    # game end results
    p1Result = getAndUpdatePlayerStore(p1store, 0, board)
    p2Result = getAndUpdatePlayerStore(p2store, 0, board)

    if p1Result.harvest > p2Result.harvest:
        print("Player 1 wins!")
        print("P1 store: ", p1Result.harvest)
        print("P2 store: ", p2Result.harvest)
    else:
        print("Player 2 wins!")
        print("P1 store: ", p1Result.harvest)
        print("P2 store: ", p2Result.harvest)


mancala()
