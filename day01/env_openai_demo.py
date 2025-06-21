# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

# 使用os库来访问环境变量
import os

socks5_proxy = "socks5h://127.0.0.1:1080"
# 设置 SOCKS5 代理（使用环境变量）
os.environ['HTTP_PROXY'] = socks5_proxy
os.environ['HTTPS_PROXY'] = socks5_proxy

# 配置 OpenAI 服务  
client = OpenAI()

response = client.chat.completions.create(
    messages = [
        {"role": "system", "content": "你是一个擅长玩中文互联网上网络梗的高手。"},
        {"role": "user", "content": "你能给我讲一个梗吗？"},
    ],
    max_tokens=100,
    temperature=0.7,
    # top_p=1,
    # n=1,
    # stop=None,
    # user="",
    stream=False,
    # logit_bias=None,
    # presence_penalty=0.0,
    # frequency_penalty=0.0,
    # best_of=1,
    model="gpt-4.1-mini",
)

print(response)

print(response.choices[0].message.content)  # 更具体的的打印
