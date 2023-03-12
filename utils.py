import sys
import time
from enum import Enum
from platform import system as platform
from os import system


class ModeConstants(str, Enum):
    SOLUTION_MODE = "sol"
    CODE_MODE = "code"


AVRORA_NAME = "ARM_Student"
PASTING_MODES = [ModeConstants.SOLUTION_MODE, ModeConstants.CODE_MODE]


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


def get_mode():
    mode = ModeConstants.SOLUTION_MODE  # by default
    if len(sys.argv) > 2:
        mode = sys.argv[2]
    if mode not in PASTING_MODES:
        print("Unknown pasting mode, solution mode chose by default")
        mode = ModeConstants.SOLUTION_MODE
    return mode
