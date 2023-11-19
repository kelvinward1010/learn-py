#I.Assign Mutiple Value


#1.And you can assign the same value to multiple variables in one line:
# x = y = z = 'Orarange'

# print(x)
# print(y)
# print(z)

#2.If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
# fruits = ['Orange', 'Banana', 'Fried Chicken']
# x,y,z = fruits

# print(x)
# print(y)
# print(z)


#II. Output Variables

#1.The Python print() function is often used to output variables.
# x = "Python is awesome"
# print(x)

#2. In the print() function, you output multiple variables, separated by a comma:
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y,"ok", z)

#3. You can also use the + operator to output multiple variables:
# x = "Python"
# y = "is"
# z = "awesome"
# print(x+y+z)

#4. For numbers, the + character works as a mathematical operator:
# x = 5
# y = 2
# print(x+y, x*y, x-y, float(x/y))


#III. Global Variables

#1. Create a variable outside of a function, and use it inside the function
# x = "Kelvin"

# def myFunc():
#     print(x)
    
# myFunc()


#2. Create a variable inside a function, with the same name as the global variable
x = "Kelvin"

def myFunc():
    x = "Ward"
    print(x)
    
myFunc()
print(x)