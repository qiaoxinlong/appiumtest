#coding=utf-8
from configparser import ConfigParser


class ReadIni:
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = '..\config\LocalElement.ini'
		else:
			self.file_path = file_path
		self.data = self.read_ini()
	def read_ini(self):
		read_ini = ConfigParser()
		# with open(self.file_path, 'r', encoding='UTF-8') as f:
		# 	f.read()
		read_ini.read(self.file_path,encoding='UTF-8')
		return read_ini

	#通过key获取对应的value
	def get_value(self,key,section=None):
		if section == None:
			section = 'Community'
		try:
			value = self.data.get(section,key)		
		except:
			value = None
		return value

