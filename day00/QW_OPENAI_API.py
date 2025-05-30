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
        ChatCompletionSystemMessageParam(role="system", content="You are a helpful assistant."),
        ChatCompletionAssistantMessageParam(role="assistant", content="我是个有用的智能助手。"),
        ChatCompletionUserMessageParam(role="user", content="你是谁？"),
        ChatCompletionUserMessageParam(role="user", content="我是Murphy？"),
        ChatCompletionUserMessageParam(role="user", content="你知道我是谁吗？")
    ]
    completion = client.chat.completions.create(
        model="qwen3-235b-a22b",  # 此处以qwen3-235b-a22b为例，可按需更换模型名称
        messages=messages,
        # max_tokens=100,
        # temperature=0.7,
        # top_p=1,
        # n=1,
        # stop=None,
        # user="",
        # stream=False,
        # logit_bias=None,
        # presence_penalty=0.0,
        # frequency_penalty=0.0,
        # best_of=1,
    )

    print(completion.model_dump_json())

if __name__ == '__main__':
    get_response()