import FreeSimpleGUI as gui

label1 = gui.Text("Select Files to Compress:")
files_input = gui.Input()
choose_button_for_files_input = gui.FilesBrowse("Choose")

label2 = gui.Text("Select Destination Folder:")
folder_input = gui.Input()
choose_button_for_folder_input = gui.FolderBrowse("Choose")

compress_button = gui.Button("Compress")

window = gui.Window("File Compressor",
                    layout=[[label1, files_input, choose_button_for_files_input],
                            [label2, folder_input, choose_button_for_folder_input],
                            [compress_button]
                            ])
window.read()
window.close()