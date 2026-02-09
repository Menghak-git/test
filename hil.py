print("Instructions for Grading System Module:")
print("Score Ranges and Corresponding Grades:")
print("0-49:F")
print("50-59:E")
print("60-69:D")
print("70-79:C")
print("08-89:B")
print("90-100:A")
score= int(input("Enter the score (0-100):"))
grade=''
if score>= 90 and score<=100:
    grand= 'A'
elif score >= 80 and score <=89:
    grade='B'
elif score >= 70 and score <= 79:
    grade='C'

elif score>=60 and score <=69:
    grand='D'
elif score>=50 and score <=59:
    grade='E'
elif score>=0 and score <=49:
    grade = 'f'
else:
    grade= 'Invalid score'
print (" garde assigned:",grade)