from utils import create_gui
from toobj import create_rounded_prism, create_rectangular_prism, create_cylinder, save_obj
import config
import sys

user_data = sys.argv[1]


print(user_data['button_side'])

for x in user_data.values():
    if x == '':
        exit()


buttons_position_v = user_data['button_side']
buttons_position_h = user_data['button_vertical']
camera_number = int(user_data['camera_number'])
camera_side = user_data['camera_side']

buttons_position = (buttons_position_v, buttons_position_h)



def create_model(buttons_position, camera_side, camera_number):
    # Main rectangular prism with curved edges (14x6x1)
    main_prism_vertices, main_prism_faces = create_rounded_prism(
        width=14.0, 
        height=6.0, 
        depth=1.0, 
        position=(0, 0, 0), 
        rotation=(0, 0, 0),
        curve_radius=0.8  # Adjust this value to control the roundness
    )

    tn1w = config.button_side_linker[buttons_position]
    
    # Get user input for tiny prisms
    
    tiny1_width = 0.8
    tiny1_height = 0.2
    tiny1_depth = 0.15
    tiny1_x = tn1w[0]
    tiny1_y = tn1w[1]
    tiny1_z = tn1w[2]
    

    tiny2_width = tiny1_width
    tiny2_height = tiny1_height
    tiny2_depth = tiny1_depth
    tiny2_x = tiny1_x - 1.0
    tiny2_y = tiny1_y 
    tiny2_z = tiny1_z
    
    # Get user input for cylinder
    
    cyl_radius = 0.5
    cyl_height = 0.2
    
    
    # Create buttons
    tiny_prism1_vertices, tiny_prism1_faces = create_rectangular_prism(
        width=tiny1_width, 
        height=tiny1_height, 
        depth=tiny1_depth, 
        position=(tiny1_x, tiny1_y, tiny1_z)
    )
    
    tiny_prism2_vertices, tiny_prism2_faces = create_rectangular_prism(
        width=tiny2_width, 
        height=tiny2_height, 
        depth=tiny2_depth, 
        position=(tiny2_x, tiny2_y, tiny2_z)
    )
    

    all_vertices = [main_prism_vertices, tiny_prism1_vertices, tiny_prism2_vertices]
    all_faces = [main_prism_faces, tiny_prism1_faces, tiny_prism2_faces]

    # Create cameras
    cam_side = config.camera_R if camera_side == 'right' else config.camera_L

    for i in range(camera_number):
        if camera_number == 2:
            cylinder_vertices, cylinder_faces = create_cylinder(
                radius=cyl_radius,
                height=cyl_height,
                position=cam_side[i+1]
            )
            all_vertices.append(cylinder_vertices)
            all_faces.append(cylinder_faces)

        else: 
            cylinder_vertices, cylinder_faces = create_cylinder(
                radius=cyl_radius,
                height=cyl_height,
                position=cam_side[i]
            )
            all_vertices.append(cylinder_vertices)
            all_faces.append(cylinder_faces)
    
    
    
    # Save to OBJ file
    save_obj("./shapes.obj", all_vertices, all_faces)
    
    

create_model(buttons_position, camera_side, camera_number)
