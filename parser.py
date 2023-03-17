import os
import typing

import pyperclip

from constants import ModeConstants, STD_SOURCE, SUPPORTED_TYPES, PASTING_MODES

from argparse import ArgumentParser


class CustomParser(ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mode = ModeConstants.SOLUTION_MODE
        self._source = STD_SOURCE

    def parse_args(self):
        ns = vars(super().parse_args())
        print(ns)
        for arg, value in ns.items():
            setattr(self, "_" + arg, value)

    @property
    def source(self) -> typing.Tuple[str, str]:
        data: str = self._source
        if self._source == STD_SOURCE:
            data: str = pyperclip.paste()
            data.replace("\t", "")
        if os.path.exists(data) and (
                os.path.splitext(data)[1] in SUPPORTED_TYPES):
            return data, "path"
        # TODO: think about proper return type
        return data, "text"

    @property
    def mode(self) -> ModeConstants:
        if self._mode not in PASTING_MODES:
            print("Unknown pasting mode, solution mode chose by default")
            self._mode = ModeConstants.SOLUTION_MODE  # by default
        return self._mode


args_processor = CustomParser()
args_processor.add_argument('--mode', '-m',
                            default=ModeConstants.SOLUTION_MODE,
                            help=f"Pick mode of pasting:\n"
                                 f"if you want to paste solution method,"
                                 f" write '{ModeConstants.SOLUTION_MODE}';\n"
                                 f"if you want to paste code,"
                                 f" write '{ModeConstants.CODE_MODE}'")

args_processor.add_argument('--source', '-s',
                            default=STD_SOURCE,
                            help="By default is 'buffer', which is a keyword for "
                                 "taking image path or plain text from clipboard\n"
                                 "If you don't want such behaviour, you can instead"
                                 " provide path or text in this arg manually")
args_processor.parse_args()
