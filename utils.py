import sys
import time
from platform import system as platform
from os import system


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
        mode = "sol"  # by default
    return mode
