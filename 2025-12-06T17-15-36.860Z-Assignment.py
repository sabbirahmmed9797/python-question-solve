#QUESTION NO:1
#write a python program that takes a number as input and chack whether it is even or odd

num1=int(input("enter the number:"))
if(num1 % 2==0):
    print("the number is even")
else:
    print("the number is odd")


#QUESTION NO:2
#wrtes a program that takes two numbers and an oprator(+,-,*,/)and performs the calculation

num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
oprator=input("Enter operator (+, -, *, /): ")
if(oprator=="+"):
    print(num1+num2)
elif(oprator=='-'):
    print(num1 - num2)
elif( oprator == '*'):
    print(num1 * num2)
elif (oprator == '/'):
    print(num1 / num2)
else:
    print("Invalid operator")



    #QUESTION NO-3
"""write a program that using the for loop that calculate the sum of even numbers 
between 1 to 100"""

a=0
for i in range(2, 101, 2): 
    a += i

print("Sum of even numbers from 1 to 100 is:", a)