from game_components.table import Table


class Assistant:
    __table = None
    __mode = ["live", "extract"]
    __program_mode = None

    def __init__(self, table_mode):
        self.__program_mode = self.__mode[int(table_mode)]
        self.__table = Table(self.__program_mode)

    # main loop
    def start(self):
        # live
        if self.__program_mode == self.__mode[0]:
            while True:
                self.__table.analyze()

                # testing limit
                if self.__loop_limiter():
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
    mode = 1
    assistant = Assistant(mode)
    assistant.start()
