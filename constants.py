from enum import Enum


class ModeConstants(str, Enum):
    SOLUTION_MODE = "sol"
    CODE_MODE = "code"


AVRORA_MACOS = "ARM_Student"
AVRORA = "ACO Avrora"
PASTING_MODES = [ModeConstants.SOLUTION_MODE, ModeConstants.CODE_MODE]
STD_SOURCE = "buffer"
SUPPORTED_IMAGES_TYPES = [".jpeg", ".png", ".jpg"]
SUPPORTED_CODE_TYPES = [".c", ".h", ".cpp"]
SUPPORTED_TYPES = SUPPORTED_CODE_TYPES + SUPPORTED_IMAGES_TYPES
