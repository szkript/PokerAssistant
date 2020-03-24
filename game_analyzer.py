class GameAnalyzer:
    __num_of_players = None
    __chances = None

    def __init__(self, number_of_players):
        self.__num_of_players = number_of_players

    def calculate_staring_chance(self, cards, dealer_pos):
        result = []
        my_position = self.determine_position(dealer_pos)
        # pair
        result.append(self.__pair_validator(cards, my_position))
        result.append(self.__suit_validator(cards, my_position))

        return result

    # give back my position determined by seat and dealer_chip
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

    @staticmethod
    def __pair_validator(cards, my_position):
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

    @staticmethod
    def __suit_validator(cards, my_position):
        if cards[0].suit == cards[1].suit:
            values = 14

            while values > 1:
                var_index = None
                if cards[0].value == values:
                    var_index = 1
                elif cards[1].value == values:
                    var_index = 0

                values -= 1
                card_val = cards[var_index]
                if var_index is not None:
                    if values == 14:  # ace
                        if card_val >= 10:
                            return "playable"
                        elif 9 >= card_val >= 6:
                            if my_position == "dealer":  # middle or late
                                return "playable"
                        elif 5 >= card_val >= 2:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 13:  # king
                        if card_val >= 10:
                            return "playable"
                        elif 9 == card_val:
                            if my_position == "dealer":  # middle or late only
                                return "playable"
                        elif 8 >= card_val >= 2:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 12:  # queen
                        if card_val >= 10:
                            return "playable"
                        elif 9 >= card_val >= 8:
                            if my_position == "dealer":  # middle or late
                                return "playable"

                    elif values == 11:  # jumbo
                        if card_val >= 10:
                            return "playable"
                        elif 8 == card_val:
                            if my_position == "dealer":  # middle or late
                                return "playable"
                        elif card_val == 7:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 10:
                        if card_val == 9:
                            return "playable"
                        elif card_val == 8:
                            if my_position == "dealer":  # mid or late
                                return "playable"
                        elif card_val == 7:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 9:
                        if card_val == 8:
                            if my_position == "dealer":  # mid or late
                                return "playable"
                        elif 7 >= card_val >= 6:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 8:
                        if 8 >= card_val >= 7:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 7:
                        if 6 >= card_val >= 5:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 6:
                        if card_val == 5:
                            if my_position == "dealer":  # late only
                                return "playable"

                    elif values == 5:
                        if card_val == 4:
                            if my_position == "dealer":  # late only
                                return "playable"

        elif cards[0].suit != cards[1].suit:
            pass

        else:
            return "unplayable"
