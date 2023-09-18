"""
动画使用到的数学函数
---
https://github.com/semitable/easing-functions/blob/master/easing_functions/easing.py
https://blog.csdn.net/z2014z/article/details/120691794
https://easings.net/zh-cn#
"""

import math


def LinearInOut(t: float) -> float:
    """
    线性递增函数
    ---
    """
    return t


def QuadEaseIn(t: float) -> float:
    """
    二次方缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInQuad
    """
    return t * t


def QuadEaseOut(t: float) -> float:
    """
    二次方缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutQuad
    """
    return -(t * (t - 2))


def QuadEaseInOut(t: float) -> float:
    """
    二次方缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutQuad
    """
    if t < 0.5:
        return 2 * t * t
    return (-2 * t * t) + (4 * t) - 1


def CubicEaseIn(t: float) -> float:
    """
    三次方缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInCubic
    """
    return t * t * t


def CubicEaseOut(t: float) -> float:
    """
    三次方缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutCubic
    """
    return (t - 1) * (t - 1) * (t - 1) + 1


def CubicEaseInOut(t: float) -> float:
    """
    三次方缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutCubic
    """
    if t < 0.5:
        return 4 * t * t * t
    p = 2 * t - 2
    return 0.5 * p * p * p + 1


def QuarticEaseIn(t: float) -> float:
    """
    四次方缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInQuart
    """
    return t * t * t * t


def QuarticEaseOut(t: float) -> float:
    """
    四次方缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutQuart
    """
    return (t - 1) * (t - 1) * (t - 1) * (1 - t) + 1


def QuarticEaseInOut(t: float) -> float:
    """
    四次方缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutQuart
    """
    if t < 0.5:
        return 8 * t * t * t * t
    p = t - 1
    return -8 * p * p * p * p + 1


def QuinticEaseIn(t: float) -> float:
    """
    五次方缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInQuint
    """
    return t * t * t * t * t


def QuinticEaseOut(t: float) -> float:
    """
    五次方缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutQuint
    """
    return (t - 1) * (t - 1) * (t - 1) * (t - 1) * (t - 1) + 1


def QuinticEaseInOut(t: float) -> float:
    """
    五次方缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutQuint
    """
    if t < 0.5:
        return 16 * t * t * t * t * t
    p = (2 * t) - 2
    return 0.5 * p * p * p * p * p + 1


# 正弦函数无在线演示
# 见源代码
# https://github.com/semitable/easing-functions/blob/master/easing_functions/easing.py


def SineEaseIn(t: float) -> float:
    """
    正弦缓入函数
    ---
    doc:
    """
    return math.sin((t - 1) * math.pi / 2) + 1


def SineEaseOut(t: float) -> float:
    """
    正弦缓出函数
    ---
    doc:
    """
    return math.sin(t * math.pi / 2)


def SineEaseInOut(t: float) -> float:
    """
    正弦缓入+缓出函数
    ---
    doc:
    """
    return 0.5 * (1 - math.cos(t * math.pi))


def CircularEaseIn(t: float) -> float:
    """
    圆形曲线缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInCirc
    """
    return 1 - math.sqrt(1 - (t * t))


def CircularEaseOut(t: float) -> float:
    """
    圆形曲线缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutCirc
    """
    return math.sqrt((2 - t) * t)


def CircularEaseInOut(t: float) -> float:
    """
    圆形函数缓出+缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInOutCirc
    """
    if t < 0.5:
        return 0.5 * (1 - math.sqrt(1 - 4 * (t * t)))
    return 0.5 * (math.sqrt(-((2 * t) - 3) * ((2 * t) - 1)) + 1)


def ExponentialEaseIn(t: float) -> float:
    """
    指数缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInExpo
    """
    if t == 0:
        return 0
    return math.pow(2, 10 * (t - 1))


def ExponentialEaseOut(t: float) -> float:
    """
    指数缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutExpo
    """
    if t == 1:
        return 1
    return 1 - math.pow(2, -10 * t)


def ExponentialEaseInOut(t: float) -> float:
    """
    指数缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutExpo
    """

    if t == 0 or t == 1:
        return t

    if t < 0.5:
        return 0.5 * math.pow(2, (20 * t) - 10)
    return -0.5 * math.pow(2, (-20 * t) + 10) + 1


def ElasticEaseIn(t: float) -> float:
    """
    超限弹性缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInElastic
    """
    return math.sin(13 * math.pi / 2 * t) * math.pow(2, 10 * (t - 1))


def ElasticEaseOut(t: float) -> float:
    """
    超限弹性缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutElastic
    """
    return math.sin(-13 * math.pi / 2 * (t + 1)) * math.pow(2, -10 * t) + 1


def ElasticEaseInOut(t: float) -> float:
    """
    超限弹性缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutElastic
    """
    if t < 0.5:
        return (
            0.5 * math.sin(13 * math.pi / 2 * (2 * t)) * math.pow(2, 10 * ((2 * t) - 1))
        )
    return 0.5 * (
        math.sin(-13 * math.pi / 2 * ((2 * t - 1) + 1)) * math.pow(2, -10 * (2 * t - 1))
        + 2
    )


def BackEaseIn(t):
    """
    超限回弹缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInBack
    """
    return t * t * t - t * math.sin(t * math.pi)


def BackEaseOut(t):
    """
    超限回弹缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutBack
    """
    p = 1 - t
    return 1 - (p * p * p - p * math.sin(p * math.pi))


def BackEaseInOut(t):
    """
    超限回弹缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutBack
    """
    if t < 0.5:
        p = 2 * t
        return 0.5 * (p * p * p - p * math.sin(p * math.pi))

    p = 1 - (2 * t - 1)

    return 0.5 * (1 - (p * p * p - p * math.sin(p * math.pi))) + 0.5


def BounceEaseIn(t):
    """
    反弹缓入函数
    ---
    doc:https://easings.net/zh-cn#easeInBounce
    """
    return 1 - BounceEaseOut().func(1 - t)


def BounceEaseOut(t):
    """
    反弹缓出函数
    ---
    doc:https://easings.net/zh-cn#easeOutBounce
    """
    if t < 4 / 11:
        return 121 * t * t / 16
    elif t < 8 / 11:
        return (363 / 40.0 * t * t) - (99 / 10.0 * t) + 17 / 5.0
    elif t < 9 / 10:
        return (4356 / 361.0 * t * t) - (35442 / 1805.0 * t) + 16061 / 1805.0
    return (54 / 5.0 * t * t) - (513 / 25.0 * t) + 268 / 25.0


def BounceEaseInOut(t):
    """
    反弹缓入+缓出函数
    ---
    doc:https://easings.net/zh-cn#easeInOutBounce
    """
    if t < 0.5:
        return 0.5 * BounceEaseIn(t * 2)
    return 0.5 * BounceEaseOut(t * 2 - 1) + 0.5


if __name__ == "__main__":
    print(ExponentialEaseOut(1))
