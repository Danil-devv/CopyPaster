import time
from PIL import Image
import pytesseract as pytesseract
from pynput.keyboard import Key, Controller

spec_chars = {"†": "tab",
              "˜": "nl"}

input_file = input()
custom_config = r'-l rus+eng --psm 6'
txt = pytesseract.image_to_string(Image.open(f'{input_file}'),
                                  config=custom_config)

txt = txt.replace("\t", "†")
txt = txt.replace("\n", "˜")

time.sleep(3)  # время на смещение фокуса
keyb = Controller()
for i in txt:
    time.sleep(0.1)
    if i in spec_chars.keys():
        match i:
            case "†":
                for _ in range(4):
                    keyb.press(" ")
                    keyb.release(" ")
            case "˜":
                keyb.press(Key.enter)
                keyb.release(Key.enter)
    else:
        try:
            keyb.press(i)
            keyb.release(i)
        except:
            print(i)
