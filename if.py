year = int(input("Enter a year: "))
arrear = int(input("Enter the arrear: "))
income = int(input("Enter the income: "))
score = int(input("Enter the score: "))
age = int(input("Enter the age: "))
attendence = int(input("Enter the attendance: "))
flag = False

if year>=2021 and arrear<=2 and income<=2000000 and 18<=age<21  and score>=60 and attendence>=80:
    print("You are eligible for the scholarship")
    flag = True

if arrear>2:
    if score>=60 and attendence>=90:
        print("You are eligible for the scholarship")
if 20000000<=income<25000000 and flag==True:
    print("Half the scholarship is awarded to you")


