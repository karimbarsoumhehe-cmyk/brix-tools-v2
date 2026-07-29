@echo off
title Brix Tools - Setup
cls
echo Installing the python modules required for Brix Tools:
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.
echo Installation complete! Run "start.bat" to launch the tool.
pause