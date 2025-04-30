@echo off
cls

python main.py
echo First step is completed successfully.

:ask
echo Do you want to see the visualization created with vis.py? (y/n)
set /p choice=

if /i "%choice%"=="y" (
    python vis.py shapes.obj
) else if /i "%choice%"=="n" (
    echo Skipping visualization.
) else (
    echo Invalid choice. Please enter y or n.
    goto ask
)

cls