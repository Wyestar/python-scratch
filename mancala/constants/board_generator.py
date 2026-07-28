from constants.cell import Cell, CellType


def mancalaBoardGenerator():
    lCell = Cell("l", 0, CellType.FIELD, None, None)
    kCell = Cell("k", 0, CellType.FIELD, None, lCell)
    jCell = Cell("j", 0, CellType.FIELD, None, kCell)
    iCell = Cell("i", 1, CellType.FIELD, None, jCell)
    hCell = Cell("h", 1, CellType.FIELD, None, iCell)
    gCell = Cell("g", 2, CellType.FIELD, None, hCell)

    p2Store = Cell("p1store", 0, CellType.STORE, None, gCell)

    fCell = Cell("f", 0, CellType.FIELD, gCell, p2Store)
    eCell = Cell("e", 1, CellType.FIELD, hCell, fCell)
    dCell = Cell("d", 0, CellType.FIELD, iCell, eCell)
    cCell = Cell("c", 1, CellType.FIELD, jCell, dCell)
    bCell = Cell("b", 0, CellType.FIELD, kCell, cCell)
    aCell = Cell("a", 1, CellType.FIELD, lCell, bCell)

    p2Store = Cell("p2store", 0, CellType.STORE, None, aCell)

    lCell.oppositeCell = aCell
    lCell.nextCell = p2Store
    kCell.oppositeCell = bCell
    jCell.oppositeCell = cCell
    iCell.oppositeCell = dCell
    hCell.oppositeCell = eCell
    gCell.oppositeCell = fCell

    return p2Store
