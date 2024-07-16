import tkinter
from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("470x500+100+200")
window.resizable(False,False)
window.configure(background="#17161b")

label_result = Label(window,width=25, height=2, text="", font=("Arial", 30))
label_result.pack()



window.mainloop()
