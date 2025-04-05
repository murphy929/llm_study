from openai import OpenAI
from getAPI import read_config
import os

def get_response():
    client = OpenAI(
        api_key=read_config("dashscope", "api_key"),
        # api_key=os.getenv("DASHSCOPE_API_KEY"), # 如果您没有配置环境变量，请用百炼API Key将本行替换为：api_key="sk-xxx"
        base_url=read_config("dashscope", "base_url"),  # 填写DashScope SDK的base_url
    )
    completion = client.chat.completions.create(
        model="qwen-plus",  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': '你是谁？'}]
        )
    print(completion.model_dump_json())

if __name__ == '__main__':
    get_response()