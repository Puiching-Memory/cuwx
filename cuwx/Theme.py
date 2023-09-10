import wx
import winreg

def get_windows_theme_color():
	'''
	查询注册表项->主题颜色
	---
	arg:None
	return:(R,G,B,A)
	'''
	tarkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\DWM')
	val = winreg.QueryValueEx(tarkey,'ColorizationColor')

	color16 = hex(val[0])
	A = int(str(color16)[2:4],16)
	R = int(str(color16)[4:6],16)
	G = int(str(color16)[6:8],16)
	B = int(str(color16)[8:10],16)
		
	return (R,G,B,A)  


if __name__ == "__main__":
	print(get_windows_theme_color())
	