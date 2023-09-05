'''
桥接层
通过分析原GUI文件自动生成新GUI-class
import 方式分析事件/子类
文本分析方式查找__init__局域变量,这通常是sizer
'''

import wx,wx.core
import importlib

import cuwx

def main(module_name):
	GUI_module = importlib.import_module(module_name) #依据提供的模块名进行导入，以适应不同GUI文件的桥接工作
	path = './' + GUI_module.__name__ + '.py' #默认处在同一目录中
	
	class Main(GUI_module.Main):
		def __init__(self, parent):
			super().__init__(parent)

			sizer_line,sizer_def,sizer_do,sizer_name,sizer_structure = self.Analyze(path)
			self.__Remove_Class_Children()

			#TODO:依据结构表重构新子项


		def list_instance_variables(self):  
			"""
			返回该类中所有实例变量>>self.XX
			---
			arg:None
			return:list
			"""
			instance_variables = [attr for attr in dir(self) if not attr.startswith('__')]  
			instance_variables = [attr for attr in instance_variables if not callable(getattr(type(self), attr, None))]  
			instance_variables = [attr for attr in instance_variables if not attr.startswith('__')]  
			instance_variables = [attr for attr in instance_variables if not hasattr(type(self), attr)]  
			return instance_variables  

		def __Remove_Class_Children(self):	
			'''
			删除子项
			---
			arg:None
			return:None
			'''
			child_classlist = []
			print(self.list_instance_variables())
			for i in self.list_instance_variables():
				child_classlist.append(eval('self.' + i))

			child_wxlist = self.GetChildren()
			for i in child_wxlist:
				for ia in child_classlist:
					if i == ia:
						print(1)

		def Analyze(self, path):
			"""
			打开GUI文件并开始分析
			---
			arg:
				path : str -> 文件路径
			doc:
				wx.Sizer命名以Sizer开头
				针对wxFormBuilder (version 3.10.1-0-g8feb16b3)
			"""

			#TODO:扩展分析范围到所有控件，而不只是sizer

			with open(path, 'r') as data:
				#Step:过滤无关字符
				data_Dec = [] #过滤后代码行list
				for i in data.readlines():
					i = i.replace('\n','')
					i = i.replace('\t','')
					if i == '':
						pass
					elif i[0] == '#':
						pass
					elif 'import' in i:
						pass
					elif 'class' in i:
						pass
					elif 'def' in i:
						pass
					else:
						data_Dec.append(i)

			print('GUI有效行数:', len(data_Dec))

			#Step:提取包含"sizer"的所有行
			sizer_line = []
			for i in data_Dec:
				if 'Sizer' in i:
					sizer_line.append(i)

			#Step:提取所有sizer定义/操作
			sizer_def = []
			sizer_do = []
			for i in sizer_line:
				if '=' in i:
					sizer_def.append(i)
				else:
					sizer_do.append(i)
			
			sizer_do.pop() #删除最后一项，这通常是self.SetSizer( SizerMain )

			#Step:提取sizer名字
			sizer_name = []
			for i in sizer_def:
				sizer_name.append(i[0:i.find('=') - 1])

			#Step:提取sizer嵌套结构
			# --->sizer_structure[]
			#	|--->sizer_name[]
			#		|--->sizer_do[]
			#			|--->arg''
			#
			sizer_structure = []
			for i in sizer_name:
				sizer_structure.append([])

			
			for i in sizer_do:
				count = 0 #计数器
				for ia in sizer_name:
					if ia in i:
						target = sizer_structure[count]
						info = i
						info = info[info.find('Add') + 5:-2].replace(' ','').split(',')
						##print(info)
						target.append(info)
						break

					count = count + 1
			print('分析完成')
			return sizer_line,sizer_def,sizer_do,sizer_name,sizer_structure

			
	return Main



if __name__ == "__main__":
	main(module_name = 'GUI_Base')