from PIL import Image
import pytesseract

from paste import sol_method_paste, code_paste
from utils import get_mode, get_src
from constants import ModeConstants

from parser import parse_args


def main():
    args = parse_args()
    src, src_type = get_src(args)
    if src_type == "text":
        txt = src
    else:
        custom_config = r'-l rus+eng --psm 6'
        try:
            txt = pytesseract.image_to_string(Image.open(f'{src}'),
                                              config=custom_config)
        except FileNotFoundError:
            print("Allegedly the file path is wrong")
            exit(0)
    mode = get_mode(args)
    match mode:
        case ModeConstants.SOLUTION_MODE:
            sol_method_paste(txt)
        case ModeConstants.CODE_MODE:
            code_paste(txt)


if __name__ == "__main__":
    main()
