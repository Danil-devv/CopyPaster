import sys
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
    else:
        time.sleep(3)  # TODO: make linux and win switch


def get_mode():
    pasting_modes = ["sol", "code"]
    mode = "sol"  # by default
    if len(sys.argv) > 2:
        mode = sys.argv[2]
    if mode not in pasting_modes:
        return "sol"  # by default


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


def main():
    input_file = input()
    custom_config = r'-l rus+eng --psm 6'
    try:
        txt = pytesseract.image_to_string(Image.open(f'{input_file}'),
                                          config=custom_config)
    except FileNotFoundError:
        print("Allegedly the file path is wrong")
        exit(0)
    mode = get_mode()
    match mode:
        case "sol":
            sol_method_paste(txt)
        case "code":
            code_paste(txt)


if __name__ == "__main__":
    main()
