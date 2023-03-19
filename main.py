from paste import sol_method_paste, code_paste
from constants import ModeConstants

from parser import args_processor


def main():
    txt = args_processor.get_text()
    match args_processor.mode:
        case ModeConstants.SOLUTION_MODE:
            sol_method_paste(txt)
        case ModeConstants.CODE_MODE:
            code_paste(txt)


if __name__ == "__main__":
    main()
