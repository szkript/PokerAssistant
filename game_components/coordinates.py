from utils import Utils


class Positions:
    __BASE_PATH = "game_components/positions/"
    card_width = 76
    card_width_resized = 37

    card_height = 106
    card_height_resized = 53

    # absolute position
    table_pos = None
    # relative pos from cropped table img(unmodified size)
    my_cards_pos = None
    # relative pos from cropped table img(unmodified size)
    middle_cards_pos = None
    dealer_chip = None
    players_position = None
    all_card_pos_calculated = None

    def __init__(self, num_of_players):
        # loading all variable from disk
        self.__init_vars(num_of_players)

    # load required coordinates from disk (pickle)
    def __init_vars(self, num_of_players):
        self.table_pos = Utils.load_vars(self.__BASE_PATH + "table_coordinates")
        self.all_card_pos_calculated = Utils.load_vars(self.__BASE_PATH + "all_card_calculated_coordinates")
        self.my_cards_pos = Utils.load_vars(self.__BASE_PATH + "all_hand_calculated_coordinates")
        self.middle_cards_pos = Utils.load_vars(self.__BASE_PATH + "all_middle_calculated_coordinates")
        self.players_position = Utils.load_vars(self.__BASE_PATH + f"player{num_of_players}_coordinates")
        self.dealer_chip = Utils.load_vars(self.__BASE_PATH + f"dealer_chip{num_of_players}_coordinates")
