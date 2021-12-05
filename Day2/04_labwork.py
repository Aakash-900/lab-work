# labsession question number 4
No_students = int(input("Enter the number of students: "))
No_apple = int(input("Enter the number of apple: "))
Eachwillget = (No_apple//No_students)
Remaining = (No_apple % No_students)
print(f"Each student will get {Eachwillget}")
print(f"No of apple will remain {Remaining}")