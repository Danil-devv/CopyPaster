import argparse
from constants import ModeConstants, STD_SOURCE


def parse_args():
    parser = argparse.ArgumentParser(
        description='Utility for pasting things in Avrora')
    parser.add_argument('--mode', default=ModeConstants.SOLUTION_MODE,
                        help=f"Pick mode of pasting:\n"
                             f"if you want to paste solution method,"
                             f" write '{ModeConstants.SOLUTION_MODE}';\n"
                             f"if you want to paste code,"
                             f" write '{ModeConstants.CODE_MODE}'")

    parser.add_argument('--source', default=STD_SOURCE,
                        help="By default is 'buffer', which is a keyword for "
                             "taking image path or plain text from clipboard\n"
                             "If you don't want such behaviour, you can instead"
                             " provide path or text in this arg manually")
    return vars(parser.parse_args())
