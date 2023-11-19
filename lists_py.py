#I. List
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

#1. Allow Duplicates
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

#2. List Length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

#3. List - DataTypes
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# list4 = ["abc", 34, True, 40, "male"]

#4. Using the list() constructor to make a List:
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

#II. Access List Items
#1. List items are indexed and you can access them by referring to the index number:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

#2. Negative indexing means start from the end
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

#3. Range of Indexs
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

#4. By leaving out the start value, the range will start at the first item:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

#5. By leaving out the end value, the range will go on to the end of the list:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

#6. Range of Negative Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

#7. Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "apple1" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# else:
#   print("No, 'apple' is not in the fruits list")

#III. Change List Items
#1. Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

#2. Change a Range of Item Values
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)


#IV. Add List Items
#1. Extend List
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#2. Add Any Iterable
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thisdict = {"kiwi": 8, "orange": 9}
# thisset = {"kiwi", "orange"}
# thislist.extend(thistuple)
# thislist.extend(thisdict)
# thislist.extend(thisset)
# print(thislist)

#V. Remove List Items
#1.Remove Specified Item
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

#2. Remove Specified Index
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop() # remove last items
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

#VI. Loop Lists
#1. Loop Through a List
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

#2. Loop Through the Index Numbers: Use the range() and len() functions to create a suitable iterable.
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


#3. Using a While Loop
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i += 1

#4. Looping Using List Comprehension
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

#VII. List Comprehension
#1. list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
        
# print(newlist)

#Or
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]
# newTest = [p for p in fruits if "p" in p]

# print(newTest)

# With no if statement:
# newlist = [x for x in fruits]
# print(newlist)

#2. use range to create a list
# newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

#3. Expressions
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x.upper() for x in fruits]
# print(newlist)

# newlist = ['hello' for x in fruits]
# print(newlist)

# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)


#VIII. Sort Lists
#1. Sort List Alphanumerically
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

#2. Sort Descending
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

#IX. Copy Lists
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

#OR

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


#X. Join Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

#OR

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

#OR 
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)



###----------------- LIST AND TUPLE AND SET IS THE SAME --------------------###