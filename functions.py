import streamlit as st


def get_todos(filename="todos.txt"):
    with open(r"files/"+filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename="todos.txt"):
    with open(r"files/"+filename, "w") as file_local:
        file_local.writelines(todos_arg)
