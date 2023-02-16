import time
from sys import stdin
from pynput.keyboard import Key, Controller
spec_chars={"†":"tab",
            "˜":"nl"}

x = stdin.readlines()
for i in range(len(x)):
    x[i] = x[i].replace("\t", "†")
    x[i] = x[i].replace("\n", "˜")

time.sleep(3)
keyb = Controller()
for i in x:
    for j in i:
        time.sleep(0.1)
        if j in spec_chars.keys():
            match j:
                case "†":
                    for i in range(4):
                        keyb.press(" ")
                        keyb.release(" ")
                case "˜":
                    keyb.press(Key.enter)
                    keyb.release(Key.enter)
        else:
            try:
                keyb.press(j)
                keyb.release(j)
            except:
                print(j)
