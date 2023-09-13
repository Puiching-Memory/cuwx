import ctypes
import os

# https://learn.microsoft.com/zh-cn/windows/win32/api/wingdi/nf-wingdi-addfontresourcew
#TODO:载入字体后发送系统通知

def Load(path):
	gdi32 = ctypes.WinDLL("gdi32.dll")  # 调用此DLL载入字体
	gdi32.AddFontResourceW(path)


def Unload(path):
	gdi32 = ctypes.WinDLL("gdi32.dll")  # 调用此DLL卸载字体
	gdi32.RemoveFontResourceW(path)


def find_files(directory, extension):
	'''
		directory = './cuwx/font'  # 请将此处替换为你的文件夹路径  
		extensions = '.ttf'
		re = cuwx.Font.find_files(directory,extensions)
		print(re)
	'''
	file_paths = []  
	for root, dirs, files in os.walk(directory):  
		for file in files:  
			if file.endswith(extension):  
				file_paths.append(os.path.join(root, file))  

	return file_paths

if __name__ == "__main__":
	pass