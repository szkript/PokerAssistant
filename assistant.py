from game_components.table import Table
from game_components.card import Card
from game_analyzer import GameAnalyzer
from assistant_run_mode import AssistantRunMode as Run_mode


class Assistant:
    __table = None
    __program_mode = None
    __LIMIT = False
    __cards = []

    def __init__(self, table_mode):
        self.__program_mode = Run_mode(table_mode)
        self.__table = Table(self.__program_mode)

    # main loop
    def start(self):
        # live
        if self.__program_mode == Run_mode.LIVE:
            game = GameAnalyzer(number_of_players=9)
            while True:
                self.__cards.clear()
                try:
                    table = self.__table.get_all(test_mode=True)
                except TypeError:
                    print("end of images")
                    break
                recognized_cards = table["hand"] + table["middle"]
                for card in recognized_cards:
                    prepared_card = Card(card)
                    self.__cards.append(prepared_card if prepared_card.value is not None else None)

                # new display
                self.__display_info(table["dealer_position"], game)
                # TODO: determine phase
                if self.__cards[0] is None and self.__cards[1] is None:  # hand
                    continue
                elif self.__cards[2] is not None:  # middle #1 card
                    continue
                # calculate pre flop chances
                move = game.calculate_staring_chance(self.__cards, table["dealer_position"])
                print(move)
                # testing limit
                if self.__LIMIT and self.__loop_limiter():
                    break
        # extract
        elif self.__program_mode == Run_mode.EXTRACT:
            self.__table.extractor()

    def __loop_limiter(self):
        if self.__table.get_img_count() > 10:
            return True
        return False

    def __display_info(self, dealer_position, game_analyzer):
        # middle_cards_txt = self.__cards[2:7]
        possible_phase = "Not determined"
        mid_txt = []
        for possible_phase, midcard in enumerate(self.__cards[2:7]):
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
