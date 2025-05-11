student_marks={
    'Alfai':45,
    'Kaif':70,
    'Rohan':80,
    'David':90
}

student_name=input('Enter the name:')

if student_name in student_marks:
    print(student_name,"'s marks:",student_marks.get(student_name))

else:
    print("student not found")    