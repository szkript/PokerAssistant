from os.path import join, isdir
from keras.preprocessing import image
import os
import cv2
import numpy as np


class Utils:
    # give back number of files with specific extension in given folder
    @staticmethod
    def number_of_files(folder_path, extension):
        files_in_folder = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.' + extension):
                    files_in_folder.append(file)
            break
        return len(files_in_folder)

    # return directories in given directory
    @staticmethod
    def get_directories(path):
        return [x[0] for x in os.walk(path)]

    @staticmethod
    def show_image(img):
        cv2.imshow("cropped", img)
        cv2.waitKey(0)

    @staticmethod
    def save_image(img, filename):
        cv2.imwrite(filename, img)

    @staticmethod
    def validate_path(path):
        if not isdir(path):
            os.mkdir(path)

    # crop image at given params
    @staticmethod
    def crop_at_pos(img, coordinates):
        return img[coordinates["y"]:coordinates["y"] + coordinates["h"],
               coordinates["x"]:coordinates["x"] + coordinates["w"]]

    @staticmethod
    def calculate_card_positions(pos, pos1):
        poscalc = []
        margin = 4

        tmp = pos.copy()
        for i in range(2):
            tmp = tmp.copy()
            if i > 0:
                tmp["x"] = tmp["x"] + tmp["w"]
            poscalc.append(tmp)

        tmp = pos1.copy()
        for x in range(5):
            tmp = tmp.copy()
            if x > 0:
                tmp["x"] += tmp["w"] + margin
            poscalc.append(tmp)
        return poscalc

    @staticmethod
    def preprocess_image(img_path):
        processing = image.load_img(img_path, target_size=(64, 64))
        processing = image.img_to_array(processing)
        processing = np.expand_dims(processing, axis=0)
        return processing
