import math
from main_script import *
import config

number_of_cameras = 3
camera_positions = camera

# create cameras
for i in range(number_of_cameras):
    create_camera("PCamera"+str(i+1), co)