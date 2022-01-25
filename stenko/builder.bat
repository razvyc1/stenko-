@echo off
color F
title stenko - name for exe
set /p a=" write the name for exe - "
if [%a%] NEQ [] (
    CALL:icon
    EXIT /B 1 
)
:icon
title stenko - name of icon 
set /p b=" write the name of icon - "
if [%b%] NEQ [] (
    CALL:main
    EXIT /B 1 
)
ECHO is on
:main
title stenko - building %a%
cls
pyinstaller --clean --onefile --noconsole -i %b%.ico -n %a% main.py
rmdir /s /q __pycache__
rmdir /s /q build
del /f / s /q %a%.spec
goto Prep
:Prep
    title stenko - exiting
    SET count=5
    SET genericMessage=the console will be closed
    goto Output
:Output
    cls
        IF NOT %count% == -1 (
        IF %count% == 0 (
        color 0F
            echo - https://stenko.xyz
        ) ELSE (
            echo %genericMessage% in %count%
            echo %a%.exe has been built in 'dist'
        )
        SET /A count=%count% - 1
        ping localhost -n 2 >nul
        goto Output
    ) ELSE (
        exit
    )