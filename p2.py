# find bitwise XOR of tow numbers

'''a = 2
b = 3
print(a^b)'''

# find bitwise NOT of two numbers
'''a = 2
b = 3
print (~a)'''

# check whether a number is even using bitwise operator

'''num =int(input(" enter a number:"))
if(num & 1) == 0:
    print(" even number")
else:
    print("odd number")'''

# swap two numbers using XOR operator

'''a = 2
b = 3
a = a^b
b = b^a
c = a^b
print("a=",c)
print("b=",b)'''

# find bitwise AND of two numbers
'''a = 2
b = 3
print(a&b)'''

# find bitwise OR of two numbers
'''a = 2
b = 3
print(a|b)'''

# bill amount
'''bill = int(input("enter the bill amount:"))
gst = bill *18/100
total = bill +gst
print("gst:",gst)
print("total amount:", total)'''

# average weight of 5 persons
'''a = int(input("enter the weight of the first person:"))
b = int(input("enter the weight of the second person:"))
c = int(input("enter the weight of the third person:"))
d = int(input("enter the weight of the fourth person:"))
e = int(input("enter the weight of the fifth person:"))
average = a+b+c+d+e/5
print(average)'''

# find square of a number
'''num = int(input("enter a number:"))
square = num*num
print("square:",square)'''

# cube of the number
'''num = int(input("enter the number:"))
cube = num *num*num
print("cube of the number is:",cube)'''

#compare two numbers equal or not
'''a= int(input("enter a number 1:"))
b=int(input("enter a number 2:"))
if a==b:
    print("the numbers are equal:")
else:
    print("the numbers are not equal:")'''

# check first num greater than second
'''a= int(input("enter a number 1:"))
b=int(input("enter a number 2:"))
if a>b:
    print("number1 is greater:")
else:
    print("number2 is smaller:")'''

# check the number is less than 50
'''num = int(input("enter the number:"))
if num<50:
    print("the number is less than 50:")
else:
    print("the number is greater than 50:")'''

# compare using >= operator   
'''a= int(input("enter a number 1:"))
b=int(input("enter a number 2:"))
if a>=b:
    print("number1 is greater or equal:")
else:
    print("number2 is smaller:")'''

# check two values are not equal
'''a= int(input("enter a number 1:"))
b=int(input("enter a number 2:"))
if a!=b:
    print("the numbers are not equal:")
else:
    print("the numbers are equal:")'''
    
# check number exists in list
'''l =[1,2,3,4,5]
num = int(input("enter a number:"))
if num in l:
    print("the number exists in list:")
else:
    print("the number does not exists in list:")'''

# ci
'''principal = int(input("Enter principal amount: "))
rate = int(input("Enter annual interest rate: "))
time = int(input("Enter time : "))
amount = principal * (1 + rate / 100) ** time
Compound_Interest= amount - principal
print("compound interest:", Compound_Interest)'''

# membership operator
'''l= [2,3,4,5,6,7]
num = int(input("enter a number:"))
if num in l:
    print("number exists")
else:
    print("number does not exists")'''

# check using is operator
'''a = 25
b = 25
print(a is b)'''

# check using is not operator
a = 11
b = a
print(a is not b)
    


