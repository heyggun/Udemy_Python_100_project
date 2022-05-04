student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
#TODO-1: Create an empty dictionary called student_grades.

student_grades = dict()

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:

  score = student_scores[student]

# if score > 90:  
  if 91<=score<=100:
    grade = 'Outstanding'
    
# if score > 80: 
  elif 81<=score<=90:
    grade = 'Exceeds Expectations'
  
  elif 71<=score<=80:
    grade = 'Acceptable'

  else :
    grade = 'Fail'
    
  student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)





