import tkinter
from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("470x500+100+200")
window.resizable(False,False)
window.configure(background="#17161b")

equation =""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation= ""

    label_result.config(text=result)
    
label_result = Label(window,width=22, height=2, text="",background="#17161b", foreground="#fff", font=("Helvetica", 30))
label_result.pack()




Button(window, text="C",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#2d78db",command=lambda:clear()).place(x=10, y=100)
Button(window, text="(",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#3f525a",command =lambda: show("(")).place(x=125, y=100)
Button(window, text=")",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#3f525a",command =lambda: show(")")).place(x=240, y=100)
Button(window, text="/",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#3f525a",command =lambda: show("/")).place(x=355, y=100)

Button(window, text="7",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("7")).place(x=10, y=180)
Button(window, text="8",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("8")).place(x=125, y=180)
Button(window, text="9",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("9")).place(x=240, y=180)
Button(window, text="*",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#3f525a",command =lambda: show("*")).place(x=355, y=180)

Button(window, text="4",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("4")).place(x=10, y=260)
Button(window, text="5",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("5")).place(x=125, y=260)
Button(window, text="6",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("6")).place(x=240, y=260)
Button(window, text="-",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#3f525a",command =lambda: show("-")).place(x=355, y=260)

Button(window, text="1",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("1")).place(x=10, y=340)
Button(window, text="2",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("2")).place(x=125, y=340)
Button(window, text="3",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("3")).place(x=240, y=340)
Button(window, text="+",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#3f525a",command =lambda: show("+")).place(x=355, y=340)

Button(window, text="%",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("%")).place(x=10, y=420)
Button(window, text="0",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show("0")).place(x=125, y=420)
Button(window, text=".",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#202d36",command =lambda: show(".")).place(x=240, y=420)
Button(window, text="=",width=5, height =1, font=("Helvetica",25,""),  foreground="#ffffff", background="#e97311",command =lambda: calculate()).place(x=355, y=420)
window.mainloop()
