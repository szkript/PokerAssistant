class GameAnalyzer:
    __num_of_players = None
    __chances = None
    __pre_flop_chart = dict()

    def __init__(self, number_of_players):
        self.__num_of_players = number_of_players
        self.__init_pre_flop_chart()

    def calculate_staring_chance(self, cards, dealer_pos):
        my_position = self.determine_position(dealer_pos)

        pass

    def __init_pre_flop_chart(self):
        for index, value in enumerate(range(2, 15)):
            print(index+2, value)

    def determine_position(self, dealer_position):
        position = None
        if self.__num_of_players == 3:
            if dealer_position == 0:
                # best position
                position = "dealer"  # (late)
            elif dealer_position == 1:
                position = "small blind"  # (early)
            elif dealer_position == 2:
                position = "big blind"  # (early)
        elif self.__num_of_players == 9:
            pass

        return position
        position = "mid"
        position = "late"
        position = "early"
        position = "small blind"
        position = "big blind"
        position = "dealer"
