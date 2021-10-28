from dataclasses import dataclass, asdict
from math import ceil


@dataclass
class Stats:
    INT: int
    REF: int
    DEX: int
    TECH: int
    COOL: int
    WILL: int
    LUCK: int
    MOVE: int
    BODY: int
    EMP: int

    @property
    def max_hp(self):
        return 5 * ceil((self.BODY + self.WILL) / 2) + 10

    def to_dict(self):
        return asdict(self)

