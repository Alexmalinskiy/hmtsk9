# folder Migrations lays in the same dir as python file
import os
import os.path


def menu():
    files = source_search()
    while True:
        print("Уточните содержимое файла. (q - для выхода из поиска)")
        inp = input()
        if inp.lower() == "q":
            break
        files = search_util(inp, files)
        line_print(files)
        print("Всего: {0}".format(len(files)))


def search_util(line, files):
    new_files = []
    for file in files:
        with open(file, "r", encoding="utf8") as f:
            if line.lower() in f.read().lower():
                new_files.append(file)
    return new_files


def source_search():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"Migrations")
    print(path)
    files = [os.path.join(path,file) for file in os.listdir(path) if os.path.splitext(file.lower())[1] == ".sql"]
    return files


def line_print(files):
    for file in files:
        print(file)


if __name__ == '__main__':
    menu()