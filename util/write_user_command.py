#coding=utf-8
import yaml
class WriteUserCommand:
	def read_data(self):
		'''
		加载yaml数据
		'''
		with open("../config/userconfig.yaml") as fr:
			data = yaml.load(fr)
		return data

	def get_value(self,key,port):
		'''
		获取value
		'''
		data = self.read_data()
		value = data[key][port]
		return value

	def write_data(self,i,device,bp,port):
		'''
		写入数据
		'''
		data = self.join_data(i,device,bp,port)
		with open("../config/userconfig.yaml","a") as fr:
			yaml.dump(data,fr)

	def join_data(self,i,device,bp,port):
		data = {
		"user_info_"+str(i):{
		"deviceName":device,
		"bp":bp,
		"port":port
		}
		}
		return data

	def clear_data(self):
		with open("../config/userconfig.yaml","w") as fr:
			fr.truncate()
		fr.close()

	def get_file_lines(self):
		data = self.read_data()
		return len(data)



