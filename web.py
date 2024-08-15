import streamlit as st
import functions as fc

todos = fc.get_todos()


def add_todo():
    todo = st.session_state['new_todo'].strip().title() + "\n"
    todos.append(todo)
    fc.write_todos(todos)


st.title("My Todo App")


for index, _name in enumerate(todos):
    checkbox = st.checkbox(_name, key=_name)
    if checkbox:
        del todos[index]
        fc.write_todos(todos)
        del st.session_state[_name]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
