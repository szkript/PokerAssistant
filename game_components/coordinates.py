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
        dealer_chip = [dict() for i in range(num_of_players)]
        # loading all variable from disk
        self.__init_vars()

        if num_of_players == 9:
            dealer_chip = Utils.load_vars(self.__BASE_PATH + "dealer_chip9_coordinates")
        elif num_of_players == 3:
            dealer_chip = Utils.load_vars(self.__BASE_PATH + "dealer_chip3_coordinates")
        elif num_of_players == 6:  # elv jó
            dealer_chip = Utils.load_vars(self.__BASE_PATH + "dealer_chip6_coordinates")
        self.dealer_chip = dealer_chip

    # load required coordinates from disk (pickle)
    def __init_vars(self):
        self.table_pos = Utils.load_vars(self.__BASE_PATH + "table_coordinates")
        self.all_card_pos_calculated = Utils.load_vars(self.__BASE_PATH + "all_card_calculated_coordinates")
        self.players_position = Utils.load_vars(self.__BASE_PATH + "player9_coordinates")
        self.my_cards_pos = Utils.load_vars(self.__BASE_PATH + "all_hand_calculated_coordinates")
        self.middle_cards_pos = Utils.load_vars(self.__BASE_PATH + "all_middle_calculated_coordinates")
