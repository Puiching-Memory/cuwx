import wx
from .Button import *

IS_DARK = True
IS_LIGHT = False
DARK = 0
LIGHT = 1
THEME = DARK

def Set2Dark():
	try:
		er = but
		er.Set2Dark()

	except Exception as error:
		print(error)
		return
	else:
		IS_DARK = True
		IS_LIGHT = False
		THEME = DARK


def Set2Light():
	try:
		but.Set2Light()

	except Exception as error:
		print(error)
		return
	else:
		IS_DARK = False
		IS_LIGHT = True
		THEME = LIGHT