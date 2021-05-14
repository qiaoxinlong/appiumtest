import logging
import os
import datetime
class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        base_path = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_path, "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = log_dir + "/" + log_file
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.DEBUG)
        formater = logging.Formatter(
            '%(asctime)s  %(filename)s  %(funcName)s  %(levelname)s  %(message)s - - -> %(message)s')
        self.file_handle.setFormatter(formater)
        self.logger.addHandler(self.file_handle)
        # self.logger.debug("test1234")
    def get_log(self):
       return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)
