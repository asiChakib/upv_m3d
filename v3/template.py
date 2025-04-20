import bpy
import math

# functions to create shapes

def create_phone_model():
    corner_segments = 8
    radius = 0.8
    width, height, thickness = 15.6, 7.6, 1.0
    
    verts = []
    
    for i in range(36):
        if i < 9:
            angle = math.pi + (i*math.pi/2) / (corner_segments)
            x = -7 + radius * math.cos(angle)
            y = -3 + radius * math.sin(angle)
        elif i < 18:
            angle = 3 * math.pi/2 + (i-9) * math.pi/2 / (corner_segments)
            x = 7 + radius * math.cos(angle)
            y = -3 + radius * math.sin(angle)
        elif i < 27:
            angle = 0 + (i-18) * math.pi/2 / (corner_segments)
            x = 7 + radius * math.cos(angle)
            y = 3 + radius * math.sin(angle)
        else:
            angle = math.pi/2 + (i-27) * math.pi/2 / (corner_segments)
            x = -7 + radius * math.cos(angle)
            y = 3 + radius * math.sin(angle)
            
        verts.append((x, y, -0.5))
        verts.append((x, y, 0.5))
        
    faces = []
    bottom_face = [i*2 for i in range(36)]
    faces.append(bottom_face)
    top_face = [i*2+1 for i in range(36)]
    top_face.reverse()
    faces.append(top_face)
    
    for i in range(36):
        next_i = (i+1) % 36
        faces.append([i*2, next_i*2, next_i*2+1, i*2+1])
        
    return verts, faces 
        
def create_camera(name, position):
    radius = 0.5
    height = 0.2
    vertices = 32
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=height)
    camera = bpy.context.object
    camera.name = name
    camera = bpy.data.objects.get(name)
    camera.location = position
    bpy.ops.object.transform_apply(location=True)
    
def create_button(name, dimensions, position):
    bpy.ops.mesh.primitive_cube_add()
    button1 = bpy.context.object
    button1.name = name
    button1 = bpy.data.objects.get(name)
    button1.scale = dimensions
    button1.location = position
    bpy.ops.object.transform_apply(location=True, scale=True)

# here the scripts starts

cam_side = {{ CAM_SIDE }}
but_dim = {{ BUT_DIM }}
button = {{ BUTTON }}

# create cameras
i = 1
for p in cam_side:
    create_camera("PCamera"+str(i+1), p)
    i += 1
    
# create buttons
create_button("button+", but_dim, button)
button = (button[0]-1.2, button[1], button[2])
create_button("button-", but_dim, button)

# create phone base

mesh = bpy.data.meshes.new("PhoneBase")
obj = bpy.data.objects.new("PhoneBase", mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

verts, faces = create_phone_model()
mesh.from_pydata(verts, [], faces)
