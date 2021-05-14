# coding=utf-8
from util.read_init import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        local = read_ini.get_value(key)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'ids':
                    return self.driver.find_elements_by_id(local_by)
                elif by == 'classNames':
                    return self.driver.find_elements_by_class_name(local_by)
                elif by == 'UiSelector':
                    return self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + local_by + '")'.replace("'", "'"))
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                # self.driver.save_screenshot("../jpg/test02.png")
                return None
        else:
            return None
