
import win32gui
import win32con
import win32print
import win32api


def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """获取缩放后的分辨率"""
    screen_Size_X = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_Size_Y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return screen_Size_X, screen_Size_Y


def GetZoom():
    raw = get_real_resolution()
    real = get_screen_size()
    rate = raw[0] / real[0]

    return rate

if __name__ == "__main__":
    print(round(GetZoom(),3))