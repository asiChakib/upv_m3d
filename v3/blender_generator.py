from pathlib import Path

# Your input values
CAM_SIDE = [(1, 1, 0.5), (-1, 1, 0.5)]
BUT_DIM = (0.2, 0.5, 0.1)
BUTTON = (0, -3.8, 0.5)

# Read the template file
template_path = Path("template.py")
with open(template_path, "r") as file:
    template_content = file.read()

# Replace placeholders
final_script = (
    template_content
    .replace("{{ CAM_SIDE }}", str(CAM_SIDE))
    .replace("{{ BUT_DIM }}", str(BUT_DIM))
    .replace("{{ BUTTON }}", str(BUTTON))
)

# Write the final script to file
output_path = Path("final_bscript.py")
with open(output_path, "w") as file:
    file.write(final_script)

print(f"Script written to: {output_path.resolve()}")
