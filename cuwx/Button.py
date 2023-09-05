import wx


class but(wx.Control):
	def __init__(
		self,
		parent,
		id=wx.ID_ANY,
		label="",
		bmp=None,
		center=True,
		flat=False,
		pos=wx.DefaultPosition,
		size=wx.DefaultSize,
		style=wx.NO_BORDER,
		*args,
		**kwargs
	):
		wx.Control.__init__(self, parent, id, pos, size, style, *args, **kwargs)

		self.parent = parent

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		##self.Bind(wx.EVT_ERASE_BACKGROUND, lambda x: None)
		##self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
		##self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
		##self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
		##self.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)
		##self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
		##self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
		##self.Bind(wx.EVT_SIZE, self.OnSize)


	def OnPaint(self, event):
		wx.PaintDC(self)
		print('OnPaint')

