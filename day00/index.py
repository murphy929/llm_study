# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

# 配置 OpenAI 服务  

client = OpenAI()

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "讲个笑话",
        }
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
    model="gpt-3.5-turbo",
)

print(response)

print(response.choices[0].message.content)  # 更具体的的打印
