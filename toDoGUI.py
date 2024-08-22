import FreeSimpleGUI as gui
import functions

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo") # tooltip is a message shown on hover
add_button = gui.Button("Add")

window = gui.Window("My To-Do App", # This will be the title of the App.
                    layout=[[label], [input_box, add_button]], # list inside list means a row. layout=[[row1], [row2]]
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
        
        case gui.WIN_CLOSED:
            break

window.close()