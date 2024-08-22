import FreeSimpleGUI as gui
import functions

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo") # tooltip is a message shown on hover
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window("My To-Do App", # This will be the title of the App.
                    layout=[[label], # row 1 on the window
                            [input_box, add_button], # row 2 on the window ...
                            [list_box, edit_button, complete_button],
                            [exit_button]], 
                    font=('Helvetica', 20)) 

# window.read()  # user action required to execute below this line.
# Alternatively
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        # In case it's an add event
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])
        
        case gui.WIN_CLOSED:
            break

window.close()