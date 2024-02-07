Set WshShell = CreateObject("WScript.Shell")

' Define repository URL and clone directory
repoURL = "https://github.com/sachinsenal0x64/FIXARR"
cloneDir = "FIXARR"

' Check if fixarr.py exists
If Not objFSO.FileExists(cloneDir & "\fixarr.py") Then
    WScript.Echo "fixarr.py does not exist. Cloning Git repository..."
    WshShell.Run "git clone " & repoURL & " " & cloneDir, 0, True
End If

' Change to the clone directory
WshShell.CurrentDirectory = cloneDir

' Print message and install packages
WScript.Echo "Installing Packages......"
WshShell.Run "pip install -r requirements.txt", 0, True

' Run fixarr.py with  displaying the console window
WshShell.Run "python fixarr.py", 1, True
