class Standard:
    def __init__(self, grade, students):
        self.grade = grade
        self.students = students
        self.attendance = dict()

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, idx):
        return self.students.pop(idx)