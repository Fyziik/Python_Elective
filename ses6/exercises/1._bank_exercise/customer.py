class Customer:

    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def change_information(self, name, age):
        self.name = name
        self.age = age

    

    def __str__(self):
        return self.name + " " + str(self.age)