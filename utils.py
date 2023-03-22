import time

from platform import system as platform
from os import system

from constants import AVRORA_LINUX, AVRORA_WIN


def _win32_enum_callback(hwnd, wildcard):
    import win32gui
    if wildcard in str(win32gui.GetWindowText(hwnd)):
        win32gui.SetForegroundWindow(hwnd)


def focus_change():
    if platform() == 'Darwin':
        exit_code = system(
            f'''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "{AVRORA_LINUX}" to true' '''
        )
        if exit_code != 0:
            print(
                "Error occurred while switching to Avrora."
                " Do you have it opened?")
            exit(0)

    elif platform() in ("Windows", "win32", "cygwin"):
        import win32gui
        win32gui.EnumWindows(_win32_enum_callback,
                             AVRORA_WIN)
    else:
        print("You have < 3 seconds to alt+tab into avrora! Hurry!")
        time.sleep(3)  # TODO: make linux switch
