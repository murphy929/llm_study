# 引入dotenv库来读取.env文件
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

# 使用os库来访问环境变量
import os

socks5_proxy = "socks5h://127.0.0.1:1080"
# 设置 SOCKS5 代理（使用环境变量）
os.environ['HTTP_PROXY'] = socks5_proxy
os.environ['HTTPS_PROXY'] = socks5_proxy

import openai

# 设置API密钥
openai.api_key = os.environ.get('OPENAI_API_KEY')

from openai import OpenAI
# 创建 OpenAI 客户端实例
client = OpenAI()

# 获取模型列表
model_list = client.models.list()

print(model_list)