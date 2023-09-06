import wx


class but(wx.Control):
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
        wx.Control.__init__(self, parent, id, pos, size, style, *args, **kwargs)

        self.parent = parent

        self.label = label
        self.Focus = False

        self.SetLabel(label)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.EraseBackground)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        ##self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        ##self.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)
        ##self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        ##self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseClick)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        if wx.Platform == "__WXMSW__":
            self.Bind(wx.EVT_LEFT_DCLICK, self.OnMouseClick)

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)
        # self.Refresh()

    def Draw(self, dc: wx.DC):
        dc.Clear()

        width, height = self.GetClientSize()  # 可绘制区大小

        dc.SetBrush(wx.Brush(self.GetBackgroundColour()))
        dc.SetPen(wx.Pen("yellow"))

        dc.SetBackground(dc.GetBrush())  # 绘制背景

        dc.SetFont(self.GetFont())  # 设置字体
        label = self.GetLabel()  # 设置文本
        textWidth, textHeight = dc.GetTextExtent(label)  # 获取文本区大小

        dc.DrawRoundedRectangle(0, 0, width, height, 8)  # 绘制圆角

        # 计算以居中对齐
        textXpos = width / 2 - textWidth / 2
        textYpos = height / 2 - textHeight / 2
        dc.DrawText(label, int(textXpos), int(textYpos))  # 绘制文字

    def EraseBackground(self, event):
        pass
        # event.Skip()

    def OnSize(self, event):
        event.Skip()

    def OnMouseClick(self, event):
        print("left ck")

    def OnSetFocus(self, event):
        pass

    def OnKillFocus(self, event):
        pass

    def Set2Dark(self):
        self.SetBackgroundColour(wx.Colour("black"))
        self.SetForegroundColour(wx.Colour('white'))

    def Set2Light(self):
        pass
    
