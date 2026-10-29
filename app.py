from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:1.5b")
response = llm.invoke("用一句话介绍你自己")
print(response)
