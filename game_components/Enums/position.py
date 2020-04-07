from enum import Enum


class Position(Enum):
    SMALL_BLIND = 0
    BIG_BLIND = 1
    EARLY = 2
    MIDDLE = 3
    LATE = 4
    DEALER = 5

    # def determine_position(self, dealer_position):
    #     if dealer_position == self.DEALER:
    #         return self.DEALER
    #     elif self.SMALL_BLIND <= dealer_position <= self.EARLY:
    #         return self.EARLY
    #     elif self.EARLY < dealer_position <= self.MIDDLE:
    #         return self.MIDDLE
    #     elif self.MIDDLE < dealer_position <= self.LATE:
    #         return self.LATE

    def __str__(self):
        return self.name
