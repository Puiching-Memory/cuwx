import wx
import wx.lib.newevent
import win32api
from .MathN import *

# 自定义事件
button_cmd_event_push, EVT_BUTTON_PUSH = wx.lib.newevent.NewCommandEvent()  # 按下按钮事件
button_cmd_event_up, EVT_BUTTON_UP = wx.lib.newevent.NewCommandEvent()  # 松开按钮事件

# TODO:按钮内阴影
# TODO:高DPI支持
# TODO:内存优化


class ButtonN(wx.Control):
    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        label="",
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=wx.NO_BORDER,
        *args,
        **kwargs
    ):
        wx.Control.__init__(self, parent, id, pos, size, wx.NO_BORDER, *args, **kwargs)

        self.parent = parent

        # 获取屏幕设置信息
        settings = win32api.EnumDisplaySettings(
            win32api.EnumDisplayDevices().DeviceName, -1
        )

        self.IS_First_Tick = True  # 是否为首帧
        self.Tick_Frame = 0  # 当前帧
        self.FPS = settings.DisplayFrequency  # 帧率/秒
        self.Last_time = 0.2  # 动画持续时间
        self.AL_Frames = 0  # 总帧数

        # 动画计时器
        self.timer = wx.Timer()
        self.timer.SetOwner(self, wx.ID_ANY)

        # 设置默认颜色
        self.SNBrushColour = wx.Colour(0, 0, 0)  # 刷子颜色，这通常会用于内填充
        self.SNPenColour = wx.Colour(255, 208, 104)  # 笔颜色，这通常会用于描边
        self.UNBrushColour = [0, 0, 0]  # 用户刷子颜色,不使用wx.colour,因为精度不足,用于计算动画
        self.UNPenColour = [255, 208, 104]  # 用户笔颜色
        self.UTBrushColour = [0, 0, 0]  # 目标刷子颜色
        self.UTPenColour = [255, 208, 104]  # 目标笔颜色
        self.SetForegroundColour(wx.Colour("white"))  # 字体颜色
        self.SetBackgroundColour(wx.Colour("black"))  # 背景颜色

        self.SetLabel(label)

        # 事件绑定
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.EraseBackground)
        ##self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        ##self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.Bind(wx.EVT_TIMER, self.tick, id=wx.ID_ANY)  # 计时器事件

        if wx.Platform == "__WXMSW__":
            self.Bind(wx.EVT_LEFT_DCLICK, self.OnLeftDown)

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)

    def Draw(self, dc: wx.DC):
        dc.Clear()

        width, height = self.GetClientSize()  # 可绘制区大小

        dc.SetFont(self.GetFont())  # 设置字体
        label = self.GetLabel()  # 设置文本
        textWidth, textHeight = dc.GetTextExtent(label)  # 获取文本区大小

        dc.SetBrush(wx.Brush(self.SNBrushColour))
        dc.SetPen(wx.Pen(self.SNPenColour))
        dc.DrawRoundedRectangle(0, 0, width, height, 4)  # 绘制圆角

        # 计算以居中对齐
        textXpos = width / 2 - textWidth / 2
        textYpos = height / 2 - textHeight / 2
        dc.DrawText(label, int(textXpos), int(textYpos))  # 绘制文字

    def EraseBackground(self, event):
        pass
        # event.Skip()

    def OnSize(self, event):
        event.Skip()

    def OnLeftDown(self, event):
        self.UTBrushColour = [70, 70, 70]
        self.Last_time = 0.1
        self.IS_First_Tick = True
        self.Tick_Frame = 0
        self.timer.Stop()
        self.timer.Start(int(1000 / self.FPS))
        # 发送事件
        wx.PostEvent(self, button_cmd_event_push(id=self.GetId(), value=None))

    def OnLeftUp(self, event):
        self.UTBrushColour = [45, 45, 45]
        self.Last_time = 0.1
        self.IS_First_Tick = True
        self.Tick_Frame = 0
        self.timer.Stop()
        self.timer.Start(int(1000 / self.FPS))
        wx.PostEvent(self, button_cmd_event_up(id=self.GetId(), value=None))

    def OnEnterWindow(self, event):
        self.SetCursor(wx.Cursor(6))
        self.UTBrushColour = [45, 45, 45]
        self.UTPenColour = [230, 170, 94]
        self.Last_time = 0.1
        self.IS_First_Tick = True
        self.Tick_Frame = 0
        self.timer.Stop()
        self.timer.Start(int(1000 / self.FPS))

    def OnLeaveWindow(self, event):
        self.SetCursor(wx.Cursor(1))
        self.UTBrushColour = [0, 0, 0]
        self.UTPenColour = [255, 208, 104]
        self.Last_time = 0.1
        self.IS_First_Tick = True
        self.Tick_Frame = 0
        self.timer.Stop()
        self.timer.Start(int(1000 / self.FPS))

    def Set2Dark(self):
        self.SetBackgroundColour(wx.Colour("black"))
        self.SetForegroundColour(wx.Colour("white"))

    def Set2Light(self):
        self.SetBackgroundColour(wx.Colour("white"))
        self.SetForegroundColour(wx.Colour("black"))

    def tick(self, event):
        # 动画,指数缓入
        if self.IS_First_Tick == True:
            self.IS_First_Tick = False
            # 起始值
            self.RBrush = self.UNBrushColour[0]
            self.GBrush = self.UNBrushColour[1]
            self.BBrush = self.UNBrushColour[2]

            self.RPen = self.UNPenColour[0]
            self.GPen = self.UNPenColour[1]
            self.BPen = self.UNPenColour[2]

            # 差值
            self.RBdistance = self.UTBrushColour[0] - self.RBrush
            self.GBdistance = self.UTBrushColour[1] - self.GBrush
            self.BBdistance = self.UTBrushColour[2] - self.BBrush

            self.RPdistance = self.UTPenColour[0] - self.RPen
            self.GPdistance = self.UTPenColour[1] - self.GPen
            self.BPdistance = self.UTPenColour[2] - self.BPen

            # 动画总帧数
            self.AL_Frames = round(self.FPS * self.Last_time)

        if self.Tick_Frame != self.AL_Frames:
            self.Tick_Frame += 1

            # 获取缩放倍率
            sc = ExponentialEaseOut(self.Tick_Frame / self.AL_Frames)

            self.UNBrushColour[0] = self.RBrush + self.RBdistance * sc
            self.UNBrushColour[1] = self.GBrush + self.GBdistance * sc
            self.UNBrushColour[2] = self.BBrush + self.BBdistance * sc

            self.SNBrushColour = wx.Colour(
                int(self.UNBrushColour[0]),
                int(self.UNBrushColour[1]),
                int(self.UNBrushColour[2]),
            )

            ##print(self.SNBrushColour)

            self.UNPenColour[0] = self.RPen + self.RPdistance * sc
            self.UNPenColour[1] = self.GPen + self.GPdistance * sc
            self.UNPenColour[2] = self.BPen + self.BPdistance * sc

            self.SNPenColour = wx.Colour(
                int(self.UNPenColour[0]),
                int(self.UNPenColour[1]),
                int(self.UNPenColour[2]),
            )

            self.Refresh()
        else:
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            del (
                self.RBrush,
                self.BBrush,
                self.GBrush,
                self.RPen,
                self.GPen,
                self.BPen,
                self.RBdistance,
                self.GBdistance,
                self.BBdistance,
                self.RPdistance,
                self.GPdistance,
                self.BPdistance,
            )
            self.timer.Stop()
