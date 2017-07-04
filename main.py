# folder Migrations lays in the same dir as python file
def menu():
    import pprint
    files = source_search()
    while True:
        print("Уточните имя файла. (q - для выхода из поиска)")
        inp = input()
        if inp.lower() == "q":
            break
        files = search_util(inp, files)
        line_print(files)
        print("Всего: {0}".format(len(files)))


def search_util(str, files):
    import os
    files = [file for file in files if str.lower() in file.lower()]
    return files


def source_search():
    import os
    import os.path
    path = os.path.join(os.getcwd(),"Migrations")
    print(path)
    files = [file for file in os.listdir(path) if "sql" in file.lower()]
    return files


def line_print(files):
    for file in files:
        print(file)


if __name__ == '__main__':
    menu()