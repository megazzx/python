# to find the last digight of a number 
'''num=int(input("enter a number:"))
print(num % 10)'''

# to remove last digit of the number
'''num = int (input("enter a number:"))
last_digit = num//10
print(" number after removing last digit is:",last_digit)'''

# to find last 2 digits of the given number
'''num = int(input("enter a number:"))
last_digits = num % 100
print(" last 2 digits are:",last_digits)'''

# input distance and time
'''distance = int(input("enter the distance:"))
time = int(input("enter the time:"))
speed = distance/time
print(speed)'''

# bmi calculator
'''weight = int(input("enter the weight:"))
height = int(input("enter the height:"))
bmi = weight/(height/100)**2
print(bmi)'''

# volume of cylinder
'''radius = int(input(" enter the value of radius:"))
height = int(input("enter the value of height:"))
volume = 3.14*radius**radius*height
print(volume)'''

# convert centimeter to meter
'''num = int(input("enter a number:"))
meter = num/100
print(meter)'''

#volume of cuboid
'''length = int(input("enter the value of length:"))
breath = int(input("enter the value of breath:"))
height = int(input("enter the value of height:"))
volume = length*breath*height
print(volume)'''

# to find the last digit of a number
'''num = int(input("enter a number:"))
last_digit = num%10
print("the last digit is:",last_digit)'''

#square the middle digit of a five_digit
'''num = int(input("enter the number:"))
middle = (num//100)%10
square = middle * middle
print("the middle digit is:",square)'''

# expand the number
num = int(input("enter a 4 digit number:"))
a = num // 1000
b = (num // 100)%10
c = (num //10)%10
d = num %10
print(a*1000,"+",b*100,"+",c*10,"+",d)

