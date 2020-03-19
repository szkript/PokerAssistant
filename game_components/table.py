from utils import Utils
import pyautogui
import os
import cv2
from os.path import join, isdir
from game_components import positions as position


class Table:
    # folder paths
    __SCREENSHOT_FOLDER = "desktop_screenshots"
    __DESKTOP_IMAGE_FOLDERS_NUM = 0
    __GATHERING_FOLDER = "image_gathering"
    __BASE_PATH = None

    # image related
    __table_img_loaded = None

    # classifier model
    __classifier = None

    # for image counting
    __img_count = 0
    __current_file_name = None

    # built up objects from prediction
    hand = None
    middle = None
    dealer_position = None

    def __init__(self, mode):
        # classifier init
        if mode == "live":
            self.__set_folder_path()
        elif mode == "extract":
            Utils.validate_path(self.__GATHERING_FOLDER)
            self.__DESKTOP_IMAGE_FOLDERS_NUM = Utils.get_directories(self.__SCREENSHOT_FOLDER).__len__() - 1

    # experimental
    def extractor(self):
        self.__read_images()

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
        directories = Utils.get_directories(actual_path)
        try:
            next_folder = str(int(directories[-1][-1]) + 1)
        except ValueError:
            next_folder = str(0)

        directory = actual_path + "\\" + next_folder
        print(f"The current working directory is {directory} \n")
        if not isdir(directory):
            os.makedirs(directory)

        self.__BASE_PATH = directory

    def __load_image_to_memory(self):
        self.__table_img_loaded = cv2.imread(self.__current_file_name)

    # crop image at given params
    @staticmethod
    def crop_at_pos(img, coordinates):
        return img[coordinates["y"]:coordinates["y"] + coordinates["h"],
               coordinates["x"]:coordinates["x"] + coordinates["w"]]

    # reads existing images from given folder
    def __read_images(self):
        if self.__DESKTOP_IMAGE_FOLDERS_NUM < 0:
            print("no data to examine, gather some and come back later")
            return

        selected_folder = input(f"choose folder from 0 to {self.__DESKTOP_IMAGE_FOLDERS_NUM - 1}:\n")
        while True:
            try:
                print(f'image num {self.__img_count}')
                # building file name
                self.__current_file_name = f'{join(self.__SCREENSHOT_FOLDER, selected_folder)}\\desktop-{self.__img_count}.jpg'
                # open image by filename and store its content in variable -> __table_img_loaded
                self.__load_image_to_memory()
                # crop table from __table_img_loaded and update with cropped image to serve as base table
                self.__table_img_loaded = self.crop_at_pos(self.__table_img_loaded, position.table_pos)

                # TODO: image extractor controller here
                user_input = input("gimmme some input biatch\n")
                if user_input == "":
                    self.__img_count += 1
                elif user_input == ".":
                    Utils.save_image(self.__table_img_loaded, self.__GATHERING_FOLDER + "\\current_table.jpg")
                    print("table img saved")
                    continue
                if int(user_input) >= 0:
                    self.__img_count = int(user_input)

            except KeyboardInterrupt:
                break

