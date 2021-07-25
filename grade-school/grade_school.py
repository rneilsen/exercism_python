class School:
    def __init__(self):
        self.grades = {}        # key = grade (int), val = students (set of strings)

    def add_student(self, name, grade):
        if grade not in self.grades:
            self.grades[grade] = {name}
        else:
            self.grades[grade].add(name)

    def roster(self):
        roster = []
        for grade in sorted(self.grades.keys()):
            roster += self.grade(grade)
        return roster

    def grade(self, grade_number):
        return sorted(self.grades.get(grade_number, []))
