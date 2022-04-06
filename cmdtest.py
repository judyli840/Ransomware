import winreg

path = winreg.HKEY_CURRENT_USER

def create_disablecmd_key():
    try:
        key = winreg.OpenKeyEx(path, r"SOFTWARE\\")
        newKey = winreg.CreateKey(key,"System")
        winreg.SetValueEx(newKey, "DisableCMD", 0, winreg.REG_DWORD, str(0))
        if newKey:
            winreg.CloseKey(newKey)
    except Exception as e:
            print(e)

create_disablecmd_key()