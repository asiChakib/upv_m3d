#!/bin/bash

clear

# Run the first Python script
python3 main.py
echo "First step is completed successfully."

# Ask the user if they want to see the visualization
while true; do
    read -p "Do you want to see the visualization created with vis.py? (y/n): " choice
    case "$choice" in
        [Yy]* ) 
            python3 vis.py shapes.obj
            break
            ;;
        [Nn]* ) 
            echo "Skipping visualization."
            break
            ;;
        * ) 
            echo "Invalid choice. Please enter y or n."
            ;;
    esac
done

clear
read -p "Press any key to exit..."