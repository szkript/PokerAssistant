from game_components.Enums.color import Color


class Card:
    __original_name = None
    suit = None
    value = None
    display_name = None

    def __init__(self, name):
        if name == "trash" or name == "background" or name == "nothing":
            return
        self.__original_name = name
        self.set_fields(name)

    def set_fields(self, name):
        separator = str(name).index("_")
        suit = name[:separator]
        self.suit = Color.assign(suit)
        value = name[separator + 1:]
        if value == 'j':
            self.value = 11
        elif value == 'q':
            self.value = 12
        elif value == 'k':
            self.value = 13
        elif value == 'a':
            self.value = 14
        else:
            self.value = int(value)

        self.display_name = f"{self.suit}|{self.value}"

    def __str__(self):
        return f"{self.display_name}"
