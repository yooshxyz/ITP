class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.birthplace = ""
        self.age = 0
    def __repr__(self):
        return f"{self.first_name} {self.last_name} age: {self.age}"