def student_attendance(attendance_percentage):
    low_percentage = [percentage for percentage in attendance_percentage if percentage < 75]
    eligible_students = [percentage for  percentage in attendance_percentage if percentage>=75]
    sorted_attendance = sorted(attendance_percentage, reverse = True)
    top_attendance = sorted_attendance[:3]

    print("Students below 75 percentage are:",*low_percentage)
    print("Students eligible for exams count:",len(eligible_students) )
    print("Top 3 attendance percentages:",*top_attendance)

attendance_percentage = list(map(int,input("Enter the students attendance percentage: ").split()))
student_attendance(attendance_percentage)


# Enter the students attendance percentage: 45 94 86 76 97 65
# Students below 75 percentage are: 45 65
# Students eligible for exams count: 4
# Top 3 attendance percentages: 97 94 86