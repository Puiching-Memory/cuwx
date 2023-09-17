'''
动画使用到的数学函数
---
https://github.com/semitable/easing-functions/blob/master/easing_functions/easing.py
https://blog.csdn.net/z2014z/article/details/120691794
'''

import math


def ExponentialEaseIn(t: float) -> float:
	'''
	指数缓入函数
	---
	doc:https://easings.net/zh-cn#easeInExpo
	'''
	if t == 0:
		return 0
	return math.pow(2, 10 * (t - 1))

def ExponentialEaseOut(t: float) -> float:
	'''
	指数缓出函数
	---
	doc:https://easings.net/zh-cn#easeOutExpo
	'''
	if t == 1:
		return 1
	return 1 - math.pow(2, -10 * t)


def ExponentialEaseInOut(t: float) -> float:
	'''
	指数缓入+缓出函数
	---
	doc:https://easings.net/zh-cn#easeInOutExpo
	'''

	if t == 0 or t == 1:
		return t

	if t < 0.5:
		return 0.5 * math.pow(2, (20 * t) - 10)
	return -0.5 * math.pow(2, (-20 * t) + 10) + 1




if __name__ == "__main__":
	print(ExponentialEaseOut(1))