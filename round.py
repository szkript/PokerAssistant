from game_components.Enums.phase import Phase


class Round:
    phase = None
    hand = None
    middle = None
    dealer_position = None
    my_chip_amount = None

    def __init__(self, hand, middle, dealer_position, my_chip_amount=None):
        self.hand = hand
        self.middle = middle
        self.dealer_position = dealer_position
        self.__determine_phase()

    def __determine_phase(self):
        self.__preflop_criteriums()
        self.__phase_criteriums()
        print(self.phase)

    def __preflop_criteriums(self):
        if self.hand[0] is not None and self.hand[1] is not None and self.middle[0] is None:
            self.phase = Phase.PRE_FLOP

    def __phase_criteriums(self):
        if self.hand[0] is not None and self.hand[1] is not None and self.middle[0] is not None:
            if len(self.middle == 3):
                self.phase = Phase.FLOP
            elif len(self.middle == 4):
                self.phase = Phase.TURN
            elif len(self.middle == 5):
                self.phase = Phase.RIVER

