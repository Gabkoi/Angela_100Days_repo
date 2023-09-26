# control flow

# Bath Top > greater than operator
"""
water_level = 30

if water_level > 80:
    print("Drain Water")

else:
    print("Containue")
"""


# rollercoaster  rider  >= greater or equal to operator
'''
hieght = int(input("what is your hieght in cm "))

if hieght >= 120:
    print("You can ride the rollercoaster")
    
    bill = 0
    age = int(input("What is your age "))
    if age < 12:
        bill = 5
        print("Child ticket are $5")

    elif age <= 18:
        bill = 7
        print("Youth ticket are $7")

    else:
        bill = 12
        print("Adult Ticket are $12")

    want_photos = input("Do you want a photos taken? Y or N  \n")

    if want_photos == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")

    elif want_photos == "N":
        print(f"You are still allow to payed {bill}")

else:
    print("Sorry, yo hsve to grow taller before you can ride rollercoster")
'''



# play groud != less than or equal to operator
"""
child_uder_age = input("what is your age to before entering the play ground ")

if child_uder_age != 18:
    print("you can enter to player ")

else:
    print("You are above age age to enter ")
"""

# first flow control Exercise

"""

number = int(input("Put in your number"))

if number % 2 ==0 :
    print("This is a even number")

else:
    print("This is a odd number")

"""


# BMI Calculator Exercise using the condional statement if / eslif else
'''
height = float(input("Enter your body height m "))
weight = float(input("What is your body weight "))
BMI = (weight / height + height)
print(BMI)


if BMI < 18.5:
    print(f"Your bmi is  {BMI} and you are UnderWeight")

elif BMI < 25:
    print(f"Your bmi is {BMI} and your are Normal")

elif BMI < 30:
    print(f"Your bmi is {BMI} and and your are OverWeight")

elif BMI < 35:
    print(f"your bmi is {BMI} and your are Obese")

else:
    print(f"Your bmi is {BMI} and you are clinically.")
'''


# Leap Year Excercise using the  if else
'''
year = int(input("Enter your year you want "))

if year % 4 == 0:
    print("Leap year")
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
else:
    print("Not a leap year")
'''   


# Program for my PIzza Cafe 

print("Welcome to the  pizza Diliveries ")

size = input("What size do you want? S, M, or L ")

add_pepperoni = input("Do you have pepperoni? Y or N ")

extra_cheese = input("Do you want a extra chase? Y or N")





# import urllib.request

# webUrl = urllib.request.urlopen("https://www.javatpoint.com/python-tutorial")
