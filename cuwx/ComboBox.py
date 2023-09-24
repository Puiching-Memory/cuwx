import wx
import wx.lib.newevent
import win32api
from .ComboPopup import *
from .Theme import get_windows_theme_color
from .MathN import *

# 自定义事件
combobox_cmd_event_down, EVT_COMBOBOX_DOWN = wx.lib.newevent.NewCommandEvent()  # 按下事件
combobox_cmd_event_up, EVT_COMBOBOX_UP = wx.lib.newevent.NewCommandEvent()  # 松开事件

# TODO:可变箭头角度


class ComboBoxN(wx.Control):
    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        tips="",
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=wx.NO_BORDER,
        choise=[],
        *args,
        **kwargs
    ):
        wx.Control.__init__(self, parent, id, pos, size, wx.NO_BORDER, *args, **kwargs)

        self.parent = parent

        # 获取屏幕设置信息
        settings = win32api.EnumDisplaySettings(
            win32api.EnumDisplayDevices().DeviceName, -1
        )

        self.IS_Checked = False  # 是否按下
        self.IS_Empty = True  # 选项是否为空(将显示提示字符)
        self.NArrow_Angle = 0  # 当前箭头角度,范围:0-360°
        self.TArrow_Angle = 0  # 目标箭头角度

        self.IS_First_Tick = True  # 是否为首帧
        self.Tick_Frame = 0  # 当前帧
        self.FPS = settings.DisplayFrequency  # 帧率/秒
        self.Last_time = 0.2  # 动画持续时间
        self.AL_Frames = 0  # 总帧数

        self.Popupwindow = ComboPopupN(parent=self, choise=[], size=wx.Size(self.GetSize()[0], 200))

        # 动画计时器
        self.timer = wx.Timer()
        self.timer.SetOwner(self, wx.ID_ANY)

        # 设置默认颜色
        r = get_windows_theme_color()[0]
        g = get_windows_theme_color()[1]
        b = get_windows_theme_color()[2]
        self.ThemeColour = [r, g, b]
        self.SNBrushColour = wx.Colour(20, 20, 20)  # 刷子颜色，这通常会用于内填充
        self.SNPenColour = wx.Colour(255, 208, 104)  # 笔颜色，这通常会用于描边
        self.UNBrushColour = [0, 0, 0]  # 用户刷子颜色,不使用wx.colour,因为精度不足,用于计算动画
        self.UNPenColour = [255, 208, 104]  # 用户笔颜色
        self.UTBrushColour = [0, 0, 0]  # 目标刷子颜色
        self.UTPenColour = [255, 208, 104]  # 目标笔颜色
        self.SetForegroundColour(wx.Colour("white"))  # 字体颜色
        self.SetBackgroundColour(wx.Colour("black"))  # 背景颜色

        self.SetLabel(tips)

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
        self.Bind(wx.EVT_KILL_FOCUS, self.OnLeftUp)
        self.Bind(wx.EVT_MOVE, self.OnMove)

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

        dc.SetPen(wx.Pen(self.SNPenColour))
        dc.SetBrush(wx.Brush(self.SNBrushColour))
        dc.DrawRoundedRectangle(0, 0, width, height, 4)

        self.SetForegroundColour(wx.Colour("white"))
        dc.DrawText(self.GetLabel(), 10, round(height / 2 - textHeight / 2))
        dc.DrawRotatedText("\uE70D", 80, round(height / 2 - textHeight / 2), 0)

    def EraseBackground(self, event):
        pass
        # event.Skip()

    def OnSize(self, event):
        event.Skip()

    def OnMove(self, event):
        event.Skip()

    def OnLeftDown(self, event):
        if self.IS_Checked == False:
            self.UTBrushColour = [40, 40, 40]
            self.Last_time = 0.2
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))

            # 发送事件
            wx.PostEvent(self, combobox_cmd_event_down(id=self.GetId(), value=None))
        else:
            self.UTBrushColour = [60, 60, 60]
            self.Last_time = 0.2
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))

            wx.PostEvent(self, combobox_cmd_event_down(id=self.GetId(), value=None))

    def OnLeftUp(self, event):
        if self.IS_Checked == False:
            self.IS_Checked = True
            self.UTPenColour = self.ThemeColour
            self.UTBrushColour = [70, 70, 70]
            self.TArrow_Angle = 180
            self.Last_time = 0.2
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))

            # 显示下拉列表
            self.Popupwindow.SetPosition(
                wx.Point(
                    self.GetScreenPosition()[0],
                    self.GetScreenPosition()[1] + self.GetSize()[1] + 5,
                )
            )
            self.Popupwindow.Show()
            self.Popupwindow.OnShow()
            self.Popupwindow.SetFocus()
            wx.PostEvent(self, combobox_cmd_event_up(id=self.GetId(), value=None))
        else:
            self.IS_Checked = False
            self.UTBrushColour = [45, 45, 45]
            self.UTPenColour = [230, 170, 94]
            self.TArrow_Angle = 0
            self.Last_time = 0.2
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))

            self.Popupwindow.OnHide()
            wx.PostEvent(self, combobox_cmd_event_up(id=self.GetId(), value=None))

    def OnEnterWindow(self, event):
        self.SetCursor(wx.Cursor(6))
        if self.IS_Checked == True:
            self.UTBrushColour = [80, 80, 80]
            self.UTPenColour = self.ThemeColour
            self.Last_time = 0.2
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))
        else:
            self.UTBrushColour = [45, 45, 45]
            self.UTPenColour = [230, 170, 94]
            self.Last_time = 0.2
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))

    def OnLeaveWindow(self, event):
        self.SetCursor(wx.Cursor(1))
        if self.IS_Checked == True:
            self.UTBrushColour = [70, 70, 70]
            self.UTPenColour = self.ThemeColour
            self.Last_time = 0.2
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))
        else:
            self.UTBrushColour = [0, 0, 0]
            self.UTPenColour = [255, 208, 104]
            self.Last_time = 0.2
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

            ##self.BArrow_Angle = self.NArrow_Angle

            # 差值
            self.RBdistance = self.UTBrushColour[0] - self.RBrush
            self.GBdistance = self.UTBrushColour[1] - self.GBrush
            self.BBdistance = self.UTBrushColour[2] - self.BBrush

            self.RPdistance = self.UTPenColour[0] - self.RPen
            self.GPdistance = self.UTPenColour[1] - self.GPen
            self.BPdistance = self.UTPenColour[2] - self.BPen

            ##self.DArrow_Angle = self.BArrow_Angle - self.TArrow_Angle

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

            ##self.NArrow_Angle = self.BArrow_Angle + self.DArrow_Angle * sc

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
