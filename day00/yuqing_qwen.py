import dashscope
from getAPI import read_config

# 从配置文件读取 API 密钥
api_key = read_config("dashscope", "api_key")
if not api_key:
    raise ValueError("无法从配置文件读取 API 密钥")

# 设置 API 密钥
dashscope.api_key = api_key

# 封装模型响应函数
def get_response(param_messages):
    try:
        llm_response = dashscope.Generation.call(
            model='qwen-plus',
            messages=param_messages,
            result_format='message'  # 将输出设置为message形式
        )
        return llm_response
    except Exception as e:
        print(f"调用模型时发生错误: {e}")
        return None
    
review = '这款音效特别好,能给你意想不到的音质，这你也信？！'
messages=[
    {"role": "system", "content": "你是一名舆情分析师，帮我判断产品口碑的正负向，回复请用一个词语：正向 或者 负向"},
    {"role": "user", "content": review}
]

response = get_response(messages)
if response and response.output:
    print(response.output.choices[0].message.content)
else:
    print("无法获取模型响应")