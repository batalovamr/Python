def get_op():
    op = int(input("1 - добавить ученика, \n2 - добавить предмет, \n3 - добавить оценку, \n4 - показать весь список, \n5 - показать конкретного ученика, \n6 - выход\n"))
    return op

def input_student():
    name = input("Введите имя и фамилию: ")
    return name

def input_lesson():
    less = input("Введите название предмета: ")
    return less

def get_mark():
    name = input("Введите имя и фамилию: ")
    less = input("Введите название предмета: ")
    mark = input("Введите оценку: ")
    return name, less, mark

def input_student_table():
    name = input("Введите имя и фамилию ученика для просмотра оценок: ")
    return name