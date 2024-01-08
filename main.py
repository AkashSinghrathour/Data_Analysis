# teclado channel
import numpy as np
from graph import creat_chart 
from data import read_data
user = """ please choose from the following option :

-> Enter 'c' to chart a new graph.
-> Enter 'q' to quite.
Your selection: """

Charting_new = " Enter the column you'd like to chart : "

file_prompt = "Enter your Desired file name: "

def handle_chart():
    
    column = int(input("chart_menu : "))
    # creat_chart(
        # [1,2,3,4,5,6],
        # [2.7,4.5,4,3.6,5,3.8]
    x=read_data(-1)
    y=[n for n in read_data(column)]
    file_name = input(file_prompt)
    creat_chart(x,y,file_name)
    # )
while True:
    user_selection = input(user)
    if user_selection =="c":
        handle_chart()
    elif user_selection == "q":
        break
    else:
        print(f"sorry, '{user_selection}' is not a valid option.")