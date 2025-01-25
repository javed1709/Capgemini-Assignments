def grade(marks1,marks2,marks3,marks4,marks5):
    total_marks=marks1+marks2+marks3+marks4+marks5
    percentage=total_marks
    grade='F'
    if percentage>=25 and percentage<=55:
        grade='C'
    elif percentage>=65 and percentage<90:
        grade='B'
    elif percentage>=90:
        grade='A'
    return [total_marks,percentage,grade]

name=input("Enter the student name:")
m1,m2,m3,m4,m5=int(input("Enter subj1 marks <=20:")),int(input("Enter subj2 marks <=20:")),int(input("Enter subj3 marks <=20:")),int(input("Enter subj4 marks <=20:")),int(input("Enter subj5 marks <=20:"))
lst=grade(m1,m2,m3,m4,m5)
print(f"{name} Secured Total marks:{lst[0]}, Percentage:{lst[1]}, Grade:{lst[2]}")