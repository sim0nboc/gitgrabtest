import tkinter as tk
from tkinter import ttk

msg = "Hello"

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

popup = tk.Tk()
popup.wm_title("!")
label = ttk.Label(popup, text=msg, font=NORM_FONT)
label.pack(side="top", fill="x", pady=10)
B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
B1.pack()
popup.mainloop()
