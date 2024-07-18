class Allergies:

    def __init__(self, score):
        self.lst,candidates= [],{"cats":128,"pollen":64,"chocolate":32,"tomatoes":16,"strawberries":8,"shellfish":4,"peanuts":2,"eggs":1}
        for i in range(len(candidates)):
            if score%256 >= list(candidates.values())[i]:
                score -= list(candidates.values())[i]
                self.lst.append(list(candidates.keys())[i])

    def allergic_to(self, item):  return item in self.lst