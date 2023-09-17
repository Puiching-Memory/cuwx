'''


'''


def RGB2HSL(R: int, G: int, B: int):
    """
    RGB颜色转为HSL颜色
    ---
    tar:R,G,B->int(0,255)
    return:[H,S,L]
    doc:
        H 色相 (0°,360°)
        S 饱和度 (0%,100%)
        L 亮度 (0%,100%)
    more:https://www.rapidtables.org/zh-CN/convert/color/rgb-to-hsl.html
    """

    r1 = R / 255
    g1 = G / 255
    b1 = B / 255

    Cmax = max(r1, g1, b1)
    Cmin = min(r1, g1, b1)
    Delta = Cmax - Cmin

    # 计算L值
    L = (Cmax + Cmin) / 2

    # 计算H值
    if Delta == 0:
        H = 0
    elif Cmax == r1:
        H = 60 * ((g1 - b1) / Delta % 6)
    elif Cmax == g1:
        H = 60 * ((b1 - r1) / Delta + 2)
    elif Cmax == b1:
        H = 60 * ((r1 - g1) / Delta + 4)

    # 计算S值
    if Delta == 0:
        S = 0
    else:
        S = Delta / (1 - abs(2 * L - 1))

    return [round(H), S, L]


def HSL2RGB(H, S, L):
    """
    HSL颜色转为RGB颜色
    ---
    tar:H,S,L->int(0,255)
    return:[R,G,B]
    doc:
        R Red (0,255)
        G Green (0,255)
        B Blue (0,255)
    more:https://www.rapidtables.org/zh-CN/convert/color/hsl-to-rgb.html
    """
    C = (1 - abs(2 * L - 1)) * S
    X = C * (1 - abs((H / 60) % 2 - 1))
    m = L - C / 2

    if 0 <= H < 60:
        (r1, g1, b1) = (C, X, 0)
    elif 60 <= H < 120:
        (r1, g1, b1) = (X, C, 0)
    elif 120 <= H < 180:
        (r1, g1, b1) = (0, C, X)
    elif 180 <= H < 240:
        (r1, g1, b1) = (0, X, C)
    elif 240 <= H < 300:
        (r1, g1, b1) = (X, 0, C)
    elif 300 <= H < 360:
        (r1, g1, b1) = (C, X, 0)

    (R, G, B) = ((r1 + m) * 255, (g1 + m) * 255, (b1 + m) * 255)

    return [round(R), round(G), round(B)]


if __name__ == "__main__":
    print(HSL2RGB(100, 0.1, 0.8))
