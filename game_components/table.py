import pyautogui
import os
from os.path import join, isdir


class Table:
    # folder paths
    __SCREENSHOT_FOLDER = "desktop_screenshots"
    __GATHERING_FOLDER = "image_gathering"
    __BASE_PATH = None

    # classifier model
    __classifier = None

    # for image counting
    __img_count = 0
    __current_file_name = None

    # built up objects from prediction
    hand = None
    middle = None
    dealer_position = None

    def __init__(self):
        self.__set_folder_path()
        # create and set next folder for observe images
        # classifier init

    # returns count of images
    def get_img_count(self):
        return self.__img_count

    # for testing
    def analyze(self):
        self.__take_screenshot()

    # take and save screenshot, sets file path in __current_file_name
    def __take_screenshot(self):
        screenshot = pyautogui.screenshot()
        self.__current_file_name = f'{self.__BASE_PATH}\\desktop-{self.__img_count}.jpg'
        screenshot.save(self.__current_file_name)
        self.__img_count += 1

    # sets and create new folder for every instance
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
        print(f"The current working directory is {directory} \n")
        if not isdir(directory):
            os.makedirs(directory)

        self.__BASE_PATH = directory
