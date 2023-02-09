def operation():
    op = int(input("1 - добавить пользователя \n2 - вывести таблицу \n3 - вывести только имя и фамилию \n4 - отсортировать по именам \n5 - отсортировать по id \n6 - выход \n"))
    return op

def add_worker():
    id = int(input("Введите свой id:"))
    name = input("Введите свое имя:")
    lastname = input("Введите свою фамилию:")
    number = int(input("Введите свой номер:"))
    comments = input("Введите примечание:")
    line = f"{id}, {name}, {lastname}, {number}, {comments}\n"
    with open("worker_list.txt", "a") as file:
        file.write(line)
    print("Сохранено")

def print_table():
    with open("worker_list.txt", "r") as file:
        for line in file.readlines():
            print(line, end = "")

def print_only_names():
    with open("worker_list.txt", "r") as file:
        for line in file.readlines():
            temp = line.split(",")
            print(f"Имя - {temp[1]}, Фамилия - {temp[2]}")