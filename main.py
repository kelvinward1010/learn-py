# comment

# first_name = 'kelvin'
# last_name = "ward"
# name = first_name + " " + last_name
# print("This is: ",name)
# print(type(name))


# int
# age = 21
# age = age +1
# age +=1
# print("Your age: " + str(age))
# print(type(age))


# height = 250.5
# print(height)
# print("Your height is: " + str(height) + "cm")
# print(type(height))


# human = True
# print("Are you a human: " + str(human))
# print(type(human))

# name = "Kelvin"
# age = 21
# attractive = True

#mutile ass

# name, age, attractive = "Kelvin", 21, True
# Power = Love = Something = 30
# print(Power)
# print(Love)
# print(Something)


# your_name = input("Please enter your name: ")
# print(your_name)

# num1 = input('enter: ')
# num2 = input('enter: ')
# print(int(num1) + int(num2))
# print(type(num1))
# print(type(num2))


food_amount = float(input('Enter food amount $: '))
tip_percenttage = int(input('Enter your tip percentage %: ')) / 100
tip_amount = food_amount * tip_percenttage

#total

total = food_amount + tip_amount
print('\n\n')
print('----------------------------------')
print("$" + str(total))
print("\n")
print(f'tip amount: ${tip_amount}')
print('----------------------------------')
