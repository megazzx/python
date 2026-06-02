#Create a list of 5 student names
'''l= ["Anu", "Bala", "zara", "Divya", "ziva"]
print(l)'''

#Add a new name to the list
'''l= ["Anu", "Bala", "zara", "Divya", "ziva"]
l.append("Diya")
print(l)'''

#Remove a student name from the list
'''l= ["Anu", "Bala", "zara", "Divya", "ziva"]
l.remove("Bala")
print(l)'''

#Print all elements using loop
'''l= ["Anu", "Bala", "zara", "Divya", "ziva"]
for i in l:
    print(i)'''

#Find largest and smallest number in list
'''n= [10, 25, 5, 40, 15]
maxi=max(n)
mini=min(n)
print("Largest =", maxi)
print("Smallest =", mini)'''

#Count even and odd numbers in list
'''n = [10, 25, 5, 40, 15, 8]
for i in n:
    if i % 2 == 0:
        print("even number")
    else:
        print("odd number")'''

#Reverse a list
'''n = [1, 2, 3, 4, 5]
print(n.reverse())
print(n)'''

#Sort a list in ascending order
'''n = [40, 10, 25, 5]
print(n.sort())
print(n)'''

#Find sum and average of list elements
'''n = [10, 20, 30, 40]
s = sum(n)
avg = s / len(n)
print("Sum =", s)
print("Average =", avg)'''

#Search an element in list
'''n = [10, 20, 30, 40]
i= 40
if i in n:
    print("Found")
else:
    print("Not Found")'''

#Create a tuple with 5 numbers
'''t = (10, 20, 30, 40, 50)
print(t)'''

#Access tuple elements using indexing
'''t = (10, 20, 30, 40, 50)
print(t[0])'''

#Find length of tuple
'''t = (10, 20, 30, 40, 50)
print(len(t))'''

#Count occurrence of an element
'''t = (10, 20, 10, 30, 20)
print(t.count(20))'''

#Find index position of element
'''t = (10, 20, 30, 40)
print(t.index(40))'''

#Slice a tuple
'''t = (10, 20, 30, 40, 50)
print(t[1:3])'''

#Convert tuple into list
'''t = (10, 20, 30)
l = list(t)
print(l)'''

#Convert list into tuple
'''l = [10, 20, 30]
t = tuple(l)
print(t)'''

#Find maximum and minimum value
'''t = (10, 20, 5, 40)
maxi=max(t)
mini=min(t)
print("Max =", maxi)
print("Min =", mini)'''

#Iterate tuple using loop
'''t = (10, 20, 30, 40)
for i in t:
    print(i)'''
    
#Create a set of numbers
'''s = {10, 20, 30, 40}
print(s)'''

#Add elements into set
'''s = {10, 20, 30}
s.add(40)
print(s)'''

#Remove elements from set
'''s = {10, 20, 30}
s.remove(30)
print(s)'''

#Find union of two sets
'''a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)'''

#Find intersection of two sets
'''a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)'''

#Find difference between sets
'''a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)'''

#Remove duplicates from list using set
'''l = [1, 2, 2, 3, 4, 4]
print(list(set(l)))'''

#Check subset and superset
'''a = {1, 2,3,4}
b = {1, 2}
print(a.issuperset(b))
print(b.issubset(a))'''

#Find unique vowels in string
'''s = "information"
vowels = set()
for ch in s:
    if ch in "aeiouAEIOU":
        vowels.add(ch)
print(vowels)'''

#Convert list into set
'''l = [1, 2, 2, 3, 4]
s = set(l)
print(s)'''

#Create a student dictionary with name and marks
'''d = {"name": "Anu","marks": 85}
print(d)'''

#Add new key-value pair
'''d = {"name": "Anu","marks": 85}
d["age"] = 20
print(d)'''

#Update dictionary value
'''d = {"name": "Anu","marks": 85}
d["marks"] = 95'''

#Delete an item from dictionary
'''d = {"name": "Anu","marks": 85}
del d["marks"]
print(d)'''

#Print all keys and values
'''d = {"name": "Anu","marks": 85}
for key, value in d.items():
    print(key, ":", value)
print(d)'''




