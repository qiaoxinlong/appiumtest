#coding=utf-8
import os
class DosCmd:
	def excute_cmd_result(self,command):
		result_list = []
		result = os.popen(command).readlines()
		for i in result:
			if i =='\n':
				continue
			result_list.append(i.strip('\n'))
		return result_list

	def excute_cmd(self,command):
		os.system(command)
