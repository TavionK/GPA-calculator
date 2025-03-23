Grades = []
NumberOfCreds = []
QPList = []
NameOfCourses = []
overallCreds=[]
overallQualPoints=[]
def GPAcalc(qualityPoints, creditHours):
    GPA = totalQual/totalCred
    GPA = ('%.2f' % GPA)
    return GPA

def FinalGPAcalc(overallQual, overallCred):
    GPA = overallQual/overallCred
    GPA = ('%.2f' % GPA)
    return GPA

def qualityCalc(numCred,Grade):
    if (Grade=='A'):
        qualitypoint =4.00*numCred
    elif (Grade=='A-'):
        qualitypoint = 3.70*numCred
    elif (Grade=='B+'):
        qualitypoint =3.30*numCred
    elif (Grade=='B'):
        qualitypoint =3.00*numCred
    elif (Grade=='B-'):
        qualitypoint =2.70*numCred
    elif (Grade=='C+'):
        qualitypoint =2.30*numCred
    elif (Grade=='C'):
        qualitypoint =2.00*numCred
    elif (Grade=='C-'):
        qualitypoint=1.70*numCred
    elif (Grade=='D+'):
        qualitypoint =1.30*numCred
    elif (Grade=='D'):
        qualitypoint=1.00*numCred
    else:
        qualitypoint = 0.0
    return qualitypoint

print('Welcome to the GPA calculator.')
ans = input("Would you like to calculate your GPA for a semester? Enter Y/N:")
while ans =='Y' or ans =='y':
    Numcourses=int(input("How many courses did you take in the term:"))
    for i in range(Numcourses):
        print("Enter the name of the course", i+1, ':', end=' ')
        courseName = input()
        NameOfCourses.append(courseName)
        credit=int(input("Enter the number of credits associated with this course:"))
        NumberOfCreds.append(credit)
        Grade=input("Enter the grade for this course:")
        Grades.append(Grade)
        qualitypoint=qualityCalc(credit,Grade)
        QPList.append(qualitypoint)
        totalCred=sum(NumberOfCreds)
        totalQual=sum(QPList)
        overallCreds.append(credit)
        overallQualPoints.append(qualitypoint)
        GPA= GPAcalc(totalQual,totalCred)
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
ans
overallQual = sum(overallQualPoints)
overallCred = sum(overallCreds)
if (overallQual != 0):
    finalGPA = FinalGPAcalc(overallQual,overallCred)
    print("Your overall total credits are", overallCred)
    print("Your overall GPA: ", finalGPA)
print("Thanks for using the software!")
