import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
names = []
marks = []

def add_student(name, mark=0):
    names.append(name)
    marks.append(mark)
    print("Student Added!")

def show_students():
    if len(names) == 0:
        print("No Students Found!")
    else:
        df = pd.DataFrame({
            "Name": names,
            "Mark": marks})
        print(df)

def average_mark():
    if len(marks) == 0:
        print("No Marks Available!")
    else:
        print("Average Mark =", np.mean(marks))

def show_topper():
    if len(marks) == 0:
        print("No Students Found!")
    else:
        max_mark = max(marks)
        index = marks.index(max_mark)

        print("Topper =", names[index])
        print("Mark =", max_mark)

def show_graph():
    if len(marks) == 0:
        print("No Data Available!")
    else:
        plt.bar(names, marks)
        plt.title("Student Marks")
        plt.xlabel("Students")
        plt.ylabel("Marks")
        plt.show()

while True:
    print(" Student Performance Analyzer \n ")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Average Mark")
    print("4. Topper")
    print("5. Graph")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        mark = int(input("Enter Mark: "))
        add_student(name, mark)

    elif choice == "2":
        show_students()

    elif choice == "3":
        average_mark()

    elif choice == "4":
        show_topper()

    elif choice == "5":
        show_graph()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")