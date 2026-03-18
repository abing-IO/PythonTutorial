import tkinter as tk
from tkinter import messagebox

def generate_bill():
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())

        total = price * quantity

        if total > 1000:
            total = total * 0.9

        result_var.set(f"{total:.2f}")
    except:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Billing System")
root.geometry("300x220")

tk.Label(root, text="Item Price").pack(pady=5)
price_entry = tk.Entry(root)
price_entry.pack(pady=5)

tk.Label(root, text="Quantity").pack(pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)

tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state="readonly").pack(pady=5)

root.mainloop()