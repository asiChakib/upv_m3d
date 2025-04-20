import pyvista as pv
import numpy as np
import sys

# Create a PyVista plotter
plotter = pv.Plotter()
objfile = './tetra_lo.obj'

try :
    objfile = sys.argv[1]
except Exception:
    print("the argument passed is WRONG")

# Read the OBJ file
mesh = pv.read(objfile)

# Add the mesh to the plotter with enhanced visualization
plotter.add_mesh(mesh, 
                show_edges=True,          # Show edges of the mesh
                line_width=2,             # Edge line width
                color='lightblue',        # Face color
                opacity=0.7,              # Slight transparency
                edge_color='black',       # Edge color
                smooth_shading=True)      # Smooth shading

# Add coordinate axes for reference
plotter.add_axes()

# Add bounding box
plotter.show_bounds(grid='front', location='outer')

# Set initial camera position for better view
plotter.camera_position = [(5, 5, 5),    # Camera position
                         (0, 0, 1.7),    # Focus point
                         (0, 0, 1)]      # Up vector

# Add title
plotter.add_title("Pentagon Prism Visualization")

# Add movement instructions
plotter.add_text(
    'Controls:\n' +
    'Pan: Middle-click + drag\n' +
    'Rotate: Left-click + drag\n' +
    'Zoom: Mouse wheel or Right-click + drag\n' +
    'Reset: r key',
    position='upper_left',
    font_size=12
)

# Show the plot
plotter.show()

print("\nVisualization complete!")
print("The pentagon prism should be displayed with:")
print("- 5 sides")
print("- Height of 3.4 units")
print("- Radius of 1.0 unit")
print("- Transparent faces and visible edges")
print("- Interactive controls for viewing from all angles")