import pyautogui
from game_components.Enums.suggestion import Suggestion


class ResultHandler:

    def __init__(self, suggestion):
        if suggestion is Suggestion.FOLD:
            pyautogui.press("0")
        else:
            pyautogui.press("2")
