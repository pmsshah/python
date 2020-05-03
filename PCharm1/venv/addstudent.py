students = []

def add_student(name) :
    students.append(name)
    #add_student_infile(name)

def get_student_names() :
    students_name = []
    for student in students :
        students_name.append(student.title())
    return students_name

def print_student_names() :
    students_name = get_student_names()
    print(students_name)

def add_student_infile() :
    try:
        f = open("students.txt", "r+")
        for student in students:
            f.write(student+"\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_students_fromfile():
    try:
        f = open("students.txt", "r")
        for student in f:
            add_student(student.rstrip("\n"))
        f.close()
    except Exception:
        print("Could not read file")

read_students_fromfile()
print_student_names()
add_student("Mark4")
add_student("Mark5")
add_student("Mark6")
add_student_infile()


