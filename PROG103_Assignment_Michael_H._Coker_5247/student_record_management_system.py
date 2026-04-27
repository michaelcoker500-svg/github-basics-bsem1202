#Constant
PASS_MARK = 60

#Calculating total score and average score
def student_system(score1, score2, score3, score4):
    total_score = score1 + score2 + score3 + score4
    average_score = total_score / 4
    return total_score, average_score

#using if statement to give the grades
def get_grade(average_score):
    if average_score >= 80 and average_score <= 100:
        return "A"
    elif average_score >= 70 and average_score <= 79:
        return "B"
    elif average_score >= 60 and average_score <= 69:
        return "C"
    elif average_score >= 50 and average_score <= 59:
        return "Redo the subject"
    else:
        return "F"



#loop
while True:
    print("____________________________________")
    print("____________________________________")
    print("The student record system")

    try:
        name = input("Enter the student name: ")
        score1 = int(input("Enter the student´s first grade: "))
        score2 = int(input("Enter the second grade for the student: "))
        score3 = int(input("Enter the third score for the student: "))
        score4 = int(input("Enter the forth score for the student: "))

    except:
        print("Error: only numbers are allowed")
        continue

    # using if so no one can enter numbers less than 0 or greater than 100




    if (score1 > 100 or score2 > 100 or score3 > 100 or score4 > 100 or
        score1 < 0 or score2 < 0 or score3 < 0 or score4 < 0):
        print("Numbers should only be from 0 to 100")
        continue



    total_score, average_score = student_system(score1, score2, score3, score4,)
    grade = get_grade(average_score)

    if average_score >= PASS_MARK:
        status = "PASSED"
    else:
        status = "FAILED"

# the output
    print("student record ")
    print(f"Student name: {name}")
    print(f"The total score for the student: {total_score}")
    print(f"The average score: {average_score}")
    print(f"The student grade is: {grade}")
    print(f"The student status is: {status}")

# choice if u want to continue of end the program
    choice = input("Do if want to enter another student record (yes/no): ")
    if choice.lower() != "yes":
        print("program ended")
        break











