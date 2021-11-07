class School:
    def __init__(self):
        self.standards = dict()

    def add_standard(self, standard):
        self.standards[standard.grade] = standard

    def get_standard(self, grade):
        return self.standards[grade]