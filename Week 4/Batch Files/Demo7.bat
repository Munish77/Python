:: Demo batch file to configure something
:: By: JOR
:: Initial file: 03JAN18
:: Filename: Demo7.bat
@echo off
cls
title JOR’s Find a File
echo *******************************************
echo This batch file will do stuff
echo This is for demonstration purposes only.
echo *******************************************
SET ospath=C:\Windows\
SET filename=explorerr.exe
If exist %ospath%%filename% echo %filename% exists
If not exist %ospath%%filename% echo %filename% not exists
pause