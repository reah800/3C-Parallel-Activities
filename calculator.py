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

top_frame = tk.Frame(root, bg="#ffffff")
top_frame.pack(pady=5)



tk.Button(top_frame, text ="⌫", width=6, height=2,
          bg="#f4a6a6", fg="white", font=("Arial", 14),
          command= erase).grid(row=0, column=1, padx=5)
