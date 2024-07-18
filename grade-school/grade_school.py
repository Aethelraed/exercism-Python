class School:
    def __init__(self): self.students,self.didadd = [],[]

    def add_student(self, name, grade):
        self.didadd += [not ((name,grade) in self.students or name in self.roster())]
        if self.didadd[-1]: self.students = self.students+[(name,grade)]        
        return self.didadd[-1]

    def roster(self):  return self.grade(1)+self.grade(2)+self.grade(3)+self.grade(4)+self.grade(5)+self.grade(6)+self.grade(7) #could not get it to work with list comprehension 

    def grade(self, grade_number): return sorted([name for name, grade in self.students if grade == grade_number])

    def added(self): return self.didadd 
