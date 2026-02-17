students = {
    "S001": ("Бат", 20, "Компьютерын ухаан"),
    "S002": ("Болд", 21, "Программ хангамж")
}



def add_student(student_id, name, age, major):
    students[student_id] = (name, age, major)

def find_student_by_id(student_id):
    student = students.get(student_id)
    if student:
        print(student)
    else:
        print("Oyutan oldsongui")

def list_students_by_major(major):
    result = [s for s in students.values() if s[2] == major]
    print(result)

def count_students():
    print(len(students))

add_student("S003", "Уянга", 22, "Компьютерын ухаан")
find_student_by_id("S002") # Гаралт: ("Болд", 21, "Программ хангамж")
list_students_by_major("Компьютерын ухаан") # Гаралт: [("Бат", 20, "Компьютерын ухаан), ("Уянга", 22, "Компьютерын ухаан")]
count_students() # Гаралт: 3