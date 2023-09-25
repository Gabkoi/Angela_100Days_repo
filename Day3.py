# control flow

# Bath Top > greater than operator
"""
water_level = 30

if water_level > 80:
    print("Drain Water")

else:
    print("Containue")
"""


# coster rider  >= greater or equal to operator

"""
rider_hieght = int(input("what is your hieght "))

if rider_hieght >= 120:
    print("You can ride the rollercoaster ")
    
    age = int(input("What is tour age "))

    if age < 12:
        print("You are allwo to used the $5 Ticket")

    elif age <= 18:
        print(" you are allow to buy the $7 ticket")
      
    else:
      print("You are allow you are allow to the $12 ticket")
      
else:
    print("You are not allow to ride the rollercoaster ")
    """


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
    print(f"Your bmi is {BMI} and you are clinically Obese")
