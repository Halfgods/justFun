import tkinter as tk
# Function to check password strength
def check_password_strength():
    password = entry.get()  # Get password from entry field
    score = 0

    # Evaluate password
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()" for char in password):
        score += 1

    # Calculate percentage
    percentage = (score / 5) * 100

    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate "
    else:
        strength = "Strong"
    

    # Display the result
    result_label.config(text=f"Score: {percentage:.0f}%\nPassword Strength: {strength}")


# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="black")

# Create and place widgets

label = tk.Label(root, text="Enter your password:", font=("Timer", 18), fg="white", bg="black")
label.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Courier", 12), width=30, bg="gray", fg="white", insertbackground="white")
entry.pack(pady=10)


button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Times", 12), bg="gray", fg="black")
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 12), fg="white", bg="black")
result_label.pack(pady=10)

label = tk.Label(root, text="Made By Our Group", font=("Times", 11),bg="black", fg="skyblue1")
label.pack(pady=10)


# Start the Tkinter event loop
root.mainloop()