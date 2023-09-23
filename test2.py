import wx  
import math
  
class MyFrame(wx.Frame):  
    def __init__(self, parent, id, title):  
        wx.Frame.__init__(self, parent, id, title, size=(390, 350))  
  
    def OnPaint(self, event):  
        dc = wx.PaintDC(self)  
        text = "Hello, wxPython!"  
        font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)  
        dc.SetFont(font)  
        tw, th = dc.GetTextExtent(text)  # 获取文本的大小  
        x, y = 100, 100  # 原始位置  
        angle = 45  # 旋转角度  
  
        # 计算新的位置  
        new_x = x + th * math.sin(math.radians(angle))  
        new_y = y - tw * math.cos(math.radians(angle))  
  
        dc.DrawRotatedText(text, new_x, new_y, angle)  
  
app = wx.App()  
frame = MyFrame(None, -1, "Rotated Text Example")  
frame.Show()  
app.MainLoop()