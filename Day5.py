# loop in python
"""
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    
    print(fruit + "pie")
    print(fruits)
    """


# for Loop  excersise
'''
Student_height = input().split()

for n in range(0, len(Student_height)):
    Student_height[n] = int(Student_height[n])

    total_height = 0
    for height in Student_height:
        total_height += int(height)
print(f"Total height = {total_height} ")


number_of_student = 0
for student in Student_height:
    number_of_student += 1
print(f"Number of student = {number_of_student} ")

average_height = round(total_height / number_of_student)
print(f"Average height = {average_height}")
'''


Student_score = input().split()

for n in range(0, len(Student_score)):
    Student_score[n] = int(Student_score[n])
    
    
hieghtest_score = 0
for score in Student_score:
    if score > hieghtest_score:
        hieghtest_score = score
print(f'The hieght score is {hieghtest_score}')




 





