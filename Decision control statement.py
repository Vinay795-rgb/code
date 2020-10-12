# age = int(input("Enter the age : "))
# if(age>=18):
#           print("You are eligible to vote")
# else:
#           print("You are not eligilble to vote")

#  Write a program to detrmine the character entered by the user.
# char = input("Press any key : ")
# if(char.isalpha()):
#           print("The user has entered a charcter")
# if(char.isdigit()):
#           print("The user has entered a digit")
# if(char.isspace()):
#           print("The user entered a white space character")    

# #  Write a program to detrmine whether a person is eliglibe to ride a vehicle or not. If ha is not eligble, display how many years are left to be eligible
# age = int(input("Enter the age : "))
# if(age>=18):
#           print("You are eligible to ride a vehicle")
# else:
#           yrs = 18 -age
#           print("You have to wait for another " + str(yrs) +" years to cast your licences for riding a vehicle ")

# #  Write a program to find larger of two numbers.
# a = int((input("Enter the value of a : ")))
# b = int(float(input("Enter the value of b : "))) 
# if(a>b):
#           values1 = a -b
#           print("The value is larger than b " + str(values1) +" is values differene ")
# else:
#           values2 = b -a
#           print("The value is larger than a " + " is value difference ")

#  Write  a program to find whether the given number is even or odd.
# num = int(input("Enter any number : "))
# if(num%2==0):
#           print(num, "is even")
# else:
#           print(num, "is odd")

#  Write a program to enter any character. If the entered character is in lowercase then convert it into uppercase and if it is an uppercase characrter, then convert it into lowercase
# ch = input("Enter any character : ")
# if(ch >= 'A' and ch <= 'Z'):
#           ch = ch.lower()
#           print("The entered character was in uppercase. In lowercase it is : " + ch)
# else:
#           ch = ch.upper()
#           print("The entered character was in lowercase. in uppercase it is : " + ch)

#  Program of company
# ch = input("Enter the gender of the employee (m or f) : ")
# sal = int(input("Enter the salary of the employee : "))
# if(ch=='m'):
#           bonus = 0.05*sal
# else:
#           bonus = 0.10*sal
# amt_to_be_paid = sal+bonus
# print(" Salary = ", sal)
# print(" Bonus = ", bonus)
# print(" ***********************************")
# print("Amount to be paid : ", amt_to_be_paid)

#  Write a program to find whether a given year is a leap year or not
# year = int(input("Enter any year : "))
# if((year%4==0 and year %100!=0) or (year%400 == 0)):
#           print("Leap Year")
# else:
#           print("Not a Leap Year")

#  Write a program that prompt the user to enter a number and then print its interval
# num = int(input("Enter any number from 0-30: "))
# if(num>=0 and num<10):
#           print("It is in the range 0-10")
# if(num>=10 and num<20):
#           print("Its is in range 10-20")
# if(num>=20 and num<30):
#           print("Its is in range 20-30")

#  Write a Program to test whether number entered by user is negative, positive, or equal Zero
# num = int(input("Enter any number : "))
# if(num==0):
#           print("The value is equal to zero")
# elif(num>0):
#           print("The number is positive")
# else:
#           print("The number is negative")

#  Write a program to determine whether to the character entered is a vowel or not
# ch = input("Enter vany character : ")
# if(ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
#           print(ch, "is a vowel")
# elif(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
#           print(ch, "is a vowel")
# else:
#           print(ch, "is not a vowel")

#  Write a programto find greatest number from three numbers
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))
# if(num1>num2):
#           if(num1>num3):
#                     print(num1, "is greater than",num2, "and",num3)
#           else:
#                     print(num3,"is greater than", num1,"and",num2)
# elif(num2>num3):
#           print(num2,"is greater than", num1, "and", num3)
# else:
#           print("The three number are equal ")

#  Write a program that prompt the user to enter a number between 1-7 and then display the corresponding day of the week.
# num = int(input("Enter any number between 1 to 7 : "))
# if(num==1): print("Sunday")
# elif(num==2): print("Monday")
# elif(num==3): print("Tuesday")
# elif(num==4):print("Wednesday")
# elif(num==5):print("Thrusday")
# elif(num==6):print("Friday")
# elif(num==7):print("Saturday")
# else:
#           print("Wrong Input")

#  Write a program to caluclate tax given the follwoing conditions
# If income is less than 1,50, 000 then no tax
# If taxable income is 1,50, 001 - 300,000 then charge 10% tax
# If taxable income is 3,00, 001 - 500,000 then charge 20% tax
# If taxable income is above 5,00,001 then charge 30% tax
# MIN1 = 150001
# MAX1 = 300000
# RATE1 = 0.10
# MIN2 = 300001
# MAX2 = 500000
# RATE2 = 0.20
# MIN3 = 500001
# RATE3 = 0.30

# income = int(input("Enter the income : "))
# taxable_income = income - 150000
# if(taxable_income <=0):
#           print("No tax")
# elif(taxable_income>=MIN1 and taxable_income<MAX1):
#           tax = (taxable_income - MIN1) * RATE1
# elif(taxable_income>=MIN2 and taxable_income<MAX2):
#           tax = (taxable_income - MIN2) * RATE2
# else:
#           tax = (taxable_income-MIN3)*RATE3
# print("TAX = ", tax)

#  Write a program to enter the marks of the students
# marks1 = int(input("Enter the marks in Mathematics : "))
# marks2 = int(input("Enter the marks in Science : "))
# marks3 = int(input("Enter the marks in Social Science : "))
# marks4 = int(input("Enter the marks in Computer Science : "))
# total = marks1+marks2+marks3+marks4
# avg = float(total)/4
# print("Total = ", total,"\t Aggregate = ",avg)
# if(avg>=75):
#           print("Distinction")
# elif(avg>=60 and avg<75):
#           print("First Division")
# elif(avg>=50 and avg<60):
#           print("Second Division")
# elif(avg>=40 and avg<50):
#           print("Third Division")
# else:
#           print("Fail")

#  Write a program to calculate roots of a quadratic equation.
# a = int(input("Enter the values of a : "))
# b = int(input("Enter the values of b : "))
# c = int(input("Enter the values of c : "))
# D = int(input("Enter the values of d : "))
# deno = 2*a
# if(D>0):
#           print("REAL ROOTS")
#           root1 = (-b + D**0.5)/deno
#           root2 = (-b - D**0.5)/deno
#           print("Root1 = ",root1,"\tRoot2 = ",root2)
# elif(D==0):
#           print ("EQUAL ROOTS")
#           root1 = -b/deno
#           print("Root1 and Root2 = ",root1)
# else:
#           print("IMAGINARY ROOTS")