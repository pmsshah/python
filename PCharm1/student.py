class Student:
    school_name = "Medfield school"
    max_student_id = 1
    def __init__(self, name, id = 0):
        self.name = name
        #if(max_student_id < id):
            #max_student_id = id
        self.id = id
    def print(self):
        print("My Student: " + str(self.id) + " : " + self.name + " @ " + self.school_name)

class HStudent(Student):
    school_name = Student.school_name + " High School"
    def __init__(self, name, id = 0):
        Student.__init__(self,name,id)

my_student = HStudent("Mark1",20)
my_student.print()
