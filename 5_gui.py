import tkinter as tk

win = tk.Tk()

win.title("IFA let's GO")

label1 = tk.Label(win, text = "Hello JH")
label1.pack()

button1 = tk.Button(win, text = "Keep Going")
button1.pack()

win.mainloop()