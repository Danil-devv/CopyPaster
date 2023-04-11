import os
import typing

import pyperclip
from PIL import Image
from pytesseract import pytesseract

from constants import ModeConstants, STD_SOURCE, SUPPORTED_TYPES, \
    PASTING_MODES, SUPPORTED_CODE_TYPES, SUPPORTED_IMAGES_TYPES

from argparse import ArgumentParser


class CustomParser(ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mode = ModeConstants.SOLUTION_MODE
        self._source = STD_SOURCE

    def parse_args(self):
        ns = vars(super().parse_args())
        for arg, value in ns.items():
            setattr(self, "_" + arg, value)

    @property
    def source(self) -> typing.Tuple[str, str]:
        data: str = self._source
        if self._source == STD_SOURCE:
            data: str | None = pyperclip.paste()
            if data is None:
                print("Data not found. Do you have anything in your clipboard?")
            data.replace(" " * 4, "")
        if os.path.exists(data) and (
                os.path.splitext(data)[1] in SUPPORTED_TYPES):
            if os.path.splitext(data)[1] in SUPPORTED_CODE_TYPES:
                self._mode = ModeConstants.CODE_MODE  # change mode to 'code'
            return data, "path"
        # TODO: think about proper return type
        return data, "text"

    @property
    def mode(self) -> ModeConstants:
        if self._mode not in PASTING_MODES:
            print("Unknown pasting mode, solution mode chose by default")
            self._mode = ModeConstants.SOLUTION_MODE  # by default
        return self._mode

    def get_text(self) -> str:
        src, src_type = self.source
        if src_type == "text":
            txt = src
        elif os.path.splitext(src)[1] in SUPPORTED_IMAGES_TYPES:
            custom_config = r'-l rus+eng --psm 6'
            txt = pytesseract.image_to_string(Image.open(src),
                                              config=custom_config)
        elif os.path.splitext(src)[1] in SUPPORTED_CODE_TYPES:
            with open(src) as file:
                txt = file.read()
        return txt


args_processor = CustomParser()
args_processor.parse_args()
