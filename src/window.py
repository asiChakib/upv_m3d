import tkinter as tk
from tkinter import ttk

def register_design():
    global button_side_selected, button_vertical_selected, camera_number_selected, camera_side_selected
    
    button_side_selected = button_side_position.get()
    button_vertical_selected = button_vertical_position.get()
    camera_number_selected = camera_number.get()
    camera_side_selected = camera_side_position.get()

    choices.clear()
    choices.extend([button_side_selected, button_vertical_selected,
            camera_number_selected, camera_side_selected])



window = tk.Tk()
window.title("3d smatphone")
window.geometry("600x800")

# user input
# button_side_selected = ""
# button_vertical_selected = ""
# camera_number_selected = 0
# camera_side_selected = ""
# camera_vertical_selected = ""


label = tk.Label(window, text="buttons position")
vertical_positions = ["up", "middle", "bottom"]
side_positions = ["left", "right"]
button_side_position = ttk.Combobox(window, values=side_positions)
button_vertical_position = ttk.Combobox(window, values=vertical_positions)

label.grid(row=0, column=0, pady=10)
button_side_position.grid(row=0, column=1, padx=10, pady=10)
button_vertical_position.grid(row=0, column=2, padx=10, pady=10)

#=============================================

label2 = tk.Label(window, text="Number of cameras")
camera_number = tk.Spinbox(window, from_=0, to=100, increment=1, width=10)

label3 = tk.Label(window, text="position of cameras")
camera_side_position = ttk.Combobox(window, values=side_positions)

label2.grid(row=1, column=0, padx=5, pady=5)
camera_number.grid(row=1, column=1, padx=5, pady=5)

label3.grid(row=2, column=0)
camera_side_position.grid(row=2, column=1, padx=5, pady=5)

#=============================================
choices = []
register_button = tk.Button(window, text="register design", command=register_design)

register_button.grid(row=3, column=1, padx=5, pady=15)

#=============================================


window.mainloop()

