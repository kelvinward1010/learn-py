class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_name(self):
        print("name: ", self.name,"====" , "age: ", str(self.age))
        
# p = Person("Kelvin",23)
# p.print_name()

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.print_name()

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of", self.year)
        
x = Student("Mike", 12,1999)
x.welcome()