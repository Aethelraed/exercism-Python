class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)
    def plants(self,student):
        i = self.students.index(student)
        return [{"C":"Clover","G":"Grass","R":"Radishes","V":"Violets"}[plant] for plant in [*"".join([s[2*i:2*i+2] for s in self.diagram])]]




