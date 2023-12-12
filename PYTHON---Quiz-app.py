import tkinter as tk
import sqlite3
import random

# Create a connection to the database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a table to store questions and options
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        answer INTEGER
    )
''')

# Function to fetch a random question
def fetch_question():
    cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1')
    return cursor.fetchone()

# Function to display a question
def display_question():
    question_data = fetch_question()
    question_label.config(text=question_data[1])
    options = question_data[2:6]
    for i in range(4):
        option_buttons[i].config(text=options[i])

# Function to check the answer
def check_answer(option_index):
    question_data = fetch_question()
    correct_answer = question_data[6]
    if option_index == correct_answer:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect!")

# Create GUI
root = tk.Tk()
root.title("Random Question Game")

question_label = tk.Label(root, text="", wraplength=300)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=30, command=lambda idx=i: check_answer(idx))
    btn.pack(pady=5)
    option_buttons.append(btn)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Display initial question
display_question()

root.mainloop()

# Close the database connection when done
conn.close()
