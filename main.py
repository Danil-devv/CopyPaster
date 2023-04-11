from paste import code_paste
import keyboard
from parser import args_processor


def main():
    while True:
        # для вставки кода
        if keyboard.read_key() == "f4":
            txt = args_processor.get_text()
            txt = txt.strip().replace("\r", "")
            code_paste(txt)
        # для вставки в метод решения
        if keyboard.read_key() == "f5":
            txt = args_processor.get_text()
            txt = txt.strip().replace('\n', '')
            code_paste(txt)
        # для вставки в алгоритм
        if keyboard.read_key() == "f6":
            txt = args_processor.get_text()
            txt = txt.strip().replace('\n', '').replace('\r', ' ')
            code_paste(txt)


if __name__ == "__main__":
    main()
