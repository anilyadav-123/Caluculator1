import tkinter as tk

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


root = tk.Tk()
root.title("Simple Calculator")


display = tk.Entry(root, font=('Arial', 20))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    if text != '=':
        button = tk.Button(root, text=text, font=('Arial', 20), command=lambda t=text: button_click(t))
        button.grid(row=row, column=column, padx=10, pady=10, ipadx=20, ipady=20)
    else:
        button = tk.Button(root, text=text, font=('Arial', 20), command=calculate)
        button.grid(row=row, column=column, padx=10, pady=10, ipadx=20, ipady=20)


clear_button = tk.Button(root, text='C', font=('Arial', 20), command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=20, ipady=20)


root.configure(bg='#f0f0f0')


root.mainloop()