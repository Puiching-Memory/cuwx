'''
应用层，处理事件/高级算法
'''


##############################
# import
##############################
import BridgeN
st = BridgeN.Analyze(path = './GUI_Base.py')
exec(st,globals())


import wx,wx.xrc
import cuwx
import win32mica

import ctypes

##############################
# GUI的函数桥接
##############################


class CalcFrame(Main,wx.Frame):
	def __init__(self, parent):
		# 定义主函数
		super().__init__(parent)

		#启用win11云母效果
		hwnd = self.GetHandle()
		mode = win32mica.MicaTheme.AUTO
		style = win32mica.MicaStyle.DEFAULT
		win32mica.ApplyMica(HWND=hwnd, Theme=mode, Style=style)

		self.SetBackgroundColour(wx.Colour('black'))
		self.ButtTOOL:wx.Button

		#启用高DPI支持
		try:
			ctypes.windll.shcore.SetProcessDpiAwareness(True)
		except Exception:
			pass
		
		#启用双缓冲
		self.SetDoubleBuffered(True)
			
		#刷新界面
		self.Refresh_bysize()

	def MainOnSize(self, event):
		event.Skip()
		##print(self.GetSize())

	def Refresh_bysize(self):
		x,y = self.GetSize()
		self.SetSize(x+1,y)
		self.SetSize(x,y)
		
##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
