## Installation ##

Just clone repo

`git clone https://github.com/lokot0k/AvroraForcePaster.git`

Also you may need to install reqs:

`pip install -r requirements.txt` 

And if you're using windows, you also may need to install one more manually:

`pip install pywin32`

Now you're all set!

---
If you're using Linux, you should install wmctrl package. 

## Usage ##

`python main.py --help` for guide 

## Improvements ##

- [X] script for pasting
- [X] image-to-text with tesseract
- [ ] Proper pasting with enter+shift instead nl (unnecessary)
- [ ] Deal with markers from pictures (unnecessary)
- [X] UI for pasting (PyQt6 prolly/Terminal util)
- [X] hot-key for pasting or auto-changing focus on avrora on macOS
- [X] do previous task on windows
- [X] do previous task on linux
- [X] build executable for Windows
- [X] write explaining docs

## Как пользоваться???
Начнем с того, что данный тип программы - CLI(пока что), то есть запускать программу надо из консоли/терминала и передавать ей параметры/данные через него же.
У программы есть два режима - вставка метода решения, и вставка кода. По дефолту программа считает, что вставляется метод решения.

Подробнее о режимах:
- Режим метода решения - немного форматирует текст, делая его более-менее подходящим для генерации отчета. Не удивляйтесь, что выглядит кринжово, в отчете все так выглядит. Однако учтите, таблицы придется рисовать самому!
- Режим вставки кода - вставляет текст как он есть, сохраняя пробелы/табуляцию. Иногда конфличит с авто-форматером самой авроры. Думаю над фиксом, однако пока что придется вручную подправлять. (благо в авроре можно выделить текст и нажать таб - сместит все что выделенно ровно на таб)


Как запускать:
- `python main.py --mode [MODE] --source [SOURCE]` - из папки с проектом, если вы склонили/скачали репо.
- `main.exe --mode [MODE] --source [SOURCE]` - из папки с скачанным екзешником, если у вас винда.

Что это за моды, сурсы? Моды - режимы, описаны ранее, для вставки кода пишите `--mode code`, для вставки метода решения `--mode sol` (или ничего, так как это дефолтный режим).
С сурсами все немного сложнее: это путь к данным, или текст, который вы хотите вставить. По дефолту(то есть если не указывать параметр) он берет последний скопированный текст из буфера обмена и пастит в аврору. Однако вы можете указать этот текст в аргументах типа `--source #include<iostream>` вставит строку инклуда итд. Также можно передавать пути к файлам, например, если скопировать путь до файла (например C:\Users\asd\Desktop\main.cpp), то он вставит весь код из него. Аналогично, можно указать путь в аргументах явно, а не копировать его в буфер, например: `--source C:\Users\asd\Desktop\main.cpp`. Также можно указывать пути к картинкам, программаа вставит текст с них (учтите, маркеры и прочие спецсимволы могут быть не совсем корректны!)

### Совсем вкратце: 
Копируйте текст/код, если вставляете метод решения пишите `python main.py`(или  `main.exe`), если вставляете код пишите `python main.py --mode code` (или `main.exe --mode code`) 

---
Если вам хоть как-то помогло, поставьте звездочку! Также смело описывайте возникающие проблемы и предложения в ишуе, или кидайте пулл реквесты. Успехов!
