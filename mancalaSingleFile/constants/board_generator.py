from constants.cell import Cell, CellType


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
