@echo off
setlocal

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else (
    goto gotAdmin
)

:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

"%temp%\getadmin.vbs"
exit /B

:gotAdmin
if exist "%temp%\getadmin.vbs" (
    del "%temp%\getadmin.vbs"
)
pushd "%CD%"
CD /D "%~dp0"
goto :eof  :: or use 'exit /b'

:--------------------------------------
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

:: Define repository URL and clone directory
set "repoURL=https://github.com/sachinsenal0x64/FIXARR"
set "cloneDir=FIXARR"

:: Check if fixarr.py exists
if not exist "%cloneDir%\fixarr.py" (
    echo fixarr.py does not exist. Cloning Git repository...
    git clone %repoURL% %cloneDir%
)

:: Change to the clone directory
cd /d %cloneDir%

:: Print message and install packages
echo Installing Packages......
pip install -r requirements.txt

:: Run fixarr.py without displaying the console window
set python_path=python
set code_file=fixarr.py
start cmd.exe /k %python_path% %code_file%

endlocal
@REM @CMD.EXE
