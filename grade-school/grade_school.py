from bisect import insort
from itertools import chain

class School:
    def __init__(self):
        self.grades = []      # 'Grade n' corresponds to self.grades[n]]

    def add_student(self, name, grade):
        while len(self.grades) <= grade:
            self.grades.append([])
        insort(self.grades[grade], name)

    def roster(self):
        return list(chain(*self.grades))

    def grade(self, grade_number):
        if grade_number >= len(self.grades):
            return []
        else:
            return self.grades[grade_number]
