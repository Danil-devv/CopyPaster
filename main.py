from PIL import Image
import pytesseract

from paste import sol_method_paste, code_paste
from constants import ModeConstants

from parser import args_processor


def main():
    src, src_type = args_processor.source
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

    match args_processor.mode:
        case ModeConstants.SOLUTION_MODE:
            sol_method_paste(txt)
        case ModeConstants.CODE_MODE:
            code_paste(txt)


if __name__ == "__main__":
    main()
