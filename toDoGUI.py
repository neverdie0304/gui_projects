import FreeSimpleGUI as gui


label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo") # tooltip is a message shown on hover
add_button = gui.Button("Add")

window = gui.Window("My To-Do App", layout=[[label, input_box], [add_button]]) # This will be the title of the App. list inside list means a one row. layout=[[row1], [row2]]
window.read()  # user action required to execute below this line.
window.close()