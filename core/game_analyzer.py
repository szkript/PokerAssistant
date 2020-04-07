from game_components.Enums.position import Position as Pos
from game_components.Enums.suggestion import Suggestion as Suggest
from core.result_handler import ResultHandler
from game_components.Enums.phase import Phase


class GameAnalyzer:
    __num_of_players = None
    __chances = None
    __current_round = None
    what_to_do = None  # always fold or check if nothing good comes to overwrite it

    def __init__(self, number_of_players):
        self.best = None
        self.__num_of_players = number_of_players

    def update_round(self, current_round):
        if self.__current_round is not None:
            if self.__current_round == current_round:  # if nothing to update then dont
                return

        self.__current_round = current_round

    # todo: calc chances
    def analyze_round(self):
        self.what_to_do = Suggest.FOLD  # reset
        # if no hand then return
        if self.__current_round is None:
            return
        if self.__current_round.hand[0] is None or self.__current_round.hand[1] is None:
            return

        if self.__current_round.phase == Phase.PRE_FLOP:
            self.what_to_do = self.calculate_staring_chance()
            print("suggestion: " + str(self.what_to_do))
            ResultHandler(self.what_to_do)

        # if any of them comes true just update the self.what_to_do with Suggestion
        # TODO: check for pair,drill,poker,full chances
        # self.__pair_check()
        # TODO: check for royal poker chances
        # TODO: check for straight chances
        # TODO: check for flush chances
        # TODO: check for straight flush chances

    def calculate_staring_chance(self):
        result = [self.__pair_validator(self.__current_round.hand, self.__current_round.my_position),
                  self.__suit_validator(self.__current_round.hand, self.__current_round.my_position)]
        # pair
        for res in result:
            if res is not None:
                return res
        return self.what_to_do

    # give back my position determined by seat and dealer_chip
    def determine_position(self, dealer_position):
        position = None
        if self.__num_of_players == 3:
            if dealer_position == 0:
                # best position
                position = Pos.DEALER  # (late)
            elif dealer_position == 1:
                position = Pos.SMALL_BLIND  # (early)
            elif dealer_position == 2:
                position = Pos.BIG_BLIND  # (mid)

        elif self.__num_of_players == 6:
            if dealer_position == 0:
                position = Pos.DEALER  # late
            elif 1 <= dealer_position <= 2:
                position = Pos.LATE
            elif dealer_position == 3:
                position = Pos.EARLY
            elif dealer_position == 4:
                position = Pos.EARLY  # early, bb
            elif dealer_position == 5:
                position = Pos.EARLY  # early, sb

        elif self.__num_of_players == 9:
            if dealer_position == 0:
                # best pos
                position = Pos.DEALER
            elif 1 <= dealer_position <= 3:
                position = Pos.LATE
            elif 4 <= dealer_position <= 5:
                position = Pos.MIDDLE
            elif 6 <= dealer_position <= 8:
                position = Pos.EARLY

        return position

    # for preflop only
    @staticmethod
    def __pair_validator(cards, my_position):
        if cards[0].value == cards[1].value:
            pair_value = cards[0].value
            if pair_value >= 7:
                return Suggest.PLAYABLE
            elif 6 >= pair_value >= 5:
                if my_position == Pos.DEALER:
                    return Suggest.PLAYABLE
            elif pair_value <= 4:
                if my_position == Pos.DEALER:
                    return Suggest.PLAYABLE

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
                if var_index is not None:
                    card_val = cards[var_index].value
                    if values == 14:  # ace
                        if card_val >= 10:
                            return Suggest.PLAYABLE
                        elif 9 >= card_val >= 6:
                            if my_position == Pos.DEALER:  # middle or late
                                return Suggest.PLAYABLE
                        elif 5 >= card_val >= 2:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 13:  # king
                        if card_val >= 10:
                            return Suggest.PLAYABLE
                        elif 9 == card_val:
                            if my_position == Pos.DEALER:  # middle or late only
                                return Suggest.PLAYABLE
                        elif 8 >= card_val >= 2:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 12:  # queen
                        if card_val >= 10:
                            return Suggest.PLAYABLE
                        elif 9 >= card_val >= 8:
                            if my_position == Pos.DEALER:  # middle or late
                                return Suggest.PLAYABLE

                    elif values == 11:  # jumbo
                        if card_val >= 10:
                            return Suggest.PLAYABLE
                        elif 8 == card_val:
                            if my_position == Pos.DEALER:  # middle or late
                                return Suggest.PLAYABLE
                        elif card_val == 7:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 10:
                        if card_val == 9:
                            return Suggest.PLAYABLE
                        elif card_val == 8:
                            if my_position == Pos.DEALER:  # mid or late
                                return Suggest.PLAYABLE
                        elif card_val == 7:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 9:
                        if card_val == 8:
                            if my_position == Pos.DEALER:  # mid or late
                                return Suggest.PLAYABLE
                        elif 7 >= card_val >= 6:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 8:
                        if 8 >= card_val >= 7:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 7:
                        if 6 >= card_val >= 5:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 6:
                        if card_val == 5:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE

                    elif values == 5:
                        if card_val == 4:
                            if my_position == Pos.DEALER:  # late only
                                return Suggest.PLAYABLE
                    # non suit
                    if cards[0].suit != cards[1].suit:
                        if values == 14:  # ace
                            if card_val >= 10:
                                return Suggest.PLAYABLE
                            elif 9 >= card_val >= 7:
                                if my_position == Pos.DEALER:  # middle or late
                                    return Suggest.PLAYABLE

                        elif values == 13:  # king
                            if card_val >= 11:
                                return Suggest.PLAYABLE
                            elif 10 == card_val:
                                if my_position == Pos.DEALER:  # middle or late only
                                    return Suggest.PLAYABLE
                            elif 9 == card_val:
                                if my_position == Pos.DEALER:  # late only
                                    return Suggest.PLAYABLE

                        elif values == 12:  # queen
                            if 11 >= card_val >= 9:
                                if my_position == Pos.DEALER:  # middle or late
                                    return Suggest.PLAYABLE

                        elif values == 11:  # jumbo
                            if card_val >= 10:
                                return Suggest.PLAYABLE
                            elif 8 >= card_val >= 7:
                                if my_position == Pos.DEALER:  # middle or late
                                    return Suggest.PLAYABLE

                        elif values == 10:
                            if 9 >= card_val >= 8:
                                if my_position == Pos.DEALER:  # mid or late
                                    return Suggest.PLAYABLE

                        elif values == 9:
                            if 8 >= card_val >= 7:
                                if my_position == Pos.DEALER:  # late only
                                    return Suggest.PLAYABLE

                        elif values == 8:
                            if card_val == 7:
                                if my_position == Pos.DEALER:  # late only
                                    return Suggest.PLAYABLE
