import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import sys
import inspect
from metrics.metrics import *
import metrics.metrics as metrics

funcs = dir(metrics)[8:]

def run_metrics():
    metric_name = metric_entry.get()

    if metric_name not in funcs:
        messagebox.showerror('Invalid function name provided')
        return

    function = metrics.__dict__[metric_name]
    args = inspect.getfullargspec(function).args
    types = inspect.getfullargspec(function).annotations

    values = {}
    input_widgets = []

    for arg in args:
        if arg == 'metric_name':
            continue

        label = tk.Label(text=f"Enter value for {arg}:")
        label.pack()
        # input_widgets.append(label)

        if str(types[arg]) == "<class 'int'>":
            entry = tk.Entry()
            entry.pack()
            input_widgets.append(entry)
        elif str(types[arg]) == "<class 'list'>":
            text = tk.Text()
            text.place(x = 20, y = 20, height = 25, width = 25)
            text.pack()
            input_widgets.append(text)
        else:
            messagebox.showerror('Invalid argument type')
            return

    def calculate_metrics():
        values = {}
        index = 0

        for arg in args:
            if arg == 'metric_name':
                continue

            if str(types[arg]) == "<class 'int'>":
                values[arg] = int(input_widgets[index].get())
                index += 1
            elif str(types[arg]) == "<class 'list'>":
                items = input_widgets[index].get("1.0", tk.END).strip().split('\n')
                values[arg] = [int(x) for x in items]
                index += 1

        result = function(**values)

        result_label = tk.Label(text=f"The result for {metric_name} is {result}")
        result_label.pack()
        #messagebox.showinfo(f"The result for {metric_name} is {result}")

    calculate_button = tk.Button(text="Calculate", command=calculate_metrics)
    calculate_button.pack()

root = tk.Tk()

welcome = tk.Label(text='HELLO!!! YOU CAN TEST EACH OF THE METRICS ON THIS PAGE')
welcome.pack()

metric_entry = tk.Entry()
metric_entry.pack()

start_button = tk.Button(
    text='Test a Metric',
    width=5,
    height=5,
    bg='blue',
    command=run_metrics
)
start_button.pack()

root.mainloop()
