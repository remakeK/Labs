file_path="C:/Users/remak/OneDrive/Документы/Учеба/ВвИТ/Лабораторные/files/user_input.txt"
with open(file_path,"w") as file:
    file.write(input("Напишите текст: "))
    
    
choice=input("Вы хотите что-то дописать? y/n\n")
while choice not in ["y","n","Y","N"]:
    choice=input("Вы хотите что-то дописать? y/n\n")
if choice=="y" or choice=="Y":
    with open(file_path,"a") as file:
        file.write(input("Напишите текст: "))
        
with open(file_path,"r") as file:
    content=file.read()
    print(content)
