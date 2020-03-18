import pyautogui
import os
from os.path import join, isdir


class Table:
    __SCREENSHOT_FOLDER = "desktop_screenshots"
    __GATHERING_FOLDER = "image_gathering"
    __BASE_PATH = None

    hand = None
    middle = None
    dealer_position = None

    __classifier = None

    __img_count = 0
    __current_file_name = None

    def __init__(self):
        self.__set_folder_path()
        # create and set next folder for observe images
        # classifier init
        pass

    def get_img_count(self):
        return self.__img_count

    def analyze(self):
        self.__take_screenshot()

    def __take_screenshot(self):
        screenshot = pyautogui.screenshot()
        self.__current_file_name = f'{self.__BASE_PATH}\\desktop-{self.__img_count}.jpg'
        screenshot.save(self.__current_file_name)
        self.__img_count += 1

    def __set_folder_path(self):
        actual_path = join(os.getcwd(), self.__SCREENSHOT_FOLDER)
        if not isdir(actual_path):
            os.makedirs(actual_path)
        directories = [x[0] for x in os.walk(actual_path)]
        try:
            next_folder = str(int(directories[-1][-1]) + 1)
        except ValueError:
            next_folder = str(0)

        directory = actual_path + "\\" + next_folder
        print("The current working directory is %s" % directory + "\n")
        if not isdir(directory):
            os.makedirs(directory)

        self.__BASE_PATH = directory
