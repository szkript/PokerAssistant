from game_components.table import Table


class Assistant:
    table = None

    def __init__(self):
        self.table = Table()

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
    assistant.start()
