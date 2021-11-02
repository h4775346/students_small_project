class Student:
    availableId = 1  # Id for new students

    def __init__(self, name, age):
        self.id = self.availableId  # Give id to student
        self.name = name
        self.age = age
        Student.availableId += 1  # Increment Id for each new student


class StudentsController:
    def __init__(self):
        self.students = []

    def get_students(self):
        return self.students

    def get_students_as_string(self):
        new_students = ""
        for student in self.students:
            new_students += f'{student.id} => {student.name} : {student.age}\n\n'
        return new_students

    def get_student_by_id(self, s_id):
        for student in self.students:
            if student.id == int(s_id):
                return student
        return False  # Will return false if there was no student match the given id

    def print_student(self, s_id):
        student = self.get_student_by_id(s_id)
        if not student:
            print("Student Not Found")
            return False
        print(f'{student.id} => {student.name} : {student.age}\n\n')
        return True

    def search_for_student(self, keyword):
        for student in self.students:
            if keyword.lower() in student.name.lower():
                self.print_student(student.id)  # Will return array containing the found students

    def add_student(self, name, age):
        self.students.append(Student(name, age))
        return self

    def remove_student(self, s_id):
        student = self.get_student_by_id(s_id)
        if student:
            self.students.remove(student)

    def edit_student(self, s_id, new_student):
        old_student = self.get_student_by_id(s_id)
        if old_student:
            old_student_index = self.students.index(old_student)
            self.students[old_student_index] = new_student  # replace old student with the new one
            return True
        return False


# _____________________________________ Code Starts From Here ________________________________________________________


def print_menu():
    print('----------------------------------------')
    for menu_key in menu:
        print(f'{menu.get(menu_key).get("print")} ({menu_key})')
    print('----------------------------------------')


def do_action(action_id):
    if action_id not in menu:
        print("Invalid Option !")
        return
    menu.get(action_id).get('action')()


students = StudentsController()
# lets add some students to start with
students.add_student("Alex", 12) \
    .add_student("Sam", 13) \
    .add_student("mark", 15)

menu = {
    '1': {
        'print': 'Print all students',
        'action': lambda: print(students.get_students_as_string())
    },
    '2': {
        'print': 'Get student by id',
        'action': lambda: students.print_student(input('Enter Student Id : '))
    },
    '3': {
        'print': 'Search For Student by Name',
        'action': lambda: students.search_for_student(input('Enter Name : '))
    },
    '4': {
        'print': 'Add New Student',
        'action': lambda: students.add_student(input('Enter Name : '), input('Enter Age : '))
    },
    '5': {
        'print': 'Edit Student',
        'action': lambda: students.edit_student(input("Enter Student Id: "),
                                                Student(input("Enter New Name: "), input("Enter New Age: ")))
    },
    '6': {
        'print': 'Delete Student',
        'action': lambda: students.remove_student(input('Enter Student Id : '))
    },

}
print(students.get_students_as_string())

while 1:
    print_menu()
    action = input("Enter You Action Number: ")
    do_action(action)
