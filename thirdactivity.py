import tkinter as tk
from tkinter import ttk
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# (Task Parallelism)
def compute_sss(salary): return salary * 0.045
def compute_philhealth(salary): return salary * 0.025
def compute_pagibig(salary): return salary * 0.02
def compute_tax(salary): return salary * 0.10

# (Data Parallelism)
employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

# Payroll computation function
def compute_payroll(employee):
    name, salary = employee
    sss = compute_sss(salary)
    philhealth = compute_philhealth(salary)
    pagibig = compute_pagibig(salary)
    tax = compute_tax(salary)
    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction
    return (name, salary, total_deduction, net_salary)

# GUI Functions
def run_task_parallelism():
    # Example: run for Alice(Task Parallelism)
    name, salary = employees[0]  
    tasks = [compute_sss, compute_philhealth, compute_pagibig, compute_tax]
    results = []
    output_text.delete("1.0", tk.END) 

    output_text.insert(tk.END, f"Task Parallelism for {name} (Salary: {salary:.2f})\n\n")

    with ThreadPoolExecutor() as executor:
        future_to_task = {executor.submit(task, salary): task.__name__ for task in tasks}
        for future in as_completed(future_to_task):
            deduction = future.result()
            results.append(deduction)
            output_text.insert(tk.END, f"{future_to_task[future]}: {deduction:.2f}\n")

    total_deduction = sum(results)
    net_salary = salary - total_deduction

    output_text.insert(tk.END, f"\nTotal Deduction for {name}: {total_deduction:.2f}\n")
    output_text.insert(tk.END, f"Net Salary for {name}: {net_salary:.2f}\n")


def run_data_parallelism():
    output_text.delete("1.0", tk.END)  

    
    for row in tree.get_children():
        tree.delete(row)

    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

    for name, gross, deduction, net in results:
        
        tree.insert("", tk.END, values=(name, f"{gross:.2f}", f"{deduction:.2f}", f"{net:.2f}"))