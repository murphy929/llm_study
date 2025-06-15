import configparser
import os

class IniConfig:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        # 检查文件是否存在
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"配置文件 {config_file} 不存在！")
        # 读取配置文件
        self.config.read(config_file)
    
    def get_sections(self):
        """获取所有部分（section）"""
        return self.config.sections()
    
    def get_items_in_section(self, section_name):
        """获取某个部分中的所有键值对"""
        if not self.config.has_section(section_name):
            raise ValueError(f"配置文件中没有部分 {section_name}！")
        items = {}
        for key, value in self.config.items(section_name):
            items[key] = value
        return items
    
    def get_value(self, section_name, key):
        """获取某个键的值"""
        if not self.config.has_section(section_name):
            raise ValueError(f"配置文件中没有部分 {section_name}！")
        if not self.config.has_option(section_name, key):
            raise KeyError(f"部分 {section_name} 中没有键 {key}！")
        return self.config.get(section_name, key)
    
    def get_boolean(self, section_name, key):
        """获取布尔类型的值"""
        return self.config.getboolean(section_name, key)
    
    def get_integer(self, section_name, key):
        """获取整数类型的值"""
        return self.config.getint(section_name, key)
    
    def get_float(self, section_name, key):
        """获取浮点数类型的值"""
        return self.config.getfloat(section_name, key)