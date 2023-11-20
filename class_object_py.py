#To create a class, use the keyword class:
# class MyClass():
#     x = 10
    
# p1 = MyClass()
# print(p1.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# class CallName():
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

# p = CallName("Kelvin", "Ward")
# print(p.firstname, p.lastname)



# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

# class Person():
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def __str__(self) -> str:
#         return f"{self.firstname}({self.firstname})"
    
# x = Person("Kelvin","Locke")
# print(x)



#Object Methods
# class CallName():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def my_func(self):
#         print("Name: " + self.name, "\nAge: " + str(self.age))
        
# x = CallName("Kelvin", 23)
# x.age = 59
# x.my_func()


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
