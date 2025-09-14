import dashscope
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)  # 添加上级目录到 sys.path

import IniConfig
config_path = "config.ini"
config = IniConfig.IniConfig(config_path)

# 从配置文件读取 API 密钥
dashscope.api_key = config.get_value("dashscope", "api_key")

# 调用模型（例如通义千问）
response = dashscope.Generation.call(
    model="qwen-max",
    prompt="你好，今天过得怎么样？",
    stream=False  # 明确指定非流式响应
)

# 打印模型的响应文本
print(response.output.text)