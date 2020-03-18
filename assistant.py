from game_components.table import Table


class Assistant:
    table = None
    __mode = ["live", "extract"]

    def __init__(self):
        # TODO: 2 way init
        # self.table = Table(self.__mode[0])
        # self.table.extractor()
        pass

    def extractor(self):
        self.table = Table(self.__mode[1])
        self.table.extractor()

    # main loop
    def start(self):
        while True:
            self.table.analyze()

            # testing limit
            if self.__loop_limiter():
                break

    def __loop_limiter(self):
        if self.table.get_img_count() > 10:
            return True
        return False


if __name__ == '__main__':
    assistant = Assistant()
    assistant.extractor()
    # assistant.start()
