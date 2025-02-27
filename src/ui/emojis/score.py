from __future__ import annotations

from enum import Enum


class ScoreRankIcon(Enum):
    F = "<:F_:504305414846808084>"
    D = "<:D_:504305448673869834>"
    C = "<:C_:504305500364472350>"
    B = "<:B_:504305539291938816>"
    A = "<:A_:504305622297083904>"
    S = "<:S_:504305656266752021>"
    SH = "<:SH:504305700445487105>"
    SHD = "<:SH:504305700445487105>"
    X = "<:X_:504305739209244672>"
    XH = "<:XH:504305771417305112>"
    XHD = "<:XH:504305771417305112>"
    SS = "<:X_:504305739209244672>"
    SSH = "<:XH:504305771417305112>"
    SSHD = "<:XH:504305771417305112>"

    def __init__(self, icon: str) -> None:
        self.icon: str = icon

    def __str__(self) -> str:
        return self.icon
