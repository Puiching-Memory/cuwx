import wx


def RGB2HSL(r, g, b):
    '''
    RGB颜色转为HSL颜色
    ---
    tar:r,g,b->int(0,255)
    return:(H,S,L)
    doc:
    	H 色相 (0°,360°)
        S 饱和度 (0%,100%)
        L 亮度 (0%,100%)
    more:https://www.rapidtables.org/zh-CN/convert/color/rgb-to-hsl.html
    '''

    r1 = r / 255
    g1 = g / 255
    b1 = b / 255

    Cmax = max(r1, g1, b1)
    Cmin = min(r1, g1, b1)
    Delta = Cmax - Cmin

    L = (Cmax + Cmin) / 2

    if Delta == 0:
        H = 0
    elif Cmax == r1:
        H = 60 * ((g1 - b1) / Delta % 6)
    elif Cmax == g1:
        H = 60 * ((b1 - r1) / Delta + 2)
    elif Cmax == b1:
        H = 60 * ((r1 - g1) / Delta + 4)

    if Delta == 0:
        S = 0
    else:
        S = Delta / (1 - abs(2 * L - 1))

    return H, S, L


def HSL2RGB():
    pass


if __name__ == "__main__":
    print(RGB2HSL(100, 10, 80))
