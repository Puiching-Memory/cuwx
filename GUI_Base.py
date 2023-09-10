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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 200,100 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		SizerMain = wx.BoxSizer( wx.VERTICAL )

		SizerTop = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.ButtA = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerTop.Add( self.ButtA, 0, wx.ALL, 5 )

		self.Butt6 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.Butt6.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		SizerTop.Add( self.Butt6, 0, wx.ALL, 5 )

		self.ButtTOOL = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		SizerTop.Add( self.ButtTOOL, 0, wx.ALL, 5 )


		SizerMain.Add( SizerTop, 0, 0, 5 )

		SizerSide = wx.BoxSizer( wx.VERTICAL )

		self.Butt221 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerSide.Add( self.Butt221, 0, wx.ALL, 5 )

		self.Buttaaa = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		SizerSide.Add( self.Buttaaa, 0, wx.ALL, 5 )


		SizerMain.Add( SizerSide, 0, 0, 5 )


		self.SetSizer( SizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_KEY_DOWN, self.MainOnKeyDown )
		self.Bind( wx.EVT_SIZE, self.MainOnSize )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def MainOnKeyDown( self, event ):
		event.Skip()

	def MainOnSize( self, event ):
		event.Skip()


