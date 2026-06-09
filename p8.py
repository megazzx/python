# even numbers using function
'''def even_numbers():
    for i in range(1,51):
        if i%2==0:
            print(i)
even_numbers()'''

#sum of two numbers using function
'''def sums(a,b):
    print("sum=",a+b)
sums(3,5)'''

# sum,min,max,avg
'''def multiple_values(lst):
    sums=sum(lst)
    avg=sum(lst)/len(lst)
    maxi=max(lst)
    mini=min(lst)
    return(sums,avg,maxi,mini)
l = multiple_values([10,20,30,40])
print(l)'''

#largest of 3
'''def largest(a,b,c):
    return a,b,c
largest =max(10,2,40)
print(largest)'''

# student details 
'''def student(name,mark):
    print(name)
    print(mark)
student(mark=95,name="mega")'''

#simple interest
'''def simple_interest(p,t,r=100):
    simple_interest=(p*t*r)/100
    print("si=",simple_interest)
simple_interest(1000,4)'''

#power
'''def power(num,expo=2):
    print(num**expo)
power(5)'''

#*args sum
'''def num(*args):
    sums =sum(args)
    print(sums)
num(10,20)'''

#*args largest
'''def num(*data):
    maxi=max(data)
    print(maxi)
num(10,20,30,40)'''

#**kwargs
'''def student(** data):
    print(data)
student(name='mega',blood='b')'''

#**kwargs
'''def employee(**data):
    print(data)
employee(emp_id = 123,emp_name = 'mega')'''

#square using lambda
'''square =lambda x:x*x
print(square(4))'''

#larger of 2 using lambda 
'''large = lambda x,y: x>y
print(max(3,9))'''

#map()
'''celsius=[0,20,30,0]
fahrenheit= list(map(lambda x:(x*9/5)*35,celsius))
print(fahrenheit)'''

# square
'''n=[1,2,3,4]
result =list(map(lambda x:x*2,n))
print(result)'''

# using filter() even number
'''n=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,n))
print(even)'''

# using filter() greater than 100
'''n=[30,50,99,200,100]
result=list(filter(lambda x:x>100,n))
print(result)'''

# power of a number
'''def power(num,expo=2):
    print(num**expo)
power(2)'''

# using recursive() create fibonacci series
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end="")
        c=a+b
        a=b
        b=c
fibonacci(10)
                 


    
    
    
