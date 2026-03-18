import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        a = int(entry1.get())
        b = int(entry2.get())

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            result = a / b

        result_var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Add", command=lambda: calculate("add")).grid(row=0, column=0)
tk.Button(frame, text="Subtract", command=lambda: calculate("sub")).grid(row=0, column=1)
tk.Button(frame, text="Multiply", command=lambda: calculate("mul")).grid(row=0, column=2)
tk.Button(frame, text="Divide", command=lambda: calculate("div")).grid(row=0, column=3)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state="readonly").pack(pady=10)

root.mainloop()