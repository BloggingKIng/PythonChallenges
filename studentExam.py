# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
# allow student to sit if he/she has medical cause

totalClasses =  int(input("Enter the total number of classes   "))
attendedClasses = int(input("Enter the number of attended classes  "))

percentage = (attendedClasses/totalClasses) * 100

if percentage < 75:
    cause = input("Was abscence because of a Medical case? Y/N")

    if cause.lower()  == 'y':
        print("The student is allowed to sit in exams")
    else:
        print("Sorry you are not allowed to sit in exams ")
        print("Its because you have attended only {} classes".format(percentage))

else:
    print("Student is allowed to sit in exams")
    print("He attended {} percent class".format(percentage))

    
