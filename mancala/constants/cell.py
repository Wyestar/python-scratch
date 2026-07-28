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
