import numpy as np
import math

def create_rounded_prism(width, height, depth, position=(0, 0, 0), rotation=(0, 0, 0), curve_radius=0.5):
    """
    Generate a rectangular prism with curved edges to resemble a phone
    
    Args:
    width: Width along x-axis
    height: Height along y-axis
    depth: Depth along z-axis
    position: (x, y, z) position of the center of the prism
    rotation: (rx, ry, rz) rotation in degrees around each axis
    curve_radius: Radius of the curved edges
    
    Returns:
    vertices, faces for OBJ format
    """
    # Limit curve radius to prevent issues
    curve_radius = min(curve_radius, min(width, height) / 4)
    
    # Calculate dimensions accounting for curved edges
    inner_width = width - 2 * curve_radius
    inner_height = height - 2 * curve_radius
    
    # Number of segments for curved edges
    segments = 8  # Number of segments per corner
    
    # Generate vertices
    vertices = []
    
    # Create front face (z = -depth/2)
    # Bottom-left corner
    for i in range(segments + 1):
        angle = math.pi + (i * math.pi / 2) / segments
        x = -inner_width/2 - curve_radius + curve_radius * math.cos(angle)
        y = -inner_height/2 - curve_radius + curve_radius * math.sin(angle)
        vertices.append((x, y, -depth/2))
    
    # Bottom-right corner
    for i in range(segments + 1):
        angle = 3 * math.pi / 2 + (i * math.pi / 2) / segments
        x = inner_width/2 + curve_radius + curve_radius * math.cos(angle)
        y = -inner_height/2 - curve_radius + curve_radius * math.sin(angle)
        vertices.append((x, y, -depth/2))
    
    # Top-right corner
    for i in range(segments + 1):
        angle = 0 + (i * math.pi / 2) / segments
        x = inner_width/2 + curve_radius + curve_radius * math.cos(angle)
        y = inner_height/2 + curve_radius + curve_radius * math.sin(angle)
        vertices.append((x, y, -depth/2))
    
    # Top-left corner
    for i in range(segments + 1):
        angle = math.pi / 2 + (i * math.pi / 2) / segments
        x = -inner_width/2 - curve_radius + curve_radius * math.cos(angle)
        y = inner_height/2 + curve_radius + curve_radius * math.sin(angle)
        vertices.append((x, y, -depth/2))
    
    # Create back face (z = depth/2) - same pattern as front face
    front_vertices_count = len(vertices)
    for i in range(front_vertices_count):
        v = vertices[i]
        vertices.append((v[0], v[1], depth/2))
    
    # Apply rotation (in radians)
    rx, ry, rz = np.radians(rotation)
    
    # Rotation matrices
    Rx = np.array([
        [1, 0, 0],
        [0, math.cos(rx), -math.sin(rx)],
        [0, math.sin(rx), math.cos(rx)]
    ])
    
    Ry = np.array([
        [math.cos(ry), 0, math.sin(ry)],
        [0, 1, 0],
        [-math.sin(ry), 0, math.cos(ry)]
    ])
    
    Rz = np.array([
        [math.cos(rz), -math.sin(rz), 0],
        [math.sin(rz), math.cos(rz), 0],
        [0, 0, 1]
    ])
    
    # Apply rotations and translation
    rotated_vertices = []
    for v in vertices:
        # Convert to numpy array for matrix operations
        v_array = np.array(v)
        
        # Apply rotations
        v_rotated = Rz @ (Ry @ (Rx @ v_array))
        
        # Apply translation
        v_final = v_rotated + np.array(position)
        
        rotated_vertices.append(tuple(v_final))
    
    # Generate faces (1-indexed for OBJ format)
    faces = []
    
    # Front face (counter-clockwise when viewed from outside)
    front_face = [i+1 for i in range(front_vertices_count)]
    front_face.reverse()  # Make it counter-clockwise when viewed from outside
    faces.append(front_face)
    
    # Back face (clockwise when viewed from outside to maintain correct orientation)
    back_face = [i+1+front_vertices_count for i in range(front_vertices_count)]
    faces.append(back_face)
    
    # Side faces (connecting front to back)
    # We need to create quads between corresponding vertices on front and back
    for i in range(front_vertices_count):
        next_i = (i + 1) % front_vertices_count
        v1 = i + 1  # Front current
        v2 = next_i + 1  # Front next
        v3 = next_i + 1 + front_vertices_count  # Back next
        v4 = i + 1 + front_vertices_count  # Back current
        faces.append([v1, v2, v3, v4])
    
    return rotated_vertices, faces

