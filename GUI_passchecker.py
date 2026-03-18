import tkinter as tk

def check_strength():
    pwd = entry.get()
    strength = "Weak"

    has_digit = any(char.isdigit() for char in pwd)
    has_special = any(not char.isalnum() for char in pwd)

    if len(pwd) >= 8 and has_digit and has_special:
        strength = "Strong"
    elif len(pwd) >= 6 and (has_digit or has_special):
        strength = "Moderate"

    result_var.set(strength)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

tk.Label(root, text="Enter Password").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state="readonly").pack(pady=5)

root.mainloop()