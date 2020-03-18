from game_components.table import Table


class Assistant:
    __table = None
    __mode = ["live", "extract"]

    def __init__(self, table_mode):
        self.__table = Table(self.__mode[int(table_mode)])

    # main loop
    def start(self):
        while True:
            self.__table.analyze()

            # testing limit
            if self.__loop_limiter():
                break

    def __loop_limiter(self):
        if self.__table.get_img_count() > 10:
            return True
        return False


if __name__ == '__main__':
    # mode = input("0 - live \n1 - extract\n")
    assistant = Assistant(1)
    # assistant.start()
