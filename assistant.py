from game_components.table import Table
from game_components.card import Card
from game_analyzer import GameAnalyzer


class Assistant:
    __table = None
    __mode = ["live", "extract"]
    __program_mode = None
    __LIMIT = False
    __cards = []

    def __init__(self, table_mode):
        self.__program_mode = self.__mode[int(table_mode)]
        self.__table = Table(self.__program_mode)

    # main loop
    def start(self):
        # live
        if self.__program_mode == self.__mode[0]:
            game = GameAnalyzer(3)
            while True:
                self.__cards.clear()
                table = self.__table.get_all(test_mode=True)
                recognized_cards = table["hand"] + table["middle"]
                for card in recognized_cards:
                    prepared_card = Card(card)
                    self.__cards.append(prepared_card if prepared_card.value is not None else None)

                # TODO: determine phase
                # calculate pre flop chances
                game.calculate_staring_chance(self.__cards, table["dealer_position"])

                # testing limit
                if self.__LIMIT and self.__loop_limiter():
                    break
        # extract
        elif self.__program_mode == self.__mode[1]:
            self.__table.extractor()

    def __loop_limiter(self):
        if self.__table.get_img_count() > 10:
            return True
        return False


if __name__ == '__main__':
    # mode = input("0 - live \n1 - extract\n")
    mode = 0
    assistant = Assistant(mode)
    assistant.start()
