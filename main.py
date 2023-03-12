from PIL import Image
import pytesseract

from paste import sol_method_paste, code_paste
from utils import get_mode, ModeConstants


def main():
    input_file = input("Input path to file you want to paste:\n")
    custom_config = r'-l rus+eng --psm 6'
    try:
        txt = pytesseract.image_to_string(Image.open(f'{input_file}'),
                                          config=custom_config)
    except FileNotFoundError:
        print("Allegedly the file path is wrong")
        exit(0)
    mode = get_mode()
    match mode:
        case ModeConstants.SOLUTION_MODE:
            sol_method_paste(txt)
        case ModeConstants.CODE_MODE:
            code_paste(txt)


if __name__ == "__main__":
    main()
