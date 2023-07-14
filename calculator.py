import tkinter as tk
# Create Functions
def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current + str(number))

def button_clear():
    entry_field.delete(0, tk.END)

def button_equal():
    expression = entry_field.get()
    try:
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create Input Field
entry_field = tk.Entry(window, width=20, justify="right", font=("Arial", 12))
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create Number Buttons
button_1 = tk.Button(window, text="1", width=5,
                     command=lambda: button_click(1))
button_1.grid(row=1, column=0)

button_2 = tk.Button(window, text="2", width=5,
                     command=lambda: button_click(2))
button_2.grid(row=1, column=1)

button_3 = tk.Button(window, text="3", width=5,
                     command=lambda: button_click(3))
button_3.grid(row=1, column=2)

button_4 = tk.Button(window, text="4", width=5,
                     command=lambda: button_click(4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(window, text="5", width=5,
                     command=lambda: button_click(5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(window, text="6", width=5,
                     command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_7 = tk.Button(window, text="7", width=5,
                     command=lambda: button_click(7))
button_7.grid(row=3, column=0)

button_8 = tk.Button(window, text="8", width=5,
                     command=lambda: button_click(8))
button_8.grid(row=3, column=1)

button_9 = tk.Button(window, text="9", width=5,
                     command=lambda: button_click(9))
button_9.grid(row=3, column=2)

button_0 = tk.Button(window, text="0", width=5,
                     command=lambda: button_click(0))
button_0.grid(row=4, column=1)


# Create operator buttons (+ , - , * , /)
button_plus = tk.Button(window, text="+", width=5,
                        command=lambda: button_click("+"))
button_plus.grid(row=1, column=3)

button_minus = tk.Button(window, text="-", width=5,
                         command=lambda: button_click("-"))
button_minus.grid(row=2, column=3)

button_multiply = tk.Button(
    window, text="*", width=5, command=lambda: button_click("*"))
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(window, text="/", width=5,
                          command=lambda: button_click("/"))
button_divide.grid(row=4, column=3)


button_clear = tk.Button(window, text="C", width=5, command=button_clear)
button_clear.grid(row=5, column=0)

button_equal = tk.Button(window, text="=", width=5, command=button_equal)
button_equal.grid(row=5, column=3)


window.mainloop()
