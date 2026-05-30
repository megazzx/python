#diamond pattern
'''for i in range(1,10):
    for j in range (i+1,10):
        print(" ",end="")
    for k in range(1,i):
        print("* ",end="")
    print()
for i in range(1,10):
    for m in range (1,i):
        print(" ",end="")
    for n in range(i+1,10):
        print("* ",end="")
    print()'''

#printing letters in pattern 
'''for i in range (1,6):
    for j in range(1,6):
        if j==5 or j==1:
            print("@",end=" ")
        elif i==j and i<=3 :
            print("@",end=" ")
        elif i==2 and j==4:
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#spy number
'''n = int(input("enter a number:"))
sums = 0
product =1
t = n
while t>0:
    d = t%10
    sums+=d
    product*=d
    t//=10
if sums == product:
    print(" spy number")
else:
    print("not a spy number")'''

# harshad number
'''n = int(input("enter a number:"))
sums = 0
t = n
while t>0:
    sums += t %10
    t//=10
if n % sums == 0:
    print("harshad number")
else:
    print("not a harshad number")'''
#armstrong number
'''n = int(input("enter a number:"))
t = n
total=0
while t>0:
    d = t%10
    total += d**3
    t//=10
if total == n:
    print(" armstrong number")
else:
    print("not a armstrong number")'''

#factorial 
'''n = int(input("Enter a number: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c'''

# prime number
'''n = int(input("Enter number: "))
count = 0
for i in range(1, n+ 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")'''

#buzz number
'''num = int(input("Enter number: "))
if num % 7 == 0:
    print("buzz number")
else:
    print("not a buzz number")'''

#automorphic number
n = int(input("Enter number: "))
square = n * n
if square % 10 == n:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")
