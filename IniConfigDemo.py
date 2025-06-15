from IniConfig import IniConfig

# 创建 IniConfig 实例，传入配置文件路径
config_path = "config.ini"
config = IniConfig(config_path)

# 获取所有部分
sections = config.get_sections()
print("所有部分：", sections)

# 获取某个部分的键值对
dashscope_config = config.get_items_in_section("dashscope")
print("dashscope 配置：", dashscope_config)

# 获取特定键的值
server_ip = config.get_value("demo-Server", "ip")
print("服务器 IP 地址：", server_ip)  # 输出：192.168.1.1

# 获取布尔类型的值
debug_mode = config.get_boolean("demo-Server", "debug_mode")
print("调试模式：", debug_mode)  # 输出：True

# 获取整数类型的值
max_connections = config.get_integer("demo-Server", "max_connections")
print("最大连接数：", max_connections)  # 输出：50