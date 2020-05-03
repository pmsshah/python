def read_file1():
    # Open the file with read only permit
    f = open("venv/students.txt")
    line_count = 0
    while True:
        line = f.readline()
        if not line:
            break
        line_count += 1
        print("My line: " + str(line_count) + " " + line)
    f.close()

def read_file2():
    f = open("venv/students.txt")
    line_count = 0
    for line in f:
        line_count += 1
        print("My line: " + str(line_count) + " " + line)
    f.close()

def read_file3():
    f = open("venv/students.txt")
    lines = f.readlines()
    print(lines)
    f.close()

read_file1()