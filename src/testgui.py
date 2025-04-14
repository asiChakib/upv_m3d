import tkinter as tk
from tkinter import ttk

# Variables to store user selections
button_side_selected = ""
button_vertical_selected = ""
camera_number_selected = 0
camera_side_selected = ""
camera_vertical_selected = ""

# Function to update and store values
def save_values():
    global button_side_selected, button_vertical_selected, camera_number_selected
    global camera_side_selected, camera_vertical_selected

    button_side_selected = button_side_position.get()
    button_vertical_selected = button_vertical_position.get()
    camera_number_selected = camera_number.get()
    camera_side_selected = camera_side_position.get()
    camera_vertical_selected = camera_vertical_position.get()

    # Print values for testing
    print("Saved values:")
    print(f"Button position: {button_side_selected} {button_vertical_selected}")
    print(f"Camera: {camera_number_selected} cameras at {camera_side_selected} {camera_vertical_selected}")

window = tk.Tk()
window.title("3d smartphone")
window.geometry("800x800")

label = tk.Label(window, text="buttons position")
vertical_positions = ["up", "middle", "down"]
side_positions = ["left", "right"]
button_side_position = ttk.Combobox(window, values=side_positions)
button_vertical_position = ttk.Combobox(window, values=vertical_positions)

label.grid(row=0, column=0, pady=10)
button_side_position.grid(row=0, column=1, padx=10, pady=10)
button_vertical_position.grid(row=0, column=2, padx=10, pady=10)

#=============================================

label2 = tk.Label(window, text="Number of cameras")
camera_number = tk.Spinbox(window, from_=0, to=100, increment=1, width=10)
camera_vertical_position = ttk.Combobox(window, values=vertical_positions)
camera_side_position = ttk.Combobox(window, values=side_positions)

label2.grid(row=1, column=0, padx=5, pady=5)
camera_number.grid(row=1, column=1, padx=5, pady=5)
camera_side_position.grid(row=1, column=2, padx=5, pady=5)
camera_vertical_position.grid(row=1, column=3, padx=5, pady=5)

#=============================================

# Add a save button to capture values
save_button = tk.Button(window, text="Save Selections", command=save_values)
save_button.grid(row=2, column=0, columnspan=2, pady=20)

# Function to run when window closes
def on_closing():
    save_values()  # Save values before closing
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)  # Capture window close event

window.mainloop()

print(camera_side_selected)