class GameAnalyzer:
    __num_of_players = None
    __chances = None

    def __init__(self, number_of_players):
        self.__num_of_players = number_of_players

    def calculate_staring_chance(self, cards, dealer_pos):
        my_position = self.determine_position(dealer_pos)
        if cards[0].value == cards[1].value:
            pair_value = cards[0].value
            print("pair")
            if pair_value >= 7:
                return "playable"
            elif 6 >= pair_value >= 5:
                if my_position == "dealer":
                    return "playable"
            elif pair_value <= 4:
                if my_position == "dealer":
                    return "playable"
        return "fold"

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
