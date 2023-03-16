from enum import Enum


class ModeConstants(str, Enum):
    SOLUTION_MODE = "sol"
    CODE_MODE = "code"


AVRORA_NAME = "ARM_Student"
PASTING_MODES = [ModeConstants.SOLUTION_MODE, ModeConstants.CODE_MODE]
STD_SOURCE = "buffer"
SUPPORTED_TYPES = [".jpeg", ".png", ".jpg"]
