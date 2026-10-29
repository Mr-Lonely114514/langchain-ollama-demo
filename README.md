# 基于 LangChain + Ollama 的极简问答助手

## 功能说明
调用本地离线大模型 qwen2:1.5b，接收用户问题并生成回答。无需联网调用 API，完全本地运行。

## 技术栈
- LangChain
- langchain-ollama
- Ollama（离线模型运行时）
- qwen2:1.5b 模型

## 运行方式
1. 安装 Ollama 并拉取模型：
   ollama pull qwen2:1.5b

2. 安装依赖：
   python -m pip install langchain langchain-ollama

3. 运行：
   python app.py

## 运行示例
输入问题后，程序输出：

我是来自AI的人工智能助手，专注于提供信息、帮助完成任务和解答问题。
<img width="461" height="30" alt="屏幕截图 2026-10-29 213240" src="https://github.com/user-attachments/assets/cf9ed9f7-dd49-4f04-99b0-4715dadc71d8" />
