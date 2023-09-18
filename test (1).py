
import wx
import GUI_Fly
import win32mica

class CalcFrame(GUI_Fly.MyPanel1):
    def __init__(self, parent):
        # 定义主函数
        super().__init__(parent)


        # 启用win11云母效果
        hwnd = self.GetHandle()
        mode = win32mica.MicaTheme.AUTO
        style = win32mica.MicaStyle.DEFAULT
        win32mica.ApplyMica(HWND=hwnd, Theme=mode, Style=style)


        # 启用双缓冲
        self.SetDoubleBuffered(True)


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
