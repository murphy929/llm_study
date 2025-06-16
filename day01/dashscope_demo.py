import dashscope
import IniConfig

config = IniConfig("config.ini")

# 从配置文件读取 API 密钥
dashscope.api_key = config.get_value("dashscope", "api_key")

# 调用模型（例如通义千问）
response = dashscope.Generation.call(
    model="qwen-max",
    prompt="你好，今天过得怎么样？"
)

print(response.output.text)
