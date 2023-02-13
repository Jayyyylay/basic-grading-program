student_scores = {
  "harry": 81,
  "ron": 78,
  "hermione": 99,
  "draco": 74,
  "neville": 62,
}
student_grades = ["harry","ron","hermione","draco","neville"]

def grading(student):
        score = student_scores[student]
        if score >= 91 and score <= 100:
            remarks = "Outstanding"
            print(f'\nStudent "{student}" has a grade of {score} and it is equivalent to {remarks}\n')
        elif score >= 81 and score <= 90:
            remarks = "Exceeds Expectations"
            print(f'\nStudent "{student}" has a grade of {score} and it is equivalent to {remarks}\n')
        elif score >= 71 and score <= 80:
            remarks = "Acceptable"
            print(f'\nStudent "{student}" has a grade of {score} and it is equivalent to {remarks}\n')
        elif score <= 70:
            remarks = "Fail"
            print(f'\nStudent "{student}" has a grade of {score} and it is equivalent to {remarks}\n')

def again():
    again1 = input("Do you want to try another student? Yes or No: ").lower()
    if again1 != 'yes' and again1 != "no":
        print("Yes or No only!")
    elif again1 == "yes":
        return True
    else:
        return False

a = True
while a:
    student = input(f"Which student do you want to know the score {student_grades}: ").lower()
    if student not in student_grades:
        print("Try again!")
    else:
        grading(student)
    a = again()
