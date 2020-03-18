import pyautogui


class Table:
    SCREENSHOT_FOLDER = "desktop_screenshots/"
    GATHERING_FOLDER = "image_gathering/"

    hand = None
    middle = None
    dealer_position = None

    __classifier = None

    __img_count = 0
    __current_file_name = ""

    def __init__(self):
        # create and set next folder for observe images
        # classifier init
        pass

    def __take_screenshot(self):
        screenshot = pyautogui.screenshot()
        self.__current_file_name = f'{self.SCREENSHOT_FOLDER}desktop-{self.__img_count}.jpg'
        screenshot.save(self.__current_file_name)
        self.__img_count += 1
