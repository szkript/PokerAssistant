from typing import Dict, List, Any
from utils import Utils
import pyautogui
import os
import cv2
from os.path import join
from game_components import positions as position
from recognizer import predict


class Table:
    # built up objects from prediction
    __hand = None
    __middle = None
    __dealer_position = None

    __extracted_objects: List[Any]
    __calculated_positions: List[Dict[Any, Any]]
    # folder paths
    __SCREENSHOT_FOLDER = "desktop_screenshots"
    __DESKTOP_IMAGE_FOLDERS_NUM = 0
    __GATHERING_FOLDER = "image_gathering"
    __BASE_PATH = None

    # image related
    __table_img_loaded = None

    # classifier model
    classifier = None

    # for image counting
    __img_count = 0
    __current_file_name = None

    def __init__(self, mode):
        self.classifier = predict.Predict()
        self.__calculated_positions = Utils.calculate_card_positions(position.my_cards_pos,
                                                                     position.middle_cards_pos) + position.dealer_chip

        # classifier init
        if mode == "live":
            # self.__set_folder_path()
            pass
        elif mode == "extract":
            Utils.validate_path(self.__GATHERING_FOLDER)
            self.__DESKTOP_IMAGE_FOLDERS_NUM = Utils.get_directories(self.__SCREENSHOT_FOLDER).__len__() - 1

    # TODO: get all object
    def get_all(self, test_mode=None):
        print(self.__img_count)
        if test_mode is None:
            self.__take_screenshot()
        else:
            self.__current_file_name = f'desktop_screenshots\\5\\desktop-{self.__img_count}.jpg'
            self.__img_count += 1

        # open image by filename and store its content in variable -> __table_img_loaded
        self.__load_image_to_memory()
        # crop table from __table_img_loaded and update with cropped image to serve as base table
        self.__table_img_loaded = Utils.crop_at_pos(self.__table_img_loaded, position.table_pos)
        self.__crop_table_objects()
        self.__recognize_objects()
        self.__display("all")
        table_objects = dict(hand=self.__hand, middle=self.__middle, dealer_position=self.__dealer_position)
        return table_objects

    # experimental
    def extractor(self):
        self.__read_images()

    # returns count of images
    def get_img_count(self):
        return self.__img_count

    # for testing
    def analyze(self):
        table = self.get_all()

    # take and save screenshot, sets file path in __current_file_name
    def __take_screenshot(self):
        screenshot = pyautogui.screenshot()
        self.__current_file_name = f'{self.__BASE_PATH}\\desktop-{self.__img_count}.jpg'
        screenshot.save(self.__current_file_name)
        self.__img_count += 1

    # sets and create new folder for every instance
    def __set_folder_path(self):
        actual_path = join(os.getcwd(), self.__SCREENSHOT_FOLDER)
        Utils.validate_path(actual_path)
        directories = Utils.get_directories(actual_path)
        try:
            next_folder = str(int(directories[-1][-1]) + 1)
        except ValueError:
            next_folder = str(0)

        directory = actual_path + "\\" + next_folder
        print(f"The current working directory is {directory} \n")
        Utils.validate_path(directory)

        self.__BASE_PATH = directory

    def __load_image_to_memory(self):
        self.__table_img_loaded = cv2.imread(self.__current_file_name)

    # predict prepared images and set objects in their place
    def __recognize_objects(self):
        # example -> self.classifier.predict(self.__extracted_objects[4])
        cards_result = []
        cards = self.__extracted_objects[:7]
        for in_game_card in cards:
            cards_result.append(self.classifier.predict(in_game_card))

        dealer_chips = self.__extracted_objects[7:]
        chips_result = []
        dealer_position = -1
        for dealer_position, dealer_chip in enumerate(dealer_chips):
            res = self.classifier.predict(dealer_chip)
            chips_result.append(res)
            if res == "dealer_chip":
                break

        self.__hand = cards_result[:2]
        self.__middle = cards_result[2:]
        self.__dealer_position = dealer_position

    # reads existing images from given folder
    def __read_images(self):
        if self.__DESKTOP_IMAGE_FOLDERS_NUM < 0:
            print("no data to examine, gather some and come back later")
            return

        # selected_folder = input(f"choose folder from 0 to {self.__DESKTOP_IMAGE_FOLDERS_NUM - 1}:\n")
        selected_folder = str(0)
        while True:
            try:
                print(f'image num {self.__img_count}')
                # building file name
                self.__current_file_name = f'{join(self.__SCREENSHOT_FOLDER, selected_folder)}\\desktop-{str(self.__img_count)}.jpg'
                table = self.get_all()
                # TODO: image extractor controller here
                user_input = self.__menu()
                if user_input == "":
                    self.__img_count += 1
                    continue
                elif user_input == ".":
                    Utils.save_image(self.__table_img_loaded, self.__GATHERING_FOLDER + "\\current_table.jpg")
                    print("table img saved")
                    continue
                elif user_input == "exit":
                    print("program finished")
                    break
                elif int(user_input) >= 0:
                    self.__img_count = int(user_input)

            except KeyboardInterrupt:
                break
            except ValueError:
                break

    # crop desired objects from table img then reload them into an np array with shape of 1,3,64,64 for prediction
    def __crop_table_objects(self):
        self.__extracted_objects = []
        for n, game_obj in enumerate(self.__calculated_positions):
            cropped = Utils.crop_at_pos(self.__table_img_loaded, game_obj)
            fn = f"gateway/{n}.jpg"
            Utils.save_image(cropped, fn)
            reloaded_img = Utils.preprocess_image(fn)
            self.__extracted_objects.append(reloaded_img)

    # TODO: get hand if not none
    def get_hand(self):
        if self.__hand is None:
            # TODO: create new pic, predict and set hand cards
            self.__take_screenshot()
            pass
        return self.__hand

    # TODO: get middle if not none
    # TODO: get position if not none

    @staticmethod
    def __menu():
        menu_text = """
blank -> next
#num -> change folder
num -> img index
-cardnum -> save card from img card[i], ctrl+c / e -> exit \n
"""
        user_input = input(menu_text)
        return user_input

    def __display(self, param):
        if param is "all":
            print(f"""
hand: {self.__hand} dealer position: {self.__dealer_position}
middle: {self.__middle}
""")
        elif param is "hand":
            print(f"hand: {self.__hand}")
        elif param is "middle":
            print(f"middle: {self.__middle}")
        elif param is "position":
            print(f"position: {self.__dealer_position}")
