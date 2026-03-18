import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        c = float(entry.get())
        f = (c * 9/5) + 32
        result_var.set(f"{f:.2f}")
    except:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

tk.Label(root, text="Enter Celsius:").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Convert to Fahrenheit", command=convert).pack(pady=10)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, state="readonly")
result_entry.pack(pady=5)

root.mainloop()