from PIL import Image
import pytesseract

from paste import sol_method_paste, code_paste
from utils import get_mode


def main():
    input_file = input()
    custom_config = r'-l rus+eng --psm 6'
    try:
        txt = pytesseract.image_to_string(Image.open(f'{input_file}'),
                                          config=custom_config)
    except FileNotFoundError:
        print("Allegedly the file path is wrong")
        exit(0)
    mode = get_mode()
    match mode:
        case "sol":
            sol_method_paste(txt)
        case "code":
            code_paste(txt)


if __name__ == "__main__":
    main()
