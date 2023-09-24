# Data Types

# String
'''
print("Hello"[4])

print("123" + "234")
'''

# Interger
'''
print(12+2)
print (32)
'''

# float
'''
print(34.56)
'''


#  name convertion
'''
work = "Gabriel"
print(type(work))

a = float(123)
print(type(a))
'''


# Exercise day2  
'''
num1 = int(input())
num2 = int (input())
print(num1 + num2)
'''

# Math Operator 
'''print(3*3+3/3-3)'''

# Body weight Exercise
'''
weight = int(input("Enter your body weight "))
height = float(input("Enter your body height "))
BMI = weight / height **2 
print(int(BMI))
'''


# rounding number in python with the round Function
'''
print(round(3/5))

result = 4/2
result /= 2
print(round(result))

score = 0
score += 1
print(round(score))
'''

# Python F-String
'''
score = 0
hieght = 1.4
print(f"This is your score {score} \n This your player hieght is {hieght}")
'''


# F-string Exercise of Day2 

'''
age = int(input("What is your current Age "))

years = 90 - age
days = years * 365
weeks = years * 52
months = years * 12

message = f"you have {days} days, you have {weeks} weeks, you have {months} month left"
print(message)
'''


# Final project (Tip Caclulator)

print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill $ "))
tip_percentage = float(input("What percentage would like to give "))
user_name = int(input("How many user should split the money "))
total_bill = tip_percentage / 100
total_Amount = tip_percentage * total_bill + total_bill
bill_per_person = total_Amount  / user_name
final_amount = round(bill_per_person)
print(f"Each person should payed {final_amount}")




