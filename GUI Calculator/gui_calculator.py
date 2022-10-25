from cgitb import text
import tkinter as tk


calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0 , "end")    #text_result is the calculator screen. So, we refresh it with values on clicking of each button
    text_result.insert(1.0,calculation) 

def evaluate_calculation():
    global calculation
    try:
        if calculation == "":
            text_result.delete(1.0 , "end")
            text_result.insert(1.0,"Please Enter Value")
        else:
            calculation = str(eval(calculation))
            text_result.delete(1.0 , "end")
            text_result.insert(1.0,calculation) 
    except:
        text_result.delete(1.0,"end")
        text_result.insert(1.0,"ERROR")

def clear_screen():
    text_result.delete(1.0,"end")
    global calculation
    calculation = ""

root = tk.Tk()

root.geometry("350x400")
root.title("Calculator")

# label=tk.Label(root,text="Hello World!!",font=("Arial",12))
# label.pack(padx=10,pady=10)

text_result=tk.Text(root, height=3,font=("Arial",16))
text_result.pack(padx=10, fill='x')

# myentry=tk.Entry(root)
# myentry.pack()

# button=tk.Button(root, text="Click Me!",font=("Arial",10))
# button.pack(pady=5)

#buttonframe will be layed out using pack. The buttons will be layed out in grid
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)

btn1= tk.Button(buttonframe, text="1", command=lambda:add_to_calculation(1), font=('Arial',12))
btn1.grid(row=0, column=0, sticky="we")

btn2= tk.Button(buttonframe, text="2", command=lambda:add_to_calculation(2), font=('Arial',12))
btn2.grid(row=0, column=1, sticky="we")

btn3= tk.Button(buttonframe, text="3", command=lambda:add_to_calculation(3), font=('Arial',12))
btn3.grid(row=0, column=2, sticky="we")

btn_plus= tk.Button(buttonframe, text="+", command=lambda:add_to_calculation('+'), font=('Arial',12))
btn_plus.grid(row=0, column=3, sticky="we")

btn4= tk.Button(buttonframe, text="4", command=lambda:add_to_calculation(4), font=('Arial',12))
btn4.grid(row=1, column=0, sticky="we")

btn5= tk.Button(buttonframe, text="5", command=lambda:add_to_calculation(5), font=('Arial',12))
btn5.grid(row=1, column=1, sticky="we")

btn6= tk.Button(buttonframe, text="6", command=lambda:add_to_calculation(6), font=('Arial',12))
btn6.grid(row=1, column=2, sticky="we")

btn_minus= tk.Button(buttonframe, text="-", command=lambda:add_to_calculation('-'), font=('Arial',12))
btn_minus.grid(row=1, column=3, sticky="we")

btn7= tk.Button(buttonframe, text="7", command=lambda:add_to_calculation(7), font=('Arial',12))
btn7.grid(row=2, column=0, sticky="we")

btn8= tk.Button(buttonframe, text="8", command=lambda:add_to_calculation(8), font=('Arial',12))
btn8.grid(row=2, column=1, sticky="we")

btn9= tk.Button(buttonframe, text="9", command=lambda:add_to_calculation(9), font=('Arial',12))
btn9.grid(row=2, column=2, sticky="we")

btn_multiply= tk.Button(buttonframe, text="*", command=lambda:add_to_calculation('*'), font=('Arial',12))
btn_multiply.grid(row=2, column=3, sticky="we")

btn_openbrckt= tk.Button(buttonframe, text="(", command=lambda:add_to_calculation('('), font=('Arial',12))
btn_openbrckt.grid(row=3, column=0, sticky="we")

btn0= tk.Button(buttonframe, text="0", command=lambda:add_to_calculation(0), font=('Arial',12))
btn0.grid(row=3, column=1, sticky="we")

btn_closebrckt= tk.Button(buttonframe, text=")", command=lambda:add_to_calculation(')'), font=('Arial',12))
btn_closebrckt.grid(row=3, column=2, sticky="we")

btn_divide= tk.Button(buttonframe, text="/", command=lambda:add_to_calculation('/'), font=('Arial',12))
btn_divide.grid(row=3, column=3, sticky="we")

btn_clear= tk.Button(buttonframe, text="C", command=lambda:clear_screen(), font=('Arial',12))
btn_clear.grid(row=4, columnspan=2, sticky="we")

btn_equal= tk.Button(buttonframe, text="=", command=lambda:evaluate_calculation(), font=('Arial',12))
btn_equal.grid(row=4, column=2, columnspan=2, sticky="we")

buttonframe.pack(fill='x', padx=10)
root.mainloop()