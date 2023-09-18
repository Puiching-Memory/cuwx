"""
应用层，处理事件/高级算法
比起一般流程，需要多做什么工作？
1.桥接
2.事件绑定
3.字体调整
"""

##############################
# import
##############################
# 桥接,载入GUI类
import BridgeN

st = BridgeN.Analyze(path="./GUI_Base.py")
exec(st, globals())
del st

import wx, wx.xrc
import cuwx
import win32mica
import darkdetect
import ctypes
import os

##############################
# GUI的函数桥接
##############################


class CalcFrame(Main, wx.Frame):
    def __init__(self, parent):
        # 定义主函数
        super().__init__(parent)

        # 系统声明,禁用高DPI自动缩放
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(False)
        except Exception:
            pass

        # 启用win11云母效果
        hwnd = self.GetHandle()
        mode = win32mica.MicaTheme.AUTO
        style = win32mica.MicaStyle.DEFAULT
        win32mica.ApplyMica(HWND=hwnd, Theme=mode, Style=style)

        # 编辑器识别符
        self.Butt1: cuwx.Button
        self.Butt6: cuwx.Button

        # 查找字体路径
        directory = "./cuwx/font"

        extensions = ".ttf"
        re = cuwx.Font.find_files(directory, extensions)

        # 安装字体（临时-关机删除）
        for i in re:
            path = os.path.abspath(i)
            cuwx.Font.Load(path)

        Englist_Font = wx.Font(
            9,
            wx.FONTFAMILY_MODERN,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            False,
            "Rajdhani",
        )

        Chinese_Font = wx.Font(
            9,
            wx.FONTFAMILY_MODERN,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            False,
            "Rajdhani",
        )

        self.Butt1.SetFont(Englist_Font)

        # 启用双缓冲
        self.SetDoubleBuffered(True)

        # 刷新界面
        self.Refresh_bysize()

        # 绑定事件
        self.Bind(cuwx.EVT_BUTTON_PUSH, self.OnLeftDown, self.Butt1)
        self.Bind(cuwx.EVT_BUTTON_UP, self.OnLeftUp, self.Butt1)

        self.FlyWindows = cuwx.FlyoutN(self)


    def MainOnSize(self, event):
        event.Skip()
        ##print(self.GetSize())

    def MainOnKeyDown(self, event):
        print("检测到快捷键:" + str(event.GetKeyCode()))
        key = int(event.GetKeyCode())

        match key:
            case 27:  # ESC
                self.Destroy()
            case 48:  # 0
                pass
            case 49:  # 1
                pass
            case 50:  # 2
                pass
            case 51:  # 3
                pass
            case 52:  # 4
                pass
            case 53:  # 5
                pass
            case 54:  # 6
                pass
            case 55:  # 7
                pass
            case 56:  # 8
                pass
            case 57:  # 9
                pass
            case 340:  # F1
                pass
            case 341:  # F2
                pass
            case 342:  # F3
                pass
            case 343:  # F4
                pass
            case _:
                pass

    def Refresh_bysize(self):
        x, y = self.GetSize()
        self.SetSize(x + 1, y)
        self.SetSize(x, y)

    def OnLeftDown(self, event):
        if self.FlyWindows.IsShown() == False:
            self.FlyWindows.Show()
            self.FlyWindows.Append_Text('aaa',wx.Size(100,100))
        else:
            self.FlyWindows.SetFocus()

    def OnLeftUp(self, event):
        print(2)

    def MainOnMove(self, event):
        ##print(self.GetPosition())
        event.Skip()


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
