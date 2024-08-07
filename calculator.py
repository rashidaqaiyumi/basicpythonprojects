import tkinter as tk

calculation = ""
#defining function
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
#eval functiion(evaluates calculations and python code)
def evaluate_calculation():
    global calculation
    
    try:
        
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")    

def clear_field():
    global calculation
    calculation = ""



root = tk.Tk()
#size
root.geometry('300x275')
text_result = tk.Text(root, height=2, width=16, font=("arial", 24))
text_result.grid(columnspan=6)

button_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5 , font="arial")
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5 , font="arial")
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5 , font="arial")
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5 , font="arial")
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5 , font="arial")
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5 , font="arial")
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5 , font="arial")
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5 , font="arial")
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5 , font="arial")
button_9.grid(row=4, column=3)
button_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5 , font="arial")
button_0.grid(row=5, column=2)
button_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5 , font="arial")
button_plus.grid(row=2, column=4)
button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5 , font="arial")
button_minus.grid(row=3, column=4)
button_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5 , font="arial")
button_mul.grid(row=4, column=4)
button_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5 , font="arial")
button_div.grid(row=5, column=4)
button_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5 , font="arial")
button_open.grid(row=5, column=1)
button_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5 , font="arial")
button_close.grid(row=5, column=3)
button_clear = tk.Button(root, text="C", command=lambda: clear_field, width=5 , font="arial")
button_clear.grid(row=6, column=1, columnspan=2)
button_equals = tk.Button(root, text="=", command= evaluate_calculation, width=11 , font="arial")
button_equals.grid(row=6, column=3, columnspan=2)

root.mainloop()

