import wx
import wx.lib
import win32gui
import win32con
import win32print
import win32api
import os
import ctypes
import winreg

from .Button import ButtonN,EVT_BUTTON_PUSH,EVT_BUTTON_UP
from .CheckBox import CheckBoxN,EVT_CHECKBOX_PUSH,EVT_CHECKBOX_UP
from .ToggleButton import ToggleButtonN
from .ToggleSwitch import ToggleSwitchN
from .Flyout import FlyoutN
from .Theme import *
from .Font import *
from .Colour import *
from .DPI import *

version = 100

#TODO:https://learn.microsoft.com/zh-cn/windows/apps/design/controls/
