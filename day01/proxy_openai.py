# 导入os和sys模块以获取上级目录
import os
import sys

# 获取当前脚本所在目录的上级目录
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 添加到 sys.path
sys.path.append(parent_dir)

# 导入Inionfig模块
import IniConfig

# 创建 IniConfig 实例，传入配置文件路径
config_path = "config.ini"
config = IniConfig.IniConfig(config_path)

# 获取配置代理api信息
api_key =  config.get_value('devagi', 'api_key')
base_url = config.get_value('devagi', 'base_url')

# 设置代理API的基本URL
from openai import OpenAI
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

messages = [
    {"role": "system", "content": "你擅长讲适合3-6岁小朋友听的英语故事。"},
    {"role": "user", "content": "你能给我讲关于物归原处的故事吗？"}
]


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    max_tokens=100,
    temperature=0.7,
    stream=False
)

print(response.model_dump_json())
print(response.choices[0].message.content)  # 打印模型的响应内容