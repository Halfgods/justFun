import tkinter as tk
from tkinter import messagebox
import time

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a task from the list
def remove_task():
    try:
        task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Function to mark a task as completed
def complete_task():
    try:
        task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(task_index)
        tasks_listbox.delete(task_index)
        tasks_listbox.insert(tk.END, f"{task} (Completed)")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Pomodoro Timer function
def start_pomodoro():
    work_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60  # 5 minutes break in seconds

    countdown(work_duration, "Work time!")
    messagebox.showinfo("Pomodoro Timer", "Time for a break!")
    countdown(break_duration, "Break time!")

def countdown(duration, message):
    mins, secs = divmod(duration, 60)
    while duration:
        mins, secs = divmod(duration, 60)
        timer_label.config(text=f"{mins:02}:{secs:02}")
        root.update()
        time.sleep(1)
        duration -= 1
    messagebox.showinfo("Pomodoro Timer", message)

# Switch between dark and light modes
def switch_mode():
    if root.cget('bg') == 'black':
        root.config(bg="white")
        task_entry.config(bg="white", fg="black")
        tasks_listbox.config(bg="white", fg="black")
        timer_label.config(fg="black", bg="white")
        mode_button.config(bg="lightgray", fg="black")
        add_button.config(bg="lightgray")
        remove_button.config(bg="lightgray")
        complete_button.config(bg="lightgray")
        pomodoro_button.config(bg="lightgray")
        frame.config(bg="white")
    else:
        frame.config(bg="white")
        root.config(bg="black")
        task_entry.config(bg="gray", fg="black")
        tasks_listbox.config(bg="gray", fg="black")
        timer_label.config(fg="green", bg="black")
        mode_button.config(bg="gray", fg="black")
        add_button.config(bg="gray")
        remove_button.config(bg="gray")
        complete_button.config(bg="gray")
        pomodoro_button.config(bg="gray")
        frame.config(bg="black")

# Creating the main window
root = tk.Tk()
root.minsize(300,400)
root.title("Personal Productivity Assistant")
root.geometry("600x500")
root.config(bg="black")  # Initial mode is dark

# Creating the task entry and buttons (using grid for better organization)
frame = tk.Frame(root)
frame.pack(pady=20)

# Task entry
task_entry = tk.Entry(frame, font=("Arial", 14), width=30, bg="gray", fg="black")
task_entry.grid(row=0, column=0, padx=10, pady=5)

# Add task button
add_button = tk.Button(frame, text="Add Task", font=("Arial", 12), command=add_task, bg="gray", fg="black")
add_button.grid(row=0, column=1, padx=10, pady=5)

# Remove task button
remove_button = tk.Button(frame, text="Remove Task", font=("Arial", 12), command=remove_task, bg="gray", fg="black")
remove_button.grid(row=1, column=3, padx=10, pady=5)

# Mark as completed button
complete_button = tk.Button(frame, text="Mark as Completed", font=("Arial", 12), command=complete_task, bg="gray", fg="black")
complete_button.grid(row=1, column=1, padx=10, pady=5)

# Mode switch button
mode_button = tk.Button(frame, text="Change Mode", font=("Arial", 12), command=switch_mode, bg="gray", fg="black")
mode_button.grid(row=0, column=3, columnspan=1, pady=10)

# Creating the task listbox to show tasks
tasks_listbox = tk.Listbox(root, font=("Arial", 12), height=10, width=40, bg="gray", fg="black")
tasks_listbox.pack(pady=10)

# Timer Section
timer_label = tk.Label(root, font=("Arial", 20), fg="green", bg="black")
timer_label.pack(pady=20)

# Pomodoro button
pomodoro_button = tk.Button(root, text="Start Pomodoro Timer", font=("Courier", 12), command=start_pomodoro, bg="gray", fg="black")
pomodoro_button.pack(pady=10)

# Start the main event loop
root.mainloop()
