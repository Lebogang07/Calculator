
from tkinter import * 


def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, current + str(number))

def btnAC():
    display.delete(0, END)

def btnBack():
    pos = display.index(END)
    if pos > 0:
        display.delete(pos-1)


def equal():
    expression = display.get()
    expression = expression.replace('x', '*')  
    try:
        result = eval(expression)
        display.delete(0, END)
        display.insert(0, result)
    except Exception:
        display.delete(0, END)
        display.insert(0, "Error")

def negate():
    value = display.get()
    value = float(0 - float(value))
    display.delete(0,END)
    display.insert(0, value)
    

window = Tk()

window.geometry("300x400")
window.title("Calculator")
window.configure(bg="black")

display = Entry(window, font=("Helvetica", 18), bg="black", fg="white", relief=SUNKEN)
display.grid(row=1, column=0, columnspan=4, pady=5, padx=10)

btnAC = Button(window, text="AC", width = 6, height = 3, command=btnAC, bg="lightgrey", font=("Helvetica", 10)).grid(row=2, column=0, pady=4, padx=1)
btn7 = Button(window, text="7", width=6, height = 3, command = lambda: button_click(7), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=3, column= 0, pady=4, padx=1)
btn4 = Button(window, text="4", width=6, height = 3, command = lambda: button_click(4), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=4, column= 0, pady=4, padx=1)
btn1 = Button(window, text="1", width=6, height = 3, command = lambda: button_click(1), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=5, column= 0, pady=4, padx=1)
btn0 = Button(window, text="0", width=12, height = 3, command = lambda: button_click(0), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=6, column= 0, pady=4, padx=1, columnspan=2)

btnBack = Button(window, text="<-", width = 6, height = 3, command = btnBack,  bg="lightgrey", font=("Helvetica", 10)).grid(row=2, column=1, pady=4, padx=1)
btn8 = Button(window, text="8", width=6, height = 3, command = lambda: button_click(8), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=3, column= 1, pady=4, padx=1)
btn5 = Button(window, text="5", width=6, height = 3, command = lambda: button_click(5), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=4, column= 1, pady=4, padx=1)
btn2 = Button(window, text="2", width=6, height = 3, command = lambda: button_click(2), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=5, column= 1, pady=4, padx=1)

btnPM = Button(window, text="+/-", width = 6, height = 3, command=negate,  bg="lightgrey", font=("Helvetica", 10)).grid(row=2, column=2, pady=4, padx=1)
btn9 = Button(window, text="9", width=6, height = 3, command = lambda: button_click(9), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=3, column= 2, pady=4, padx=1)
btn6 = Button(window, text="6", width=6, height = 3, command = lambda: button_click(6), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=4, column= 2, pady=4, padx=1)
btn3 = Button(window, text="3", width=6, height = 3, command = lambda: button_click(3), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=5, column= 2, pady=4, padx=1)
btnComma = Button(window, text=",", width=6, height = 3,  command=lambda: button_click('.'), bg="darkgrey", fg="white", font=("Helvetica", 10)).grid(row=6, column= 2, pady=4, padx=1)

btnDivide = Button(window, text="/", width = 6, height = 3, command=lambda: button_click('/'),  bg="orange", fg="white", font=("Helvetica", 10)).grid(row=2, column=3, pady=4, padx=1)
btnMultiply = Button(window, text="x", width=6, height = 3,  command=lambda: button_click('x'), bg="orange", fg="white", font=("Helvetica", 10)).grid(row=3, column= 3, pady=4, padx=1)
btnMinus = Button(window, text="-", width=6, height = 3,  command=lambda: button_click('-'), bg="orange", fg="white", font=("Helvetica", 10)).grid(row=4, column= 3, pady=4, padx=1)
btnAdd = Button(window, text="+", width=6, height = 3,  command=lambda: button_click('+'), bg="orange", fg="white", font=("Helvetica", 10)).grid(row=5, column= 3, pady=4, padx=1)
btnEqual = Button(window, text="=", width=6, height = 3,  command=equal, bg="orange", fg="white", font=("Helvetica", 10)).grid(row=6, column= 3, pady=4, padx=1)



window.mainloop()
