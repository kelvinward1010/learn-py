#Creating a Function
# def Ok():
#     print("Creating a Function")
# Ok()


#Arguments
# def myFunc(name):
#     print("Your name:" + name)
# myFunc("Kelvin Ward")

# def my_name(name1, name2):
#     print(name1+" "+name2)
# my_name("Kelvin", "Ward")


#Arbitrary Arguments, *args
# def my_func(*i):
#     print("Showing my function: "+ i[2])
# my_func("A", "B", "KW")

#Keyword Arguments
# def my_func(x,y,z):
#     h = x + y + z
#     print("Showing my function: " + str(h))
# my_func(x=1,y=2,z=3)


#Arbitrary Keyword Arguments, **kwargs
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")



#Default Parameter Value
# def my_function(name = "Kelvin Ward"):
#     print("My name is: " + name)
    
# my_function("Neuvillet")
# my_function()
# my_function("Furina")



#Passing a List as an Argument
# def my_function(list):
#     x = 4
#     for i in list:
#         while x < i:
#             print(i)
#             break

# my_function([1,2,3,4,5,6,7])


# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)



#Return Values
# def my_function(x):
#     return x * 2


# print(my_function(1))
# print(my_function(2))



#The pass Statement
# def myfunction():
#   pass



#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\n\tRecursion Example Results")
tri_recursion(2)