from enum import Enum


class Color(Enum):
    SPADES = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3

    @staticmethod
    def assign(suit):
        if suit == "spades":
            return Color.SPADES
        elif suit == "heart":
            return Color.HEART
        elif suit == "club":
            return Color.CLUB
        elif suit == "diamond":
            return Color.DIAMOND
