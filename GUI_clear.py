import tkinter as tk

def clear_label():
    label.config(text="")
    clear_btn.config(state=tk.DISABLED)
    restore_btn.config(state=tk.NORMAL)

def restore_label():
    label.config(text="Python GUI Demo")
    restore_btn.config(state=tk.DISABLED)
    clear_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("GUI Demo")
root.geometry("300x150")

label = tk.Label(root, text="Python GUI Demo", font=("Arial", 14))
label.pack(pady=10)

clear_btn = tk.Button(root, text="Clear", command=clear_label)
clear_btn.pack(pady=5)

restore_btn = tk.Button(root, text="Restore", command=restore_label, state=tk.DISABLED)
restore_btn.pack(pady=5)

root.mainloop()