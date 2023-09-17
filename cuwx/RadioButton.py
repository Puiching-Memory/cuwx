import wx
import wx.lib.newevent
import win32api
from .Theme import get_windows_theme_color

# 自定义事件
button_cmd_event_push, EVT_CHECKBOX_PUSH = wx.lib.newevent.NewCommandEvent()  # 按下按钮事件
button_cmd_event_up, EVT_CHECKBOX_UP = wx.lib.newevent.NewCommandEvent()  # 松开按钮事件

# TODO:重构


class CheckBoxN(wx.Control):
    def __init__(
        self,
        parent,
        id=wx.ID_ANY,
        label="",
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=wx.BORDER_NONE,
        validator=wx.DefaultValidator,
    ):
        wx.Control.__init__(self, parent, id, pos, size, wx.BORDER_NONE, validator)

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

        self.IS_Checked = False  # 是否选中
        self.IS_Show_Edge = False  # 是否显示边框

        # 动画计时器
        self.timer = wx.Timer()
        self.timer.SetOwner(self, wx.ID_ANY)

        # 设置默认颜色
        self.SNBrushColour = wx.Colour(25, 25, 25)  # 刷子颜色，这通常会用于内填充
        self.SNPenColour = wx.Colour(255, 208, 104)  # 笔颜色，这通常会用于描边
        self.UNBrushColour = [0, 0, 0]  # 用户刷子颜色,不使用wx.colour,因为精度不足,用于计算动画
        self.UNPenColour = [255, 208, 104]  # 用户笔颜色

        # 从注册表获取主题色
        r = get_windows_theme_color()[0]
        g = get_windows_theme_color()[1]
        b = get_windows_theme_color()[2]
        self.ThemeColour = [r, g, b]  # 系统主题颜色
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
        ##dc.DrawRoundedRectangle(0, 0, width, height, 0) #绘制边框
        dc.DrawRoundedRectangle(
            int(width / 2 - textWidth / 2 - 3), int(height / 2 - 15), 30, 30, 4
        )  # 绘制复选框
        dc.DrawRoundedRectangle(
            int(width / 2 - textWidth / 2 - 2), int(height / 2 - 14), 28, 28, 3
        )

        # 计算以居中对齐
        textXpos = width / 2 - textWidth / 2 + 30 + 3
        textYpos = height / 2 - textHeight / 2
        dc.DrawText(label, int(textXpos), int(textYpos))  # 绘制文字

        # 绘制图标
        if self.IS_Checked == True:
            dc.DrawText(
                "✔", int(width / 2 - textWidth / 2), int(height / 2 - textHeight / 2)
            )

    def EraseBackground(self, event):
        pass
        # event.Skip()

    def OnSize(self, event):
        event.Skip()

    def OnLeftDown(self, event):
        if self.IS_Checked == False:
            self.IS_Checked = True
            self.UTBrushColour = self.ThemeColour
            self.Last_time = 0.05
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))
        else:
            self.IS_Checked = False
            self.UTBrushColour = [45, 45, 45]
            self.Last_time = 0.05
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))
        # 发送事件
        wx.PostEvent(
            self, button_cmd_event_push(id=self.GetId(), value=self.IS_Checked)
        )

    def OnEnterWindow(self, event):
        self.SetCursor(wx.Cursor(6))
        if self.IS_Checked == True:
            self.UTBrushColour = [i + 5 for i in self.ThemeColour]
            self.Last_time = 0.05
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
            self.timer.Start(int(1000 / self.FPS))

    def OnLeaveWindow(self, event):
        self.SetCursor(wx.Cursor(1))

    def Set2Dark(self):
        self.SetBackgroundColour(wx.Colour("black"))
        self.SetForegroundColour(wx.Colour("white"))

    def Set2Light(self):
        self.SetBackgroundColour(wx.Colour("white"))
        self.SetForegroundColour(wx.Colour("black"))

    def SetValue(self, bu: bool):
        self.IS_Checked == bu

    def tick(self, event):
        # 线性动画
        if self.IS_First_Tick == True:
            self.IS_First_Tick = False
            # 当前颜色值
            RBrush = self.UNBrushColour[0]
            GBrush = self.UNBrushColour[1]
            BBrush = self.UNBrushColour[2]

            RPen = self.UNPenColour[0]
            GPen = self.UNPenColour[1]
            BPen = self.UNPenColour[2]

            # 目标颜色值
            RBrushTar = self.UTBrushColour[0]
            GBrushTar = self.UTBrushColour[1]
            BBrushTar = self.UTBrushColour[2]

            RPenTar = self.UTPenColour[0]
            GPenTar = self.UTPenColour[1]
            BPenTar = self.UTPenColour[2]

            # 颜色差值
            RBdistance = RBrushTar - RBrush
            GBdistance = GBrushTar - GBrush
            BBdistance = BBrushTar - BBrush

            RPdistance = RPenTar - RPen
            GPdistance = GPenTar - GPen
            BPdistance = BPenTar - BPen

            # 动画总帧数
            self.AL_Frames = round(self.FPS * self.Last_time)

            # 颜色步长
            self.RBstep = RBdistance / self.AL_Frames
            self.GBstep = GBdistance / self.AL_Frames
            self.BBstep = BBdistance / self.AL_Frames

            self.RPstep = RPdistance / self.AL_Frames
            self.GPstep = GPdistance / self.AL_Frames
            self.BPstep = BPdistance / self.AL_Frames

        if self.Tick_Frame != self.AL_Frames:
            self.Tick_Frame += 1

            self.UNBrushColour[0] += self.RBstep
            self.UNBrushColour[1] += self.GBstep
            self.UNBrushColour[2] += self.BBstep

            self.SNBrushColour = wx.Colour(
                int(self.UNBrushColour[0]),
                int(self.UNBrushColour[1]),
                int(self.UNBrushColour[2]),
            )

            self.UNPenColour[0] += self.RPstep
            self.UNPenColour[1] += self.GPstep
            self.UNPenColour[2] += self.GPstep

            self.SNPenColour = wx.Colour(
                int(self.UNPenColour[0]),
                int(self.UNPenColour[1]),
                int(self.UNPenColour[2]),
            )

            self.Refresh()
        else:
            self.IS_First_Tick = True
            self.Tick_Frame = 0
            self.timer.Stop()
