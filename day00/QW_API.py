import dashscope

from getAPI import read_config

dashscope.api_key = read_config("dashscope", "api_key")

# 调用模型（例如通义千问）
response = dashscope.Generation.call(
    model="qwen-max",
    prompt="你好，今天过得怎么样？"
)

print(response.output.text)
