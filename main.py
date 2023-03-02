import time
from PIL import Image
import pytesseract
from pynput.keyboard import Controller
from os import system
from platform import system as platform


def focus_change():
    if platform() == 'Darwin':
        system(
            '''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "ARM_Student" to true' '''
        )


def main():
    input_file = input()
    custom_config = r'-l rus+eng --psm 6'
    txt = pytesseract.image_to_string(Image.open(f'{input_file}'),
                                      config=custom_config)

    txt = txt.split("\n")
    focus_change()
    keyb = Controller()

    # Парсинг для метода решения
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
            except (Controller.InvalidKeyException, ValueError):
                print(letter)
        keyb.type("\n")


if __name__ == "__main__":
    main()
