import json

questions = [
    "介绍下清华大学。",
    "什么是机器学习？",
    "深度学习和传统机器学习有什么区别？",
    "请用通俗语言解释什么是大语言模型（LLM）。",
    "介绍一下 Transformer 架构的基本原理。",
    "什么是监督学习和无监督学习？",
    "如何提高深度学习模型的泛化能力？",
    "图神经网络有哪些应用场景？",
    "什么是自然语言处理中的 attention 机制？",
    "请列举几个常用的开源大模型项目。"
]

# 保存到 JSON 文件
with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
