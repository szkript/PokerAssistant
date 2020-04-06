import pyautogui
from game_components.Enums.suggestion import Suggestion


class ResultHandler:

    def __init__(self, suggestion):
        if suggestion is Suggestion.FOLD:
            pyautogui.press("0")  # check || fold
        elif suggestion is Suggestion.PLAYABLE:
            pyautogui.press("2")  # raise || bet
        else:
            pyautogui.press("1")  # check || call
