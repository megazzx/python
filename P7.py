#max of 3
'''a=2
b=3
c=9
print(max(a,b,c))'''

#min value in a list
'''l=[10,5,20]
print(min(l))'''

# length of a string
'''a = "moon"
print(len(a))'''

#sum of elements in a list
'''l =[1,2,3,4]
print(sum(l))'''

#float to int
'''f = 2.5
print(int(f))'''

#int to str
'''i=23
print(str(i))'''

#power using pow()
'''print(pow(2,2))'''

# absolute value
'''print(abs(-2))'''

#type
'''print(type(5+6j))'''

#print hello world
'''def hello():
    print("hello world")
hello()'''

# add two numbers
'''def add(a,b):
    print(a+b)
add(9,3)'''

#even or odd
'''def even_odd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even_odd(4)'''

#square
'''def square(n):
    print(n*n)
square(4)'''

#tables
'''def tables(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
tables(3)'''

#factorial
'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
factorial(5)'''

# prime number
'''def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i == 0:
            c+=1
    if c==2:
        print("prime")
    else:
        print("not prime")
prime(3)'''

#count vowels
'''def vowels(s):
    count= 0
    for ch in s:
        if ch in "AEIOUaeiou":
            count+=1
    print(count)
vowels("notebook")'''

#reverse a number
'''def reverse(n):
    print(str(n)[::-1])
reverse(1234)'''

#largest among 3 numbers
'''def largest(a,b,c):
    print(max(a,b,c))
largest(10,20,40)'''

#return sum of two numbers
'''def add(a,b):
    return a+b
result=add(5,8)
print(result)'''

#return cube of a number
'''def cube(n):
    return n**3
result =cube(2)
print(result)'''

#return area of circle
'''def area(n):
    return 3.14*n*n
result=area(5)
print(result)'''

# return leap year or not
'''def leap(year):
    if year %4==0:
        return "leap year"
    else:
        return "not a leap year"
y = leap(2004)
print(y)'''

# return factorial
def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact*=i
    return fact
f =factorial(5)
print(f)
