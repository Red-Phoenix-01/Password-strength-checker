import tkinter as tk
from tkinter import ttk
import re

def check_strength(password):
    score = 0
    criteria = {
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Special Char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
        "Length ≥ 8": len(password) >= 8
    }

    score = sum(criteria.values())

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score == 3 or score == 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, color, criteria

def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_btn.config(text='Hide')
    else:
        entry.config(show='*')
        toggle_btn.config(text='Show')

def on_key_release(event=None):
    pwd = entry.get()
    strength, color, criteria = check_strength(pwd)
    result_label.config(text=f"Strength: {strength}", fg=color)
    strength_bar['value'] = sum(criteria.values()) * 20

    for key in criteria_labels:
        criteria_labels[key].config(
            fg="green" if criteria[key] else "gray"
        )

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x350")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", thickness=20, background="green")

tk.Label(root, text="Enter your password", font=('Segoe UI', 14), bg="#1e1e1e", fg="white").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

entry = tk.Entry(frame, width=30, show='*', font=('Segoe UI', 12))
entry.pack(side="left", padx=5)
entry.bind("<KeyRelease>", on_key_release)

toggle_btn = tk.Button(frame, text="Show", command=toggle_password, bg="#444", fg="white")
toggle_btn.pack(side="left", padx=5)

strength_bar = ttk.Progressbar(root, length=300, mode='determinate')
strength_bar.pack(pady=10)

result_label = tk.Label(root, text="", font=('Segoe UI', 16, 'bold'), bg="#1e1e1e")
result_label.pack(pady=10)

criteria_labels = {}
criteria_frame = tk.Frame(root, bg="#1e1e1e")
criteria_frame.pack(pady=10)

for text in ["Lowercase", "Uppercase", "Digit", "Special Char", "Length ≥ 8"]:
    lbl = tk.Label(criteria_frame, text=f"• {text}", font=('Segoe UI', 11), fg="gray", bg="#1e1e1e")
    lbl.pack(anchor="w")
    criteria_labels[text] = lbl

root.mainloop()
