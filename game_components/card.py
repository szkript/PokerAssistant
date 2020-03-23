class Card:
    __original_name = None
    suit = None
    value = None

    def __init__(self, name):
        if name == "trash":
            return
        self.__original_name = name
        self.set_fields(name)

    def set_fields(self, name):
        separator = str(name).index("_")
        self.suit = name[:separator]
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

