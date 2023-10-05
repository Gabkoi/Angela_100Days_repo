"""
in Day 4 we will be talking about Randomisation in python
"""

# So the randint function is used to provide random integer or hold number
"""'
print("Randit Number random number")
random_integer = float(random.randint(1, 5))
print(random_integer)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

good_random = random.randint(20, 1000000)
print(good_random)
"""


# print("\n")

"""'
# This program crate a number random decimal number between 0 and 5
print("Rondom Floating Point Number")
random_float = random.random()*5
print(random_float)

n = random.random()
print(f"this is N value {n}")
"""

# random number excercise

"""
n = random.randint(0, 1)

if  n == 1 :
    print("Head")


else:
    print("Tails")
"""


# List in python

# fruit = ['Cherry', 'Banna']
"""

state_of_America = ["Delaware", "Pannsyvania", "New Jersy", "Georgia", "Connecticut"]

# print(state_of_America)



# This code is used to correct information in the  list of rewrite information  in the  List
state_of_America[2] = "New York"
state_of_America[1] ="Paynesvenia"
print(state_of_America)
"""


# Append Function this is a Funtion that is used to add only one exract information to the  List at the end
# the Extend  Function is used to add lot of information at the end of the  information

# ex
"""
state_of_America.append("PythonLand")
state_of_America.extend(["JavaLand", "Sql land",  "C++Land"]) 
print(state_of_America)
"""

"""'
# Name of List excercise
import random

name_string = input("Give me everybody's namesm seperated by a comma. ")

names = name_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
print(random_choice)

person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} you are going to payed for the mail to day")

# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} ypu will payed day")
"""

import random

"""
random_integer =random.randint(1, 10)
print(random_integer)
 
random_float = random.random()
print(random_float)
"""

# tryer
"""'
random_try = random.random()*5
print(random_try)


random_love = random.randint(1, 100)
print(f"your your love score is {random_love}")
"""

"""
# random toss program 
num = 0
if num == random.randint(0,1):
    print("head")

else:
    print("Tails")

# python Liat 
fruits = ["Cherry", "Apple", "pip"]
print(fruits)
"""
'''
state_of_Ameraica = ["Dalaware", "Paynnsyvania", "New Jercy", "Georgia", "Connecticut"]
print(state_of_Ameraica[-1])


# changing information in the list
# state_of_Ameraica[1]= "Pancilvania"
# print(state_of_Ameraica)

state_of_Ameraica.append(["Angeland"])
print(state_of_Ameraica)

state_of_Ameraica.extend(["Good Boy", "Food boy"])
print(state_of_Ameraica)
'''

# Exercise for List
'''
import random

name_string = input("Enter your name into the list seperated by the command ")

name = name_string.split(",")


name_items =len(name)

random_list = random.randint(1, name_items -1)
print(random_list)


person_will_pay = name[random_list]
print(person_will_pay)


print(f"{person_will_pay} you are going to pay for us today.")
'''


# nestest List in python
'''
dirty_all= ["Straw Barries", "Nectarines", "Apple", "Grapes", "Peaches", "Charries", "Pears", "Tomato"]
Fruits = ["Straw Barries", "Nectarines", "Apple", "Grapes", "Peaches", "Charries", "Pears", "Tomato"]


dirty_dozen =[dirty_all, Fruits]
print(f"{dirty_dozen}")


name = ["GAbriel Akoi", "John Brown", "Peter Paul"]
grade = ["12", "Peter", ""]

final = [name, grade]
print(final)
'''
'''
line1 = ["", "", ""]
line2 = ["","", ""]
line3 = ["", "", ""]
map = [line1, line3, line2]
print("")
position =  input()

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) -1
map[number_index][letter_index] = "x"
print(f"{line1} \n{line2}\n{line3}")
'''




# Rock paper game  
game_image = ["rock", "Paper", "scisssor"]
user_choice = int(input("what are you going to types 0 for Rock, 1 for, paper or 2 for Scissors.\n"))
if 0 <=user_choice < len(game_image):
    print(game_image[user_choice])

computer = random.randint(0,2) 
print("Computer choice 1")
print(game_image[computer])

if user_choice >=3 or computer < 0:
    print("wong number")

elif computer == 0  and user_choice == 2:
    print("You have won")

elif computer > user_choice: 
    print("You lose")

elif user_choice > computer:
    print("you won")

elif computer == user_choice:
    print("It   is a draw")



 



 











 