import streamlit as st
import sys
import inspect
from metrics.metrics import *
import metrics.metrics as metrics

funcs = dir(metrics)[8:]

def run_metrics(metric: str):
    if metric not in funcs:
        st.error('Invalid function name provided')
    
    function = metrics.__dict__[metric]
    args = inspect.getfullargspec(metrics.__dict__[metric]).args
    types = inspect.getfullargspec(metrics.__dict__[metric]).annotations

    if len(args) == 2:
        if str(types[args[0]]) == "<class 'int'>" and str(types[args[-1]]) == "<class 'int'>":
            first = st.number_input(f"Enter Value for {args[0]}: ")
            second = st.number_input(f"Enter Value for {args[-1]}: ")
            if second and first:
                calc = st.button('Calculate')
                if calc:
                    result = function(first, second)
                    st.write(f"The result for {metric} is {result}")

        elif str(types[args[0]]) == "<class 'list'>" and str(types[args[-1]]) == "<class 'int'>":
            n = int(st.number_input(f"Enter the number of items in {args[0]}"))
            items = []
            if n:
                for i in range():
                    item = st.number_input(f'Enter item {i+1}')
                    if item:
                        items.append(item)

            second = st.number_input(f"Enter Value for {args[-1]}: ")

            if items != [] and second:
                calc = st.button('Calculate')
                if calc:
                    result = function(items, second)
                    st.write(f"The result for {metric} is {result}")
        else:
            st.write('Done')
    else:
        values = {}
        for arg in args:
            if str(types[arg]) == "<class 'int'>":
                first_value = st.number_input(f"Enter value for {arg}")
                if first_value:
                    values[arg] = first_value
            else:
                n = int(st.number_input(f"Enter the number of items in {arg}"))
                second_value = []
                if n:
                    for i in range(n):
                        item = st.number_input(f'Enter item {i+1}')
                        if item:
                            second_value.append(item)
                            values[arg] = second_value

        if values != {}:
            calc = st.button('Calculate')
            if calc:
                result = function(**values)
                st.write(f"The result for {metric} is {result}")

title_alignment= """
<style>
#the-title {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

st.title('HELLO!!! YOU CAN TEST EACH OF THE METRICS ON THIS PAGE')

st.write(f"Please enter the metrics you want among these\n {' '.join(funcs)}\nChceck [Docs](https://king-tomi.github.io/metrics/references/) for further information on the functions")

metric = st.text_input('What Metric are you looking to measure: ')

if metric:
    start_button = st.button('Click Here to Test a Metric')
    if start_button:
        run_metrics(metric)