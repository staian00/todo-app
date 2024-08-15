import functions
import FreeSimpleGUI as Sg

todos = []

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter a todo", key="todo", size=(51, 1))
add_button = Sg.Button("Add", size=(8, 1))
edit_button = Sg.Button("Edit", size=(8, 1))
complete_button = Sg.Button("Complete", size=(8, 1))
todos_list = Sg.Listbox(values=functions.get_todos(), size=(50, 10), key='TODOS', enable_events=True)
column = Sg.Column([[edit_button], [complete_button]])

window = Sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [todos_list, column],
                           ],
                   font=("Helvetica", 15))

while True:
    event, dic = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = dic["todo"].strip().title() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["TODOS"].update(todos)
            input_box("")

        case "Edit":
            todo_to_edit = dic["TODOS"][0]
            new_todo = dic["todo"].strip().title() + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["TODOS"].update(todos)
        case "Complete":
            try:
                todo_to_complete = dic["TODOS"][0]
                new_todo = dic["todo"].strip().title() + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                del todos[index]
                functions.write_todos(todos)
                window["TODOS"].update(todos)
            except IndexError:
                continue
        case "TODOS":
            try:
                todo_to_show = dic["TODOS"][0].strip()
                input_box(f"{todo_to_show}")
            except IndexError:
                continue

        case Sg.WIN_CLOSED:
            break

window.close()