#I. Python Dictionaries
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(thisdict['brand'])

#II. Access Dictionary Items
#1. Access Items
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)

#OR
# x = thisdict.get("brand")
# print(x)

#2. Get Keys
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.get() #at least 1 argument
# print(x)


# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = car.keys()
# print(x) #before the change

# car["color"] = "white"
# print(x) #after the change

#3. Get Values
#x = thisdict.values()

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()
# print(x) #before the change

# car["year"] = 2020
# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()
# print(x) #before the change

# car["color"] = "red"
# print(x) #after the change

#4. Get Items
#x = thisdict.items()

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()
# print(x) #before the change

# car["year"] = 2020
# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()
# print(x) #before the change

# car["color"] = "red"
# print(x) #after the change

#5. Check if Key Exists
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

#III. Change Dictionary Items
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

#Update Dictionary
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)


#IV. Add Dictionary Items
#1. Adding Items
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

#2. Update Dictionary
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)

#V. Remove Dictionary Items
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

#OR
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

#OR
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

#OR
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

#VI. Loop Dictionaries
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for x in thisdict:
#   print(x)
  
# for x in thisdict:
#   print(thisdict[x])

# for x in thisdict.values():
#   print(x)

# for x in thisdict.keys():
#   print(x)
  
# for x, y in thisdict.items():
#   print(x, y)


#VII. Copy Dictionaries
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# mydict = dict(thisdict)
# print(mydict)

#VIII. Nested Dictionaries
#Example
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily, type(myfamily))

#OR
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily2, type(myfamily2))
print(myfamily2["child2"]["name"])