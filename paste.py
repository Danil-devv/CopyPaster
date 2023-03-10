import time

from pynput.keyboard import Controller

from utils import focus_change


# пастинг метода решения
def sol_method_paste(text):
    txt = text.split("\n")
    focus_change()
    keyb = Controller()

    for line in txt:
        is_prefix = False
        if ":" not in line:
            is_prefix = True
        if is_prefix:
            for _ in range(4):
                keyb.press(" ")
                keyb.release(" ")
        for letter in line:
            time.sleep(0.1)
            try:
                keyb.press(letter)
                keyb.release(letter)
            except (Controller.InvalidKeyException, ValueError) as err:
                print(f"{err} occurred with letter {letter}")
        keyb.type("\n")


def code_paste(text):
    keyb = Controller()
    for letter in text:
        try:
            keyb.type(letter)
        except Controller.InvalidCharacterException:
            print(f"Can't type letter {letter}")
