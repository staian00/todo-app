import functions

while True:
    user_action = input("Enter add, show, edit, complete or exit\n")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for i, item in enumerate(todos):
            item = item.title().strip()
            print(f"{i+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            i = int(user_action[5:]) - 1
            print("Do you want to edit: " + str(todos[i]).capitalize()+"?")
            q = input("Yes or No: ").strip().capitalize()

            match q:
                case "Yes":
                    new_todo = input("Input a new todo: ") + "\n"
                    todos[i] = new_todo

                    functions.write_todos(todos_arg=todos)
                case "No":
                    print("Okay")
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no such task")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            i = int(user_action[9:]) - 1
            print("Do you want to compete: " + str(todos[i]).capitalize() + "?")
            q = input("Yes or No: ").strip().capitalize()

            match q:
                case "Yes":
                    del todos[i]
                    functions.write_todos(filename="todos.txt", todos_arg=todos)

                case "No":
                    print("Okay")

        except IndexError:
            print("There is no such task")
            continue

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Dude, WTF")
