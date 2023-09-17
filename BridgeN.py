'''
桥接层
通过分析原GUI文件自动生成新GUI-class
与旧Bridge不同,这是一种新的实现思路,基于exec()
'''

import wx,wx.xrc
import cuwx

def Analyze(path):
	"""
	打开GUI文件并开始分析
	---
	arg:
		path : str -> 文件路径
	doc:
		wx.Sizer
		wx.Butt
		针对wxFormBuilder (version 3.10.1-0-g8feb16b3)
	"""

	with open(path, 'r',encoding='utf8') as data:
		#Step:过滤无关字符
		data_Dec = [] #过滤后代码行list
		for i in data.readlines():
			##i = i.replace('\n','')
			##i = i.replace('\t','')
			if i == '':
				pass
			elif i[0] == '#':
				pass
			else:
				data_Dec.append(i)



	print('GUI有效行数:', len(data_Dec))
	##print(data_Dec)

	#Step:对控件进行调换wx.XX -> cuwx.XX
	#TODO:支持更多控件的替换
	cun = 0
	for i in data_Dec:
		if 'Filter' in i and '=' in i:
			head = i[:i.find('=') + 2]
			bot = i[i.find('=') + 11:]
			mid = 'cuwx.Filter.FilterN'

			combin = head + mid + bot

			data_Dec[cun] = combin

		elif 'wx.ToggleButton' in i and '=' in i:
			head = i[:i.find('=') + 2]
			bot = i[i.find('=') + 17:]
			mid = 'cuwx.ToggleButton.ToggleButtonN'

			combin = head + mid + bot
			print(combin)

			data_Dec[cun] = combin
		
		elif 'wx.Button' in i and '=' in i:
			head = i[:i.find('=') + 2]
			bot = i[i.find('=') + 11:]
			mid = 'cuwx.Button.ButtonN'

			combin = head + mid + bot
			##print(combin)
			data_Dec[cun] = combin
		elif 'wx.CheckBox' in i and '=' in i:
			head = i[:i.find('=') + 2]
			bot = i[i.find('=') + 13:]
			mid = 'cuwx.CheckBox.CheckBoxN'
			

			combin = head + mid + bot

			data_Dec[cun] = combin


		cun = cun + 1

	##print(data_Dec)

	#Step:合并字符串
	a = ''
	for i in data_Dec:
		a = a + i

	return a

if __name__ == "__main__":
	Analyze('./GUI_Base.py')