def create_rectangular_prism(width, height, depth, position=(0, 0, 0), rotation=(0, 0, 0)):
    """
    Generate a rectangular prism with specified dimensions
    
    Args:
    width: Width along x-axis
    height: Height along y-axis
    depth: Depth along z-axis
    position: (x, y, z) position of the center of the prism
    rotation: (rx, ry, rz) rotation in degrees around each axis
    
    Returns:
    vertices, faces for OBJ format
    """
    # Generate vertices (8 corners of the rectangular prism)
    half_width, half_height, half_depth = width/2, height/2, depth/2
    vertices = [
        (-half_width, -half_height, -half_depth),  # 0: bottom face, back left
        (half_width, -half_height, -half_depth),   # 1: bottom face, back right
        (half_width, half_height, -half_depth),    # 2: bottom face, front right
        (-half_width, half_height, -half_depth),   # 3: bottom face, front left
        (-half_width, -half_height, half_depth),   # 4: top face, back left
        (half_width, -half_height, half_depth),    # 5: top face, back right
        (half_width, half_height, half_depth),     # 6: top face, front right
        (-half_width, half_height, half_depth)     # 7: top face, front left
    ]
    
    # Apply rotation (in radians)
    rx, ry, rz = np.radians(rotation)
    
    # Rotation matrices
    Rx = np.array([
        [1, 0, 0],
        [0, math.cos(rx), -math.sin(rx)],
        [0, math.sin(rx), math.cos(rx)]
    ])
    
    Ry = np.array([
        [math.cos(ry), 0, math.sin(ry)],
        [0, 1, 0],
        [-math.sin(ry), 0, math.cos(ry)]
    ])
    
    Rz = np.array([
        [math.cos(rz), -math.sin(rz), 0],
        [math.sin(rz), math.cos(rz), 0],
        [0, 0, 1]
    ])
    
    # Apply rotations and translation
    rotated_vertices = []
    for v in vertices:
        # Convert to numpy array for matrix operations
        v_array = np.array(v)
        
        # Apply rotations
        v_rotated = Rz @ (Ry @ (Rx @ v_array))
        
        # Apply translation
        v_final = v_rotated + np.array(position)
        
        rotated_vertices.append(tuple(v_final))
    
    # Generate faces (1-indexed for OBJ format)
    # Each face is defined counter-clockwise when viewed from outside
    faces = [
        [1, 4, 3, 2],  # Bottom face (-z)
        [5, 6, 7, 8],  # Top face (+z)
        [1, 2, 6, 5],  # Right face (+x)
        [4, 8, 7, 3],  # Left face (-x)
        [2, 3, 7, 6],  # Front face (+y)
        [1, 5, 8, 4]   # Back face (-y)
    ]
    
    return rotated_vertices, faces

def create_cylinder(radius, height, num_sides=32, position=(0, 0, 0), rotation=(0, 0, 0)):
    """
    Generate a cylinder with specified parameters
    
    Args:
    radius: Radius of the cylinder
    height: Height of the cylinder
    num_sides: Number of sides for approximating the circular base
    position: (x, y, z) position of the center of the cylinder
    rotation: (rx, ry, rz) rotation in degrees around each axis
    
    Returns:
    vertices, faces for OBJ format
    """
    # Generate base vertices
    base_vertices = []
    for i in range(num_sides):
        angle = 2 * math.pi * i / num_sides
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        base_vertices.append((x, y, -height/2))  # Bottom face
    
    # Generate top vertices
    top_vertices = [(x, y, height/2) for x, y, _ in base_vertices]  # Top face
    
    # Combine all vertices
    vertices = base_vertices + top_vertices
    
    # Apply rotation (in radians)
    rx, ry, rz = np.radians(rotation)
    
    # Rotation matrices
    Rx = np.array([
        [1, 0, 0],
        [0, math.cos(rx), -math.sin(rx)],
        [0, math.sin(rx), math.cos(rx)]
    ])
    
    Ry = np.array([
        [math.cos(ry), 0, math.sin(ry)],
        [0, 1, 0],
        [-math.sin(ry), 0, math.cos(ry)]
    ])
    
    Rz = np.array([
        [math.cos(rz), -math.sin(rz), 0],
        [math.sin(rz), math.cos(rz), 0],
        [0, 0, 1]
    ])
    
    # Apply rotations and translation
    rotated_vertices = []
    for v in vertices:
        # Convert to numpy array for matrix operations
        v_array = np.array(v)
        
        # Apply rotations
        v_rotated = Rz @ (Ry @ (Rx @ v_array))
        
        # Apply translation
        v_final = v_rotated + np.array(position)
        
        rotated_vertices.append(tuple(v_final))
    
    # Generate faces (1-indexed for OBJ format)
    faces = []
    
    # Bottom face (counter-clockwise when viewed from outside)
    bottom_face = [i+1 for i in range(num_sides)]
    bottom_face.reverse()  # Make it counter-clockwise when viewed from outside
    faces.append(bottom_face)
    
    # Top face (counter-clockwise when viewed from outside)
    top_face = [i+1+num_sides for i in range(num_sides)]
    faces.append(top_face)
    
    # Side faces (quads)
    for i in range(num_sides):
        v1 = i + 1
        v2 = (i + 1) % num_sides + 1
        v3 = (i + 1) % num_sides + 1 + num_sides
        v4 = i + 1 + num_sides
        faces.append([v1, v2, v3, v4])
    
    return rotated_vertices, faces

