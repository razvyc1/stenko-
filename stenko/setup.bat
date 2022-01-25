@echo off
color F
title stenko - setup 
python -m pip install -r req.txt
cls
echo starting builder.bat
start builder.bat
echo press any key to exit 
pause >nul