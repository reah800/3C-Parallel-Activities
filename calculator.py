import tkinter as tk

def press(key):
    global expression
    expression += str(key)

display_var.set(expression)

def clear():
    global expression
    expression= "" display_var.set("")

    def erase():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""


root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")
root.configure(bg="#ffffff")
root.resizable(False, False)

expression = ""
display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 24),
    bg="pink",
    fg="white",
    bd=10,
    justify="right"
)
display.pack(fill="x", padx=10, pady=10)

#Top Buttons
top_frame = tk.Frame(root, bg="#ffffff")
top_frame.pack(pady=5)


tk.Button(top_frame, text ="⌫", width=6, height=2,
          bg="#f4a6a6", fg="white", font=("Arial", 14),
          command= erase).grid(row=0, column=1, padx=5)

#Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

frame = tk.Frame(root, bg="#e7c1e1")
frame.pack()

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, bg="#f4a6a6", fg="black",
                        font=("Arial", 16), width=5, height=2,
                        command=calculate)
    else:
        btn = tk.Button(frame, text=text, bg="#2a2a2a", fg="pink",
                        font=("Arial", 16), width=5, height=2,
                        command=lambda t=text: press(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", bg="red", fg="white",
                      font=("Arial", 14), command=clear)
clear_btn.pack(fill="x", padx=10, pady=5)
