import os.path
import time
import typing
from platform import system as platform
from os import system
from typing import Any

import pyperclip

from constants import AVRORA_NAME, ModeConstants, PASTING_MODES, STD_SOURCE, \
    SUPPORTED_TYPES


def _win32_enum_callback(hwnd, wildcard):
    import win32gui
    if str(win32gui.GetWindowText(hwnd)) == wildcard:
        win32gui.SetForegroundWindow(hwnd)


def focus_change():
    if platform() == 'Darwin':
        exit_code = system(
            f'''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "{AVRORA_NAME}" to true' '''
        )
        if exit_code != 0:
            print(
                "Error occured while switching to Avrora."
                " Do you have it opened?")
            exit(0)

    elif platform() in ("win32", "cygwin"):
        import win32gui
        win32gui.EnumWindows(_win32_enum_callback,
                             AVRORA_NAME)

    else:
        print("You have < 3 seconds to alt+tab into avrora! Hurry!")
        time.sleep(3)  # TODO: make linux and win switch
