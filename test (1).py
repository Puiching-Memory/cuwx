import winreg

a = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\DWM')
b = winreg.QueryValueEx(a,'ColorizationColor')

color16 = hex(b[0])
A = int(str(color16)[2:4],16)
R = int(str(color16)[4:6],16)
G = int(str(color16)[6:8],16)
B = int(str(color16)[8:10],16)

print(A,R,G,B)