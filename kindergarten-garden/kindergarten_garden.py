DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry']

PLANTS = { 'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

class Garden:
    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.students = sorted(students)
        self.rows = diagram.split()

    def plants(self, student):
        try:
            pos = self.students.index(student) * 2
        except:
            raise Exception(student + " is not in the list of students")
        
        student_plants = []
        for row in self.rows:
            student_plants.extend([PLANTS[pl] for pl in row[pos:pos+2]])
        return student_plants
