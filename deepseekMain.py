import requests

# 基础初始化设置
base_url = "http://localhost:11434/api"
headers = {
    "Content-type": "application/json"
}

class DeepSeekR1:
    def __init__(self):
        print("DeepSeekR1 initialized!")

    def generate_completion(self,prompt, model):
        url = f"{base_url}/generate"
        data = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json().get('response', '')

    def generate_completion_stream(self,prompt, model):
        url = f"{base_url}/generate"
        data = {
            "model": model,
            "prompt": prompt,
            "stream": True
        }
        response = requests.post(url, headers=headers, json=data, stream=True)
        result = ""
        for line in response.iter_lines():
            if line:
                result += line.decode('utf-8')
        return result

    def generate_chat_completion(self,messages, model):
        url = f"{base_url}/chat"
        data = {
            "model": model,
            "messages": messages,
            "stream": False
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json().get('message', {}).get('content', '')

    def generate_embeddings(self,text, model):
        url = f"{base_url}/embed"
        data = {
            "model": model,
            "input": text
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def list_local_models(self):
        url = f"{base_url}/tags"
        response = requests.get(url, headers=headers)
        return response.json().get('models', [])

    def show_model_info(self,model):
        url = f"{base_url}/show"
        data = {"name": model}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def create_model(self,model_name,model):
        url = f"{base_url}/create"
        data = {
            "model": model_name,
            "from": model,
            "system": "You are a helpful assistant."
        }
        response = requests.post(url, headers=headers, json=data)
        return response.text

    def pull_model(self,model):
        url = f"{base_url}/pull"
        model = "qwen2.5:32b"
        data = {"name": model}
        response = requests.post(url, headers=headers, json=data)
        return response.text

    def delete_model(self,model):
        url = f"{base_url}/delete"
        data = {"name": model}
        response = requests.delete(url, headers=headers, json=data)
        return response.text



# 主程序
if __name__ == "__main__":
    # 创建 DeepSeekR1 类的实例
    deepseekr1 = DeepSeekR1()
    model = "deepseek-r1:32b"
    model_name = "my_deepseekr1"

    # 生成文本补全调用
    completion = deepseekr1.generate_completion("介绍一下人工智能。",model)
    print("生成文本补全:", completion)

    # 流式生成文本补全调用
    stream_completion = deepseekr1.generate_completion_stream("讲解机器学习的应用。",model)
    print("流式生成文本补全:", stream_completion)

    # 生成对话补全调用
    messages = [
        {"role": "user", "content": "什么是自然语言处理？"},
        {"role": "assistant", "content": "自然语言处理是人工智能的一个领域，专注于人与计算机之间的自然语言交互。"}
    ]
    chat_response = deepseekr1.generate_chat_completion(messages,model)
    print("生成对话补全:", chat_response)

    # 生成文本嵌入调用
    embeddings = deepseekr1.generate_embeddings("什么是深度学习？",model)
    print("生成文本嵌入:", embeddings)

    # 模型的增删改查
    ## 列出本地模型
    local_models = deepseekr1.list_local_models()
    print("列出本地模型:", local_models)
    ## 查看模型信息
    model_info = deepseekr1.show_model_info(model)
    print("模型信息:", model_info)
    ## 创建模型
    create_response = deepseekr1.create_model(model_name,model)
    print("创建模型:", create_response)
    ## 拉取模型
    pull_response = deepseekr1.pull_model(model)
    print("拉取模型:", pull_response)
    ## 删除模型
    delete_response = deepseekr1.delete_model(model_name)
    print("删除模型:", delete_response)
