import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import sys
import inspect
from metrics.metrics import *
import metrics.metrics as metrics

funcs = dir(metrics)[8:]

def run_metrics():
    label = tk.Label(text=f"Please enter the metrics you want among these\n {' '.join(funcs)}\nChceck [Docs](https://king-tomi.github.io/metrics/references/) for further information on the functions")
    metric = tk.Entry()

    label.pack()
    metric.pack()
    
    metric = metric.get()


    if metric not in funcs:
        messagebox.showerror('Invalid function name provided')
    
    function = metrics.__dict__[metric]
    args = inspect.getfullargspec(metrics.__dict__[metric]).args
    types = inspect.getfullargspec(metrics.__dict__[metric]).annotations

    if len(args) == 2:
        if str(types[args[0]]) == "<class 'int'>" and str(types[args[-1]]) == "<class 'int'>":
            first_label = tk.label(f"Enter Value for {args[0]}")
            first = tk.Entry()
            first = int(first.get())

            second_label = tk.label(f"Enter Value for {args[0]}")
            second_t = tk.Entry()
            second = int(second_t.get())
            result = function(first, second)
            messagebox.showinfo(f"The result for {metric} is {result}")

            first_label.pack()
            first.pack()
            second_label.pack()
            second_t.pack()

        elif str(types[args[0]]) == "<class 'list'>" and str(types[args[-1]]) == "<class 'int'>":
            items_l = tk.Label(f"Enter the all the items in {args[0]} line by line")
            items_t = tk.Text()
            items = items_t.get("1.0", tk.END)
            items = [int(x) for x in items.aplit("\n")]
                

            second_l = tk.Label(f"Enter Value for {args[-1]}: ")
            second_t = tk.Entry()
            second = int(second_t.get())

            result = function(items, second)
            messagebox.showinfo(f"The result for {metric} is {result}")


            items_l.pack()
            items_t.pack()
            second_l.pack()
            second_t.pack()
        else:
            messagebox.showinfo('Done')
    else:
        values = {}
        for arg in args:
            if str(types[arg]) == "<class 'int'>":
                first_l = tk.Label(f"Enter value for {arg}")
                first_t = tk.Entry()
                first_value = first_t.get()
                values[arg] = first_value

                first_l.pack()
                first_t.pack()
            else:
                seconds_l = tk.Label(f"Enter the all the items in {arg} line by line")
                seconds_t = tk.Text()
                items = seconds_t.get("1.0", tk.END)
                second_value = [int(x) for x in items.aplit("\n")]
                values[arg] = second_value

                seconds_l.pack()
                seconds_t.pack()

        if values != {}:
            result = function(**values)
            messagebox.showinfo(f"The result for {metric} is {result}")

def main():
    window = tk.Tk()

    welcome = tk.Label(text='HELLO!!! YOU CAN TEST EACH OF THE METRICS ON THIS PAGE')
    welcome.pack()

    start = tk.Button(
        text='Test a Metric',
        width=5,
        height=5,
        bg='blue',
        command=run_metrics
    )
    start.pack()
    run_metrics()

    window.mainloop()

if __name__ == '__main__':
    main()