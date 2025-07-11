
from openai import OpenAI
import json

# 配置 OpenAI 本地接口
client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:7777/v1"
)

# 加载问题列表
with open("LLM/test/questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)
results = []
# 向模型逐条提问并打印结果
for i, question in enumerate(questions, 1):
    response = client.completions.create(
        model="vicuna-7b-v1.5-16k",
        prompt=question,
        max_tokens=512,
        temperature=0.7
    )
#     print(f"\n==== 问题 {i} ====\n{question}\n")
#     print("回答：", response.choices[0].text.strip())

    answer = response.choices[0].text.strip()
    results.append({"question": question, "answer": answer})

with open("LLM/test/qa_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)