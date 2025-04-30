import tkinter as tk
from tkinter import ttk
import sys
from toobj import *
import config

def create_blender(user_data):
    register_design(user_data)
    sys.argv = ["main_blender.py", user_data]
    with open("main_blender.py") as f:
        code = f.read()
        exec(code)
    

def generate_design(user_data):
    register_design(user_data)
    sys.argv = ["main_design.py", user_data]
    with open("main_design.py") as f:
        code = f.read()
        exec(code)
    
    
def register_design(user_data):
    """
    Retrieves the selected values from the GUI and stores them in the user_data dictionary.
    """
    user_data["button_side"] = user_data["button_side_widget"].get()
    user_data["button_vertical"] = user_data["button_vertical_widget"].get()
    user_data["camera_number"] = user_data["camera_number_widget"].get()
    user_data["camera_side"] = user_data["camera_side_widget"].get()

    print("User Preferences Registered:", user_data)  # Debugging output

def create_gui():
    """
    Creates the GUI and initializes all widgets.
    Returns the user_data dictionary with input fields and the main window.
    """
    window = tk.Tk()
    window.title("3D Smartphone")
    window.geometry("450x160")

    # Data storage
    user_data = {
        "button_side": "",
        "button_vertical": "",
        "camera_number": 0,
        "camera_side": "",
    }

    # Labels and dropbottoms
    tk.Label(window, text="Buttons Position").grid(row=0, column=0, pady=10)
    vertical_positions = ["top", "middle", "bottom"]
    side_positions = ["left", "right"]
    
    button_side_position = ttk.Combobox(window, values=side_positions)
    button_vertical_position = ttk.Combobox(window, values=vertical_positions)

    button_side_position.grid(row=0, column=1, padx=10, pady=10)
    button_vertical_position.grid(row=0, column=2, padx=10, pady=10)

    tk.Label(window, text="Number of Cameras").grid(row=1, column=0, padx=5, pady=5)
    camera_number = ttk.Combobox(window, values=['1', '2', '3'])

    tk.Label(window, text="Position of Cameras").grid(row=2, column=0)
    camera_side_position = ttk.Combobox(window, values=side_positions)
    
    camera_number.grid(row=1, column=1, padx=5, pady=5)
    camera_side_position.grid(row=2, column=1, padx=5, pady=5)

    # Store widgets inside user_data for easy access
    user_data["button_side_widget"] = button_side_position
    user_data["button_vertical_widget"] = button_vertical_position
    user_data["camera_number_widget"] = camera_number
    user_data["camera_side_widget"] = camera_side_position

    # Register Button
    register_button = tk.Button(
        window, text="Generate Design", command=lambda: (generate_design(user_data), window.destroy())
    )
    register_button.grid(row=3, column=1, padx=5, pady=15)
    
    create_blender_button = tk.Button(
        window, text="Create Blender Script",
        command=lambda: (create_blender(user_data), window.destroy())
    )
    create_blender_button.grid(row=3, column=2, padx=5, pady=15)

    return window, user_data  # Return the window and user_data for later use



# end of utils.py