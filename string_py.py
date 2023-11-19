#I. Python String
#1.Assign String to a Variable
# a = "Hello"
# print(a)

#2. Multiline Strings: You can use three double quotes Or three single quotes:
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

#3. Strings are Arrays
# a = "Hello, World!"
# print(a[1], a[0])

#4. Looping Through a String
# for x in "banana":
#   print(x)

#5. String Length
# a = "Hello, World!"
# print(len(a))

#6. Check String => result recieved: True or False
# txt = "The best things in life are free!"
# print("free" in txt) 

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("free" not in txt) 

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

#II. Slicing Strings
#1. Slicing
# x = "Ok, then what"
# print(x[2:5])

#2. Slice from the start
# x = "Ok, then what"
# print(x[:5])

#3. Slice from the end
# x = "Ok, then what"
# print(x[5:])

#4. Negative Indexing
# x = "Ok, then what"
# print(x[-5:-2])

#III. Modify String
#1. The upper() method returns the string in upper case:
# x = "Ok, then what"
# print(x.upper())

#2.The lower() method returns the string in lower case:
# x = "Ok, then what"
# print(x.lower())

#3. The strip() method removes any whitespace from the beginning or the end:
# x = "        Ok, then what "
# print(x.strip())

#IV. String Concatenation
#1. Merge variable a with variable b into variable c:
# a = "k"
# b = "w"
# c = a + b
# print(c)

#2. To add a space between them, add a " ":
# a = "k"
# b = "w"
# c = a + " " + b
# print(c)


#V. Format - Strings
#1. The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# age = 23
# txt = "My name is Kelvin and I am {} years old"
# print(txt.format(age))

#2. The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# a = 1
# b = 2
# c = 3
# txt = "a: {}, b: {}, c: {}"
# print(txt.format(a, b, c))

#VI. Escape Characters
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

