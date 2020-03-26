from enum import Enum


class Suggestion(Enum):
    FOLD = 0
    CHECK = 1
    BET = 2
    RAISE = 3
    PLAYABLE = 4

    def __str__(self):
        return self.name
