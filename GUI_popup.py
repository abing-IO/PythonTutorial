import tkinter as tk
from tkinter import messagebox

def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == "" or pwd == "":
        messagebox.showwarning("Error", "Username or Password cannot be empty")
    elif user == "admin" and pwd == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()