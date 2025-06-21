from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam, \
    ChatCompletionAssistantMessageParam

from getAPI import read_config


def get_response():
    client = OpenAI(
        api_key=read_config("dashscope", "api_key"),
        base_url=read_config("dashscope", "base_url"),  # 填写DashScope SDK的base_url
    )
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": "我是个有用的智能助手。"},
        {"role": "user", "content": "你知道我是谁吗？"},
        {"role": "assistant", "content": "你是谁？"},
        {"role": "user", "content": "我是Murphy？"}
    ]
    completion = client.chat.completions.create(
        model="qwen3-235b-a22b", # 使用DashScope的模型名称
        messages=messages,
        # max_tokens=100,
        # temperature=0.7,
        # top_p=1,
        # n=1,
        # stop=None,
        # user="",
        stream=False,
        # logit_bias=None,
        # presence_penalty=0.0,
        # frequency_penalty=0.0,
        # best_of=1,
        extra_body={
            "enable_thinking": False 
        }
    )

    print(completion.model_dump_json())
    print(completion.choices[0].message.content)  # 更具体的的打印

if __name__ == '__main__':
    get_response()