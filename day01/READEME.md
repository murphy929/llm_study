# LLM 学习笔记 - Day01

## 课程综合

### API申请与本地配置

#### 1. env文件

.env 文件的结构像这样： KEY=VALUE ，每一行一个变量。比如：

```env
DB_USER=root
DB_PASSWORD=secret
```

在使用时需加载 .env 文件。可以使用 Python 的 dotenv 模块来实现。

```python
# 引入 dotenv 模块
from dotenv import load_dotenv, find_dotenv
# 加载 .env 到环境变量
_ = load_dotenv(find_dotenv())

```

它存在的主要目的是为了管理应用的配置信息，提高安全性和灵活性。通过它可以轻松地根据不同环境调整配置，而不需要修改代码，从而提高开发效率。同时也因为键值对的缘故，导致它无法维护管理同一接口不同实现的同键值名变量，那么都是 api_key 就需要使用不同的变量名，比如 api_key_a 和 api_key_b ，这样会导致变量名过长或数量膨胀，不方便管理使用。而 config.ini 文件则可以解决这个问题,因为 ini 文件支持分区键值对，也即允许不同分区下的变量名是相同的，所以 api_key 只需要一个变量名，就可以实现不同实现同键值名变量的维护。

#### 2. config.ini文件

`ini`文件的格式如下：

```ini
[section_interface_1]
api_key = sk-1234567890

[section_interface_2]
api_key = sk-abcdefghijklmnopqrstuvwxyz

```

使用 Python 的 configparser 模块来读取 ini 文件：

```python
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['section_interface_1']['api_key']
```

#### 使用socks5代理访问openai

由于众所周知的原因，我们只能使用科学上网使用openai提供的大模型，这里以socks5为例，给出openai配置socks5的代码示例。配置使用它之前
需要安装相应软件`pip install openai requests[socks]`。

```python
# 使用 socks5h 而不是 socks5（让域名解析走代理）
socks5_proxy = "socks5h://127.0.0.1:1080"
# 设置 SOCKS5 代理（使用环境变量）
os.environ['HTTP_PROXY'] = socks5_proxy
os.environ['HTTPS_PROXY'] = socks5_proxy
```

### 使用不同的API调用方式实现模型调用

1. OpenAI[翻墙直连]

[env_demo.py](./env_demo.py)

2. 代理OpenAI[devagi]

3. 三方平台[dashscope]

4. 本地Ollama

### 几个调用案例

**1. 普通聊天型**  
对大模型输入输出内容均不限制，用于聊天型场景。

**2. 结果约束型**  
对大模型输入内容不做限制，但对返回内容做枚举性限制，类似于在候选标签中对输入进行打标分类。

**3. 函数调用型**  
对大模型输入输出均限制，指定具体的入参、出参格式，有时也包括内容的限制，它主要用作函数调用，即输入内容是函数调用，输出内容是函数返回值。
