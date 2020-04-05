from game_components.Enums.phase import Phase


class Round:
    phase = None
    hand = None
    middle = None
    dealer_position = None
    my_chip_amount = None
    my_position = None
    image_index = None
    # players = List[player]
    in_game = None
    # TODO: track preflop bets, if there are anyone who raise the big blind

    def __init__(self, hand, middle, dealer_position, my_position, image_index, my_chip_amount=None):
        self.hand = hand
        self.middle = middle
        self.dealer_position = dealer_position
        self.my_position = my_position
        self.__determine_phase()
        self.image_index = image_index

    def __determine_phase(self):
        self.__preflop_criteriums()
        self.__phase_criteriums()

    def __preflop_criteriums(self):
        if self.hand[0] is not None and self.hand[1] is not None and self.middle[0] is None:
            self.phase = Phase.PRE_FLOP

    def __phase_criteriums(self):
        if self.hand[0] is not None and self.hand[1] is not None and self.middle[0] is None:
            self.phase = Phase.PRE_FLOP
        middle_count = len(self.middle) - self.middle.count(None)
        if middle_count == 3:
            self.phase = Phase.FLOP
        elif middle_count == 4:
            self.phase = Phase.TURN
        elif middle_count == 5:
            self.phase = Phase.RIVER

        if self.hand[0] is not None and self.hand[1] is not None:
            self.in_game = True
