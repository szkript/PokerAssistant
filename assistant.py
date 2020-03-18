from game_components.table import Table


class Assistant:
    table = None

    def __init__(self):
        self.table = Table()

    def start(self):
        while True:
            self.table.analyze()
            if self.table.get_img_count() > 10:
                break


if __name__ == '__main__':
    assistant = Assistant()
    assistant.start()
