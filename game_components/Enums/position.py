from enum import Enum


class Position(Enum):
    DEALER = 0
    SMALL_BLIND = 1
    BIG_BLIND = 2
    EARLY = 3
    MIDDLE = 6
    LATE = 8

    def determine_position(self, dealer_position):
        if dealer_position == self.DEALER:
            return self.DEALER
        elif self.SMALL_BLIND <= dealer_position <= self.EARLY:
            return self.EARLY
        elif self.EARLY < dealer_position <= self.MIDDLE:
            return self.MIDDLE
        elif self.MIDDLE < dealer_position <= self.LATE:
            return self.LATE
