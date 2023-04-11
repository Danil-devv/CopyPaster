import time

from pynput.keyboard import Controller


def code_paste(text):
    keyb = Controller()
    for letter in text:
        time.sleep(0.1)
        try:
            keyb.type(letter)
        except Controller.InvalidCharacterException:
            print(f"Can't type letter {letter}")
