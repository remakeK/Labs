file_path="C:/Users/remak/OneDrive/Документы/Учеба/ВвИТ/Лабораторные/files/example.txt"
with open(file_path, "w") as file:
    file.write("I\nlike\npizza!")
    print()
def open_file(choice):
    try:
        if choice==1:
            with open(file_path, "r") as file:
                content=file.read()
                print(content)
        else:
            with open(file_path, "r") as file:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print("Файла не существует!")
choice=int(input("1-Чтение целиком\n2-Построчное чтение\n"))
while choice not in (1,2):
    choice=int(input("1-Чтение целиком\n2-Построчное чтение\n"))
open_file(choice)