def save_obj(filename, all_vertices, all_faces):
    """Save multiple shapes as a single OBJ file"""
    with open(filename, 'w') as f:
        f.write("# Multiple shapes OBJ file\n")
        
        vertex_count = 0
        
        # Write vertices and faces for each shape
        for vertices, faces in zip(all_vertices, all_faces):
            # Write vertices
            for v in vertices:
                f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
            
            # Write faces with adjusted indices
            for face in faces:
                adjusted_face = [idx + vertex_count for idx in face]
                f.write(f"f {' '.join(str(i) for i in adjusted_face)}\n")
            
            # Update vertex count for the next shape
            vertex_count += len(vertices)
        
        print(f"OBJ file saved as {filename}")

def main():
    # Main rectangular prism (13x5.6x1)
    main_prism_vertices, main_prism_faces = create_rounded_prism(
        width=14.0, 
        height=6.0, 
        depth=1.0, 
        position=(0, 0, 0), 
        rotation=(0, 0, 0),
        curve_radius=0.8
    )
    
    # Get user input for tiny prisms
    print("Enter dimensions for the first tiny rectangular prism:")
    tiny1_width = 1
    tiny1_height = 0.6
    tiny1_depth = 0.8
    tiny1_x = 5.5
    tiny1_y = 3
    tiny1_z = 0
    
    print("\nEnter dimensions for the second tiny rectangular prism:")
    tiny2_width = tiny1_width
    tiny2_height = tiny1_height
    tiny2_depth = tiny1_depth
    tiny2_x = tiny1_x - 1.2
    tiny2_y = tiny1_y 
    tiny2_z = tiny1_z
    
    # Get user input for cylinder
    print("\nEnter dimensions for the cylinder:")
    cyl_radius = 0.5
    cyl_height = 0.6
    cyl_x = 5
    cyl_y = 1
    cyl_z = 0.5
    
    # Create tiny prisms
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
    
    # Create cylinder
    cylinder_vertices, cylinder_faces = create_cylinder(
        radius=cyl_radius, 
        height=cyl_height, 
        position=(cyl_x, cyl_y, cyl_z)
    )
    
    # Combine all shapes
    all_vertices = [main_prism_vertices, tiny_prism1_vertices, tiny_prism2_vertices, cylinder_vertices]
    all_faces = [main_prism_faces, tiny_prism1_faces, tiny_prism2_faces, cylinder_faces]
    
    # Save to OBJ file
    save_obj("../shapes.obj", all_vertices, all_faces)
    
    print("\nCreated shapes.obj with:")
    print(f"- Main rounded prism: 14.0 x 6.0 x 1.0 at position (0, 0, 0)")
    print(f"- Tiny prism 1: {tiny1_width} x {tiny1_height} x {tiny1_depth} at position ({tiny1_x}, {tiny1_y}, {tiny1_z})")
    print(f"- Tiny prism 2: {tiny2_width} x {tiny2_height} x {tiny2_depth} at position ({tiny2_x}, {tiny2_y}, {tiny2_z})")
    print(f"- Cylinder: radius {cyl_radius}, height {cyl_height} at position ({cyl_x}, {cyl_y}, {cyl_z})")
    print("\nYou can visualize this file using the vis.py script:")
    print("python vis.py shapes.obj")

if __name__ == "__main__":
    main()
