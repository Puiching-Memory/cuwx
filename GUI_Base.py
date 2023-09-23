# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 200,100 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		SizerMain = wx.BoxSizer( wx.VERTICAL )

		SizerTop = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Butt1 = wx.Button( self, wx.ID_ANY, u"File", wx.DefaultPosition, wx.Size( 100,50 ), wx.BORDER_NONE )
		SizerTop.Add( self.Butt1, 0, wx.ALL, 5 )

		self.Butt11 = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 100,50 ), wx.BORDER_NONE )
		SizerTop.Add( self.Butt11, 0, wx.ALL, 5 )

		self.Butt12 = wx.Button( self, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.Size( 100,50 ), wx.BORDER_NONE )
		SizerTop.Add( self.Butt12, 0, wx.ALL, 5 )

		self.Butt13 = wx.Button( self, wx.ID_ANY, u"Windows", wx.DefaultPosition, wx.Size( 100,50 ), wx.BORDER_NONE )
		SizerTop.Add( self.Butt13, 0, wx.ALL, 5 )

		self.Butt14 = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.Size( 100,50 ), wx.BORDER_NONE )
		SizerTop.Add( self.Butt14, 0, wx.ALL, 5 )

		self.Butt141 = wx.Button( self, wx.ID_ANY, u"CMD", wx.DefaultPosition, wx.Size( 100,50 ), wx.BORDER_NONE )
		SizerTop.Add( self.Butt141, 0, wx.ALL, 5 )

		self.Butt1411 = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.Size( 100,50 ), wx.BORDER_NONE )
		SizerTop.Add( self.Butt1411, 0, wx.ALL, 5 )


		SizerMain.Add( SizerTop, 0, 0, 5 )

		SizerSide = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"启用多线程ENG", wx.DefaultPosition, wx.Size( 200,50 ), 0 )
		self.m_checkBox1.SetValue(True)
		SizerSide.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerSide.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerSide.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerSide.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerSide.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.SwitchMA = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 200,40 ), 0 )
		SizerSide.Add( self.SwitchMA, 0, wx.ALL, 5 )

		CMBAChoices = []
		self.CMBA = wx.ComboBox( self, wx.ID_ANY, u"Combo", wx.DefaultPosition, wx.Size( 100,25 ), CMBAChoices, 0 )
		SizerSide.Add( self.CMBA, 0, wx.ALL, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		SizerSide.Add( self.m_choice1, 0, wx.ALL, 5 )


		SizerMain.Add( SizerSide, 0, 0, 5 )


		self.SetSizer( SizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_KEY_DOWN, self.MainOnKeyDown )
		self.Bind( wx.EVT_MOVE, self.MainOnMove )
		self.Bind( wx.EVT_SIZE, self.MainOnSize )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def MainOnKeyDown( self, event ):
		event.Skip()

	def MainOnMove( self, event ):
		event.Skip()

	def MainOnSize( self, event ):
		event.Skip()


