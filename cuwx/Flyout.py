
import wx
import win32mica
import cuwx

class FlyoutN(wx.Frame):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		self.SizerMain = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( self.SizerMain )
		self.Layout()

		self.Centre( wx.BOTH )



		# 启用win11云母效果
		hwnd = self.GetHandle()
		mode = win32mica.MicaTheme.AUTO
		style = win32mica.MicaStyle.DEFAULT
		win32mica.ApplyMica(HWND=hwnd, Theme=mode, Style=style)


		# 启用双缓冲
		self.SetDoubleBuffered(True)

		self.Bind(wx.EVT_SHOW,self.OnShow)
		self.Bind(wx.EVT_KILL_FOCUS,self.OnKillFocus)


	def Append_Text(self,Lable,size:wx.Size=wx.DefaultSize):
		self.SizerMain.Add(cuwx.Button.ButtonN( self, wx.ID_ANY, u"File", wx.DefaultPosition, size, wx.BORDER_NONE ))

	def Append_Button(self,Lable):
		self.SizerMain.Add(wx.TextCtrl( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 ))

	
	def Set2Dark(self):
		self.SetBackgroundColour(wx.Colour("black"))
		self.SetForegroundColour(wx.Colour("white"))

	def Set2Light(self):
		self.SetBackgroundColour(wx.Colour("white"))
		self.SetForegroundColour(wx.Colour("black"))

	def OnShow(self,event):
		##print(1)
		event.Skip()

	def OnKillFocus(self,event):
		self.Hide()

##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = FlyoutN(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
