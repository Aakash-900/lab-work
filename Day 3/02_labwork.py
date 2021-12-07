#
subject_1 = int(input("Enter marks of the first subject suject:"))
subject_2 = int(input("Enter marks of the second subject suject:"))
subject_3 = int(input("Enter marks of the third subject suject:"))
subject_4 = int(input("Enter marks of the fourth subject suject:"))
avg = (subject_1+subject_2+subject_3+subject_4)/4
percentage: (avg/400)*100
if (avg>=70) :
    print("Grade: A")
elif(avg>=60 and avg <90) :
    print("Grade: B")
elif(avg>=40 and avg <80) :
    print("Grade: c")
elif (avg>=40 and avg <70) :
    print("Grade: D")

else:
    print("Grade: F")


