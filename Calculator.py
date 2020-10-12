#  Generating calculator
import math
print("\t____CALCULATOR____")

def sum(a, b):
    a+=b
    return a

def sub(a, b):
    if a > b:
        a-=b
        return a
    else :
        b-=a
        return b

def mul(a,b):
    a*=b
    return a

def div(a, b):
    q=a/b
    r=a%b
    print("\nThe quotient is : %s" %q)
    print("\nThe reminder is : %s" %r)

def sqr(a):
    x= math.sqrt(a)
    return x

while (True):
    print("\n\nChoose the operation you want to perform: ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SQUARE ROOT")
    print("\n\t6.EXIT")

    Choice = int(input(' > '))

    if Choice==1 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(' > '))
        num2 = int(input(' > '))
        s=sum(num1,num2)
        print("The sum is : %s" %s)

    elif Choice==2 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(' > '))
        num2 = int(input(' > '))
        m=sub(num1,num2)
        print("\nThe difference is: %s" %m)
    elif Choice==3 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(' > '))
        num2 = int(input(' > '))
        p=mul(num1,num2)
        print("\nThe difference is: %s" %p)
    elif Choice==4 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(' > '))
        num2 = int(input(' > '))
        div(num1,num2)
    elif Choice==5 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(' > '))
        r=sqr(num1)
        print("\nThe square root is: %s" %r)
    else:
        print("\nYou choce to exit.Bye.......")
        break