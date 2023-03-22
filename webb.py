import streamlit as sl
import defs

todos = defs.reading()

def what_todo():
    if sl.session_state['new_todo']:
        todo = sl.session_state['new_todo']
        todos.append(todo+"\n")
        defs.writing(todos)
        sl.session_state['new_todo'] = ""



sl.title("ToDo App")
sl.subheader("This app creates a personalized to-do list")
sl.write("Let's start")

for index, todo in enumerate(todos):
    print(index, todo)
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        defs.writing(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

sl.text_input("", placeholder="enter a to-do",
              on_change= what_todo, key="new_todo")

