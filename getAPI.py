import configparser

def read_config(file_path, section, option):
    """
    Reads a value from an INI configuration file.

    :param file_path: Path to the INI file.
    :param section: Section in the INI file.
    :param option: Option within the section to retrieve.
    :return: Value of the specified option, or None if not found.
    """
    config = configparser.ConfigParser()
    try:
        # 读取INI文件
        config.read(file_path)
        # 判断指定section和option是否存在
        if config.has_section(section) and config.has_option(section, option):
            # 返回指定option的值
            return config.get(section, option)
        else:
            # 如果不存在，返回None
            return None
    except Exception as e:
        # 打印错误信息
        print(f"Error reading config file: {e}")
        # 返回None
        return None


def read_config(section, option):
    file_name = "config.ini"
    return read_config(file_name, section, option)