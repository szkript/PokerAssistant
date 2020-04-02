from game_components.table import Table
from game_components.card import Card
from game_analyzer import GameAnalyzer
from assistant_run_mode import AssistantRunMode as Run_mode
from round import Round
from game_components.Enums.phase import Phase


class Assistant:
    __table = None
    __game = None
    __program_mode = None
    __LIMIT = True
    __cards = []
    __num_of_players = 3
    round_history = []

    def __init__(self, table_mode):
        self.__loop_limit_count = 30
        self.__program_mode = Run_mode(table_mode)
        self.__table = Table(self.__program_mode, self.__num_of_players)
        self.__game = GameAnalyzer(number_of_players=self.__num_of_players)

    # main loop
    def start(self):
        # live
        if self.__program_mode == Run_mode.LIVE:
            while True:
                self.__handle_data_gathering()
                # todo: only save images with changes
                # input()  # until repeatable screenshot will be ignored

        # extract
        # TODO: create control or extract mode
        elif self.__program_mode == Run_mode.EXTRACT:
            while True:
                try:
                    # with test mode its iterating through a given folder of images and simulate realtime work
                    # on existing images
                    self.__handle_data_gathering(test_mode=True)
                except TypeError:
                    print("end of images")
                    break
                # testing limit
                if self.__LIMIT and self.__loop_limiter():
                    break

    # Inner methods
    def __handle_data_gathering(self, test_mode=False):
        self.__cards.clear()
        table = self.__table.get_all(test_mode)
        recognized_cards = table["hand"] + table["middle"]
        for card in recognized_cards:
            prepared_card = Card(card)
            self.__cards.append(prepared_card if prepared_card.value is not None else None)

        _round = Round(self.__cards[:2], self.__cards[2:7], table["dealer_position"])
        try:
            if _round.phase is not None or _round != self.round_history[-1]:
                self.round_history.append(_round)
                # new display
                self.__display_info(table["dealer_position"], self.__game)
            else:
                # return before further calculations begin
                return
        except IndexError:
            self.round_history.append(_round)

        self.__display_info(table["dealer_position"], self.__game)
        # TODO: determine move
        # calculate pre flop chances
        if _round.phase is Phase.PRE_FLOP:
            move = self.__game.calculate_staring_chance(self.__cards, table["dealer_position"])
            print(move)

    def __loop_limiter(self):
        if self.__table.get_img_count() > self.__loop_limit_count:
            return True
        return False

    def __display_info(self, dealer_position, game_analyzer):
        # get current round phase(last added)
        possible_phase = self.round_history[-1].phase
        mid_txt = []
        for midcard in self.__cards[2:7]:
            if midcard is None:
                break
            mid_txt.append(midcard.display_name)
        print(f"""
hand: {self.__cards[0]}, {self.__cards[1]} || my position: {game_analyzer.determine_position(dealer_position)}
middle : {", ".join(mid_txt)}
phase : {possible_phase}
""")


if __name__ == '__main__':
    # mode = input("0 - live \n1 - extract\n")
    mode = 0
    assistant = Assistant(mode)
    assistant.start()
