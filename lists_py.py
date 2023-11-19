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