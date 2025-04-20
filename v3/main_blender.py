
import config
from pathlib import Path
import sys

user_data = sys.argv[1]

for x in user_data.values():
    if x == '':
        exit()
        

buttons_position_v = user_data['button_side']
buttons_position_h = user_data['button_vertical']
camera_number = int(user_data['camera_number'])
camera_side = user_data['camera_side']

buttons_position = (buttons_position_v, buttons_position_h)
button = config.button_side_linker[buttons_position]
but_dim = (0.5, 0.15, 0.15)
cam_side = config.camera_R if camera_side == 'right' else config.camera_L

if camera_number == 2:
    del cam_side[1]
else : 
    pass

template_path = Path("./template.py")
with open(template_path, "r") as file:
    template_content = file.read()
    
final_script = (
    template_content
    .replace("{{ CAM_SIDE }}", str(cam_side))
    .replace("{{ BUT_DIM }}", str(but_dim))
    .replace("{{ BUTTON }}", str(button))
)

output_path = Path("final_bscript.py")
with open(output_path, "w") as file:
    file.write(final_script)
    
print("blender script generated successfully!")