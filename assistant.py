from game_components.table import Table
from game_components.card import Card
from core.game_analyzer import GameAnalyzer
from core.assistant_run_mode import AssistantRunMode as Run_mode
from game_components.round import Round


class Assistant:
    # main switch
    __RUN_MODE = Run_mode.EXTRACT  # test
    __num_of_players = 6

    __table = None
    __game = None
    __program_mode = None
    __LIMIT = False
    __cards = []

    round_history = []

    def __init__(self):
        self.__loop_limit_count = 30
        self.__program_mode = Run_mode(self.__RUN_MODE)
        self.__table = Table(self.__program_mode, self.__num_of_players)
        self.__game = GameAnalyzer(number_of_players=self.__num_of_players)
        print(self.__program_mode)

    # main loop
    def start(self):
        # live
        if self.__program_mode == Run_mode.LIVE:
            while True:
                self.__handle_data_gathering()
                self.__game.analyze_round()
                # todo: only save images with changes
                # todo: new images must contain new info

        # extract
        # TODO: create control or extract mode
        elif self.__program_mode == Run_mode.EXTRACT:
            while True:
                try:
                    # with test mode its iterating through a given folder of images and simulate realtime work
                    # on existing images
                    self.__handle_data_gathering()
                    self.__image_operations()
                except TypeError as e:
                    print(e)
                    print("end of images")
                    break
                # testing limit
                if self.__LIMIT and self.__loop_limiter():
                    break

    # Inner methods
    def __handle_data_gathering(self):
        self.__cards.clear()
        # table contains recognized table data
        table = self.__table.get_all(self.__RUN_MODE)
        table["my_position"] = self.__game.determine_position(table["dealer_position"])
        recognized_cards = table["hand"] + table["middle"]
        for card in recognized_cards:
            prepared_card = Card(card)
            self.__cards.append(prepared_card if prepared_card.value is not None else None)

        _round = Round(self.__cards[:2], self.__cards[2:7], table["dealer_position"], table["my_position"],
                       self.__table.get_current_img_count())

        # relocate history into game analyzer?
        history_len = len(self.round_history)
        self.__update_history(_round)
        # if same round skip
        if len(self.round_history) <= history_len:
            return

        # # TODO: determine move
        # # calculate pre flop chances
        # if _round.phase is Phase.PRE_FLOP:
        #     move = self.__game.calculate_staring_chance(self.__cards, table["my_position"])
        #     ResultHandler(move)
        #     print(move)

    # game history handler
    def __update_history(self, _round):
        try:
            if _round.phase is not None or _round != self.round_history[-1]:
                # a collected well managed display needs with more info
                # TODO: replace the below one with the above specified
                self.__game.update_round(_round)
                self.round_history.append(_round)
                self.__display_info()
            # return before further calculations begin
            if self.__RUN_MODE is Run_mode.LIVE:
                if _round.phase is None:
                    self.__table.drop_image()

        except IndexError:
            self.round_history.append(_round)

    def __loop_limiter(self):
        if self.__table.get_current_img_count() > self.__loop_limit_count:
            return True
        return False

    # should be displayed in game analyzer
    def __display_info(self):
        # get current round data(last added)
        current_round = self.round_history[-1]
        # get current round phase
        possible_phase = current_round.phase
        mid_txt = []
        for midcard in self.__cards[2:7]:
            if midcard is None:
                break
            mid_txt.append(midcard.display_name)
        print(f"""
hand: {self.__cards[0]}, {self.__cards[1]} || my position: {current_round.my_position}
middle : {", ".join(mid_txt)}
phase : {possible_phase}
""")

    def __image_operations(self):
        # asking for option
        self.__table.menu()


if __name__ == '__main__':
    assistant = Assistant()
    assistant.start()
