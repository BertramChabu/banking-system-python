import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()


input1 =  ttk.Entry(root, bootstyle="primary")
input2 = ttk.Entry(root, bootstyle="primary")
input1.pack()
input2.pack()
b1 = ttk.Button(root, text="Exit", bootstyle="primary-outline")
b2 = ttk.Button(root, text="Login", bootstyle="success-outline")
b1.pack(side=LEFT, padx=5, pady=10)
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
