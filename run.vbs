Set WshShell = CreateObject("WScript.Shell")

' Command to mount rclone remote
fixarrCommand = "python fixarr.py"

' Run the command without displaying the console window
WshShell.Run fixarrCommand, 0, False
