# random
import random as r
l=[10,20,30,40]
print("random():",r.random())
print("randint():",r.randint(0,100))
print("randrange():",r.randint(0,100))
print("choice():",r.choice(l))
print("uniform():",r.uniform(0,100))
print("sample():",r.sample(l,k=4))

#numpy
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(np.sum(a))
print(np.mean(a))
print(np.sort(a))
print(np.max(a))
print(np.min(a))

#scipy
from scipy import stats
data=[10,20,30,40,40,40]
result=stats.mode(data)
print("mode=",result[0])
stats.tmean(data)

#pandas
import pandas as pd
s=pd.Series([10,20,30,40,40,40,40])
print(s)

data={'name':['john','anna','peter'],
      "age":[28,24,35]}
df=pd.DataFrame(data)
print(df)

from collections import deque
q=deque()
q.append(1)
q.append(2)
q.append(3)
print("queue:",list(q))
print("removed:",q.popleft())
print("queue after deleting:",list(q))

#matplotlib
import matplotlib .pyplot as plt
x=[1,2,3,4,]
y=[10,20,25,30]
plt.plot(x,y)
plt.title("graph")
plt.xlabel("x axis")
plt.ylabel("y axis")

#bar chart
import matplotlib.pyplot as plt
course=['ece','cse','aiml']
fees=[80,90,100]
plt.bar(course,fees)
plt.xlabel("course")
plt.ylabel("fees")
plt.title("course fees")
plt.show()

#drawing a circle
import turtle
t=turtle.Turtle()
t.speed(3)
t.circle(100)
turtle.done()

#drawing a square
import turtle
t=turtle.Turtle()
t.speed(3)
for i in range(4):
      t.forward(100)
      t.right(90)
turtle.done()