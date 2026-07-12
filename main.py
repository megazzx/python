import tkinter as tk
import random

questions = {"What is Python?": "programming language",
             "What is Variable?": "stores value",
             "What is Function?": "block of code",
            "What is OOP?": "object oriented programming",
            "What is keyword?": "reserved word"}
score = 0
count = 0
total_questions = 3
current_question = ""

def start_interview():
    global score, count
    score = 0
    count = 0
    score_label.config(text="Score : 0")
    result_label.config(text="")
    display_question()

def display_question():
    global current_question
    current_question = random.choice(list(questions))
    question_label.config(text=current_question )

def submit():
    global score, count
    answer = answer_entry.get().lower()
    if answer == "":
        result_label.config(text="Enter Answer")
        return
    correct_answer = questions[current_question].lower()
    if answer == correct_answer:
        score += 1
    count += 1
    score_label.config(text="Score : " + str(score))
    answer_entry.delete(0, tk.END)
    if count == total_questions:
        name = name_entry.get()
        result_label.config(text= "Final Score: " +str(score) +"/" + str(total_questions))
        question_label.config(text="Interview Completed")
    else:
        display_question()

def restart():
    global score, count
    score = 0
    count = 0
    question_label.config(text="")
    result_label.config(text="")
    answer_entry.delete(0, tk.END)
    score_label.config(text="Score : 0")
root = tk.Tk()

root.title("Interview Practice System")

root.geometry("800x800")

title = tk.Label(root,text="Interview Practice System")

title.pack(pady=10)

name_label = tk.Label(root,text="Enter Name")

name_label.pack()

name_entry = tk.Entry(root)

name_entry.pack()

start_button = tk.Button(root,text="Start Interview",command=start_interview)

start_button.pack(pady=10)

question_label = tk.Label(root,text="")

question_label.pack(pady=10)

answer_label = tk.Label(root,text="Enter Answer")

answer_label.pack()

answer_entry = tk.Entry(root,width=30)

answer_entry.pack()

submit_button = tk.Button(root,text="Submit",command=submit)

submit_button.pack(pady=10)

score_label = tk.Label(root,text="Score : 0")

score_label.pack()

result_label = tk.Label(root,text="")

result_label.pack(pady=10)

restart_button= tk.Button(root,text="Restart",command=restart)

restart_button.pack(pady=10)

root.mainloop()