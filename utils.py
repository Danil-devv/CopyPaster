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


def get_mode(args: dict[str, Any]) -> ModeConstants:
    if args["mode"] not in PASTING_MODES:
        print("Unknown pasting mode, solution mode chose by default")
        args["mode"] = ModeConstants.SOLUTION_MODE  # by default
    return args["mode"]


def get_src(args: dict[str, Any]) -> typing.Tuple[str, str]:
    data: str = args["source"]
    if args["source"] == STD_SOURCE:
        data: str = pyperclip.paste()
        data.replace("\t", "")
    if os.path.exists(data) and (os.path.splitext(data)[1] in SUPPORTED_TYPES):
        return data, "path"
    # TODO: think about proper return type
    return data, "text"
