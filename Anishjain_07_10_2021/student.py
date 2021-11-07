from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, roll_no):
        Person.__init__(self, first_name, last_name)
        self.roll_no = roll_no