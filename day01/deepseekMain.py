import requests

# 基础初始化设置
base_url = "http://localhost:11434/api"
headers = {
    "Content-type": "application/json"
}


class DeepSeek:
    def __init__(self, model, model_name):
        self.model = model
        self.model_name = model_name
        print(f"DeepSeek initialized with model: {model} and model_name: {model_name}!")

    def generate_completion(self, prompt):
        try:
            url = f"{base_url}/generate"
            data = {"model": self.model, "prompt": prompt, "stream": False}
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json().get('response', '')
        except Exception as e:
            return f"生成补全失败: {e}"

    def generate_completion_stream(self, prompt):
        try:
            url = f"{base_url}/generate"
            data = {"model": self.model, "prompt": prompt, "stream": True}
            response = requests.post(url, headers=headers, json=data, stream=True)
            response.raise_for_status()
            result = ""
            for line in response.iter_lines():
                if line:
                    result += line.decode('utf-8')
            return result
        except Exception as e:
            return f"流式生成失败: {e}"

    def generate_chat_completion(self, messages):
        try:
            url = f"{base_url}/chat"
            data = {"model": self.model, "messages": messages, "stream": False}
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json().get('message', {}).get('content', '')
        except Exception as e:
            return f"生成对话失败: {e}"

    def generate_embeddings(self, text):
        try:
            url = f"{base_url}/embed"
            data = {"model": self.model, "input": text}
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def list_local_models(self):
        try:
            url = f"{base_url}/tags"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json().get('models', [])
        except Exception as e:
            return f"获取本地模型失败: {e}"

    def show_model_info(self):
        try:
            url = f"{base_url}/show"
            data = {"name": self.model}
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return f"查看模型信息失败: {e}"

    def create_model(self):
        try:
            url = f"{base_url}/create"
            data = {
                "model": self.model_name,
                "from": self.model,
                "system": "You are a helpful assistant."
            }
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.text
        except Exception as e:
            return f"创建模型失败: {e}"

    def pull_model(self):
        try:
            url = f"{base_url}/pull"
            data = {"name": self.model}
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.text
        except Exception as e:
            return f"拉取模型失败: {e}"

    def delete_model(self):
        try:
            url = f"{base_url}/delete"
            data = {"name": self.model_name}
            response = requests.delete(url, headers=headers, json=data)
            response.raise_for_status()
            return response.text
        except Exception as e:
            return f"删除模型失败: {e}"


# 主程序
if __name__ == "__main__":
    model = "deepseek-r1:32b"
    model_name = "my_deepseek-r1"
    deepseek = DeepSeek(model, model_name)

    print("生成文本补全:", deepseek.generate_completion("介绍一下人工智能。"))
    print("流式生成文本补全:", deepseek.generate_completion_stream("讲解机器学习的应用。"))

    messages = [
        {"role": "user", "content": "什么是自然语言处理？"},
        {"role": "assistant", "content": "自然语言处理是人工智能的一个领域，专注于人与计算机之间的自然语言交互。"}
    ]
    print("生成对话补全:", deepseek.generate_chat_completion(messages))
    print("生成文本嵌入:", deepseek.generate_embeddings("什么是深度学习？"))

    print("列出本地模型:", deepseek.list_local_models())
    print("模型信息:", deepseek.show_model_info())
    print("拉取模型:", deepseek.pull_model())
    # print("创建模型:", deepseek.create_model())
    # print("删除模型:", deepseek.delete_model())
