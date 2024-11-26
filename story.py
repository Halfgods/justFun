import tkinter as tk
import random
# Story: Daily story of a college student
story = {
    "start": {
        "text": "You wake up to your alarm ringing at 5:30 AM. Do you wanna sleep more or get up?",
        "choices": {"Sleep": "late_start", "Get Up": "on_time"}
    },
    "late_start": {
        "text": "You snooze and oversleep until 8:40 AM. You miss breakfast but you reach 15 minutes before your first class ends. Do you apologize to the professor or sneak in quietly?",
        "choices": {"Apologize to sir!": "awkward_class", "Sneak In quietly": "first_class"}
    },
    "on_time": {
        "text": "You get up, have a healthy breakfast, and attend your first class feeling energetic. Do you take notes actively or do masti during the lecture?",
        "choices": {"Take Notes": "productive_day", "Do Masti": "lazy_day"}
    },
    "awkward_class": {
        "text": "Your professor accepts your apology but reminds you to be On time next time. You feel awkward but manage to focus the lecture. Do you stay for extra help after class or leave?",
        "choices": {"Stay & Study": "helpful_session", "Leave": "break_time"}
    },
    "first_class": {
        "text": "You sneak in quietly and try to catch up your best but You’re unsure of what’s going on. Do you ask a friend for notes or try to figure it out yourself?",
        "choices": {"Ask a Friend": "productive_day", "Figure it Out": "lazy_day"}
    },
    "productive_day": {
        "text": "Your effort pays off.You have some free time. Do you go to the library to study or hang out with friends?",
        "choices": {"Library": "study_session", "Hang Out": "fun_time"}
    },
    "lazy_day": {
        "text": "You struggle to keep up and feel unmotivated. Do you try to plan next day or just leave it ?",
        "choices": {"Turn Things Around": "productive_day", "Call It a Day": "end_day"}
    },
    "helpful_session": {
        "text": "The professor's tips help you understand the trick for exams better. You feel motivated to tackle your assignments & Exams. Do you start your Preparations or Do it one night Before?",
        "choices": {"Start Preparations": "productive_day", "Last night before Exam": "fun_time"}
    },
    "break_time": {
        "text": "You take a break and scrolled reels. You feel relaxed. Do you join a study group or spend the rest of the day Scrolling?",
        "choices": {"Study Group": "study_session", "Scrolling": "fun_time"}
    },
    "study_session": {
        "text": "You have a productive study session and feel prepared for upcoming exams.\n Congratulations on a successful day!",
        "choices": {}
    },
    "fun_time": {
        "text": "You Enjoyed a fun day with friends but realize you’re going to fail in Exams.You feel Tensed \nTry to not waste your time!!!",
        "choices": {}
    },
    "end_day": {
        "text": "You decide to take it easy today. Tomorrow is a new day to do every thing!!",
        "choices": {}
    }
}

def random_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

# Tkinter application
class StudentStoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A Student's Day")
        
        self.story_text = tk.Label(root, text="", font=("Times", 16), wraplength=400, bg=random_color(), fg="black", pady=20)
        self.story_text.pack(pady=10)

        self.buttons_frame = tk.Frame(root, bg="darkgrey")
        self.buttons_frame.pack()

        self.current_scene = "start"
        self.display_scene(self.current_scene)

    def display_scene(self, scene):
        # Clear previous buttons
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        
        # Update story text
        self.story_text.config(text=story[scene]["text"])
        bg="black",
        fg=random_color()

        # Create buttons for choices
        for choice, next_scene in story[scene]["choices"].items():
            btn = tk.Button(self.buttons_frame, text=choice, font=("Arial", 14),
                            command=lambda ns=next_scene: self.display_scene(ns), bg="darkgrey", fg="black")
            btn.pack(side="left", padx=10, pady=5)

# Run the app
root = tk.Tk()
app = StudentStoryApp(root)
root.geometry("600x400")
root.config(bg=random_color())
# frame=root.config(bg="black")
root.mainloop()
