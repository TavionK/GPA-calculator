Grades = []
NumberOfCreds = []
QPList = []
NameOfCourses = []
overallCreds=[]
overallQualPoints=[]
def gpa_calc(quality_points, credit_hours):
    semester_gpa = quality_points/credit_hours
    semester_gpa = ('%.2f' % semester_gpa)
    return semester_gpa

def final_gpa_calc(overall_qual, overall_cred):
    final_gpa = overall_qual / overall_cred
    final_gpa = ('%.2f' % final_gpa)
    return final_gpa

def quality_calc(num_cred, grade):
    if grade== 'A':
        class_quality_points = 4.00 * num_cred
    elif grade == 'A-':
        class_quality_points = 3.70 * num_cred
    elif grade == 'B+':
        class_quality_points = 3.30 * num_cred
    elif grade == 'B':
        class_quality_points = 3.00 * num_cred
    elif grade == 'B-':
        class_quality_points = 2.70 * num_cred
    elif grade == 'C+':
        class_quality_points = 2.30 * num_cred
    elif grade == 'C':
        class_quality_points = 2.00 * num_cred
    elif grade == 'C-':
        class_quality_points= 1.70 * num_cred
    elif grade == 'D+':
        class_quality_points = 1.30 * num_cred
    elif grade == 'D':
        class_quality_points= 1.00 * num_cred
    else:
        class_quality_points = 0.0
    return class_quality_points

print('Welcome to the GPA calculator.')
ans = input("Would you like to calculate your GPA for a semester? Enter Y/N:")
while ans =='Y' or ans =='y':
    num_courses=int(input("How many courses did you take in the term:"))
    for i in range(num_courses):
        print("Enter the name of the course", i+1, ':', end=' ')
        courseName = input()
        NameOfCourses.append(courseName)
        credit=int(input("Enter the number of credits associated with this course:"))
        NumberOfCreds.append(credit)
        Grade=input("Enter the grade for this course:")
        Grades.append(Grade)
        quality_point=quality_calc(credit, Grade)
        QPList.append(quality_point)
        totalCred=sum(NumberOfCreds)
        totalQual=sum(QPList)
        overallCreds.append(credit)
        overallQualPoints.append(quality_point)
        GPA= gpa_calc(totalQual, totalCred)
    print("This term you earned:")
    print("%-10s %-10s %-10s %-15s" %("Course","Credits","Grade","Quality Points"))
    for i in range(0,len(NumberOfCreds)):
        print("%-10s %-10s %-10s %-15s" %(NameOfCourses[i],NumberOfCreds[i],Grades[i],QPList[i]))
        
    print("Total credits for this term:", totalCred)
    print("You earned", totalQual, "total quality points and a GPA of", GPA, "for the semester.")
    NameOfCourses.clear()
    NumberOfCreds.clear()
    Grades.clear()
    QPList.clear()
    ans= input("Would you like to calculate another term's GPA? Enter Y/N:")

overallQual = sum(overallQualPoints)
overallCred = sum(overallCreds)
if overallQual != 0:
    finalGPA = final_gpa_calc(overallQual, overallCred)
    print("Your overall total credits are", overallCred)
    print("Your overall GPA: ", finalGPA)
print("Thanks for using the software!")
