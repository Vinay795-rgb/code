# # string operation
# # str = 'Python is Easy !!!'
# # print(str)
# # print(str[0])
# # print(str[3:9])
# # print(str[4:])
# # print(str[-1])
# # print(str[:5])
# # print(str * 2)
# # print(str + "ISNT'T IT?")

# #  TUPLES
# # Tup = ('a', 'bc', 78, 1.23)
# # Tup2 = ('d', 78)
# # print(Tup)
# # print(Tup[0])
# # print(Tup[1:3])
# # print(Tup[2:])
# # print(Tup *2)
# # print(Tup + Tup2)

# #  Program to Demonstarate operation on lists
# # list = ['a', 'bc', 89, 1.867]
# # list2 = ['d', 99]
# # print(list)
# # print(list[0])
# # print(list[1:3])
# # print(list[2:])
# # print(list *2)
# # print(list + list2)

# #  Program to demonstrate operation the use of dicitionary
# # dict = {"Item" : "Dairy-Milk", "Price" : 100}
# # print(dict["Item"])
# # print(dict["Price"])

# #  Write a program to enter a number and display its hex and octal equivalent and its square root
# # num = int(input("Enter a number : "))
# # print("Hexadecimal of " + str(num) + " : " + str(hex(num)))
# # print("Octal of " + str(num) + " : " + str(oct(num)))
# # print("Square root of " + str(num) + " : " + str(num**0.5))

# #  Write a program to read and print values of variables of differnt data types.
# # num = int(input("Enter the value of num : "))
# # amt = float(input("Enter the value of amt : "))
# # pi = float(input("Enter the value of pi : "))
# # code = str(input("Enter the value of code : "))
# # population_of_India = int(input("Enter the value of population of India : "))
# # msg = str(input("Enter the value of message : "))
# # # Print The values of variables
# # print("NUM = " + str(num) + "\n AMT = " + str(amt) + "\n CODE = " + str(code) + "\n POPULATION OF INDIA = " + str(population_of_India) + "\n MESSAGE = " + str(msg))

# #  Write a program to calculate area of triangle using Heron's Formula
# # (Hint: Heron's formula is given as area = sqrt(S*(S-a)*(S-b)*(S-c)))
# # a = float(input("Enter the first side of the triangle : "))
# # b = float(input("Enter the second side of the triangle : "))
# # c = float(input("Enter the third side of the triangle : "))
# # print(a,b,c)
# # S = (a+b+c)/2
# # area = (S*(S-a)*(S-b)*(S-c))**0.5
# # print("Area = " + str(area))

# #  Write a program to calculate the distance between two points.
# # x1 = (int(input("Enter the x coordinate of the first point : ")))
# # y1 = (int(input("Enter the y coordinate of the first point : ")))
# # x2 = (int(input("Enter the x coordinate of the second point : ")))
# # y2 = (int(input("Enter the x coordinate of the second point : ")))
# # distance = ((x2-x1)**2+(y2-y1)**2)**0.5
# # print("Distance = ")
# # print(distance)

# #  Program to perform addition,subtraction,multiplication,division,interger division and modulo division on two integer numbers
# # num1 = int(input("Enter two numbers : "))
# # num2 = int(input("Enter two numbers : "))
# # add_res = num1+num2
# # sub_res = num1-num2
# # mul_res = num1*num2
# # idiv_res = num1/num2
# # modiv_res = num1%num2
# # fdiv_res = float(num1)/num2
# # print(str(num1)+" + "+str(num2)+" = "+str(add_res))
# # print(str(num1)+" - "+str(num2)+" = "+str(sub_res))
# # print(str(num1)+" * "+str(num2)+" = "+str(mul_res))
# # print(str(num1)+" / "+str(num2)+" = "+str(idiv_res)+" (Integer Division)")
# # print(str(num1)+" // "+str(num2)+" = "+str(fdiv_res)+" (Float Division)")
# # print(str(num1)+" % "+str(num2)+" = "+str(idiv_res)+" (Modulo Division)")

# #  Write a program to perform addition, subtraction, division and multiplication on two floating point numbers 
# # num1 = float(input("Enter two numbers : "))
# # num2 = float(input("Enter two numbers : "))
# # add_res = num1+num2
# # sub_res = num1-num2
# # mul_res = num1*num2
# # di_res = num1/num2
# # print(str(num1)+" + "+str(num2)+" = "+" %.2f"%add_res)
# # print(str(num1)+" - "+str(num2)+" = "+" %.2f"%sub_res)
# # print(str(num1)+" * "+str(num2)+" = "+" %.2f"%mul_res)
# # print(str(num1)+" / "+str(num2)+" = "+" %.2f"%div_res)

# #  Write a program that demonstrate the use of relational operation
# x= 10
# y= 20
# print(str(x)+" < "+str(y)+" = "+str(x<y))
# print(str(x)+" == "+str(y)+" = "+str(x==y))
# print(str(x)+" != "+str(y)+" = "+str(x!=y))
# print(str(x)+" >= "+str(y)+" = "+str(x>=y))
# print(str(x)+" <= "+str(y)+" = "+str(x<=y))


#  Write a program to calculte area of a circle
# radius = float(input("Enter the radius of the circle : "))
# area = 3.14*radius*radius
# circumference = 2*3.14*radius
# print("AREA = "+str(round(area, 2))+"\t CIRCUMFERENCE = "+str(round(circumference, 2)))

#  Write a program to print the digit at one's place of anumber.
# num = int(input("Enter any number : "))
# digit_at_ones_place = num%10
# print("The digit at ones place of "+str(num)+" is "+str(digit_at_ones_place))

#  Write a program to calculate average of two numbers. Print thier derivation
# num1 = int(input("Enter the two numbers : "))
# num2 = int(input("Enter the two numbers : "))
# avg = (num1+num2)/2
# dev1 = num1-avg
# dev2 = num2-avg
# print("AVERAGE = ", avg)
# print("DERIVATION of first num = ", dev1)
# print("DERIVATION of second num = ", dev2)

#  Write a program to convert degrees fahernheit into degree celicus
# fahernheit = float(input("Enter the temperature in fahernheit : "))
# celsicus = (0.56)*(fahernheit-32)
# print("Temperature in degree celsicus = ",celsicus)

#  Write a program to calculate the total amount of money in the piggybank, given the coins of Rs10, Rs5, Rs2, and Re1
# num_of_10_coins = int(input("Enter the number of 10Rs coins in the piggybank : "))
# num_of_5_coins = int(input("Enter the number of 5Rs coins in the piggybank : "))
# num_of_2_coins = int(input("Enter the number of 2Rs coins in the piggybank : "))
# num_of_1_coins = int(input("Enter the number of 1Rs coins in the piggybank : "))
# total_amt = num_of_10_coins*num_of_5_coins*5+num_of_2_coins*2+num_of_1_coins
# print("Total amount in thre piggybank = ", total_amt)

#  Write a program to detrmine whether a person is eligilble to vote
age = int(input("Enter the age : "))
if(age>=18):
          print("You are eligible to vote")
else:
          print("You are not eligible to vote")