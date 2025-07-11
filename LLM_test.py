# #beam search方式测试样例
# from vllm import LLM
# from vllm.sampling_params import BeamSearchParams
# import time

# llm = LLM(
#     model="vicuna-7b-v1.5-16k", 
#     max_model_len = 4096,
# )

# print("model load success!")

# beam_params = BeamSearchParams(beam_width=4, max_tokens=100)

# prompts = [
#     "你是谁？",
#     "你好"
# ]

# outputs = llm.beam_search(prompts, beam_params)

# for output in outputs:
#     print(len(output.sequences))
#     print(output.sequences[0].text)
#********************************************************************************************************
# sampling方式测试样例
# from vllm import LLM, SamplingParams

# prompts = [
#     "Hello, my name is",
#     "The president of the United States is",
#     "The capital of France is",
#     "The future of AI is",
# ]
# sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

# llm = LLM(model="/home/zqm/LLM/model_LLM")

# outputs = llm.generate(prompts, sampling_params)

# for output in outputs:
#     prompt = output.prompt
#     generated_text = output.outputs[0].text
#     print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

#********************************************************************************************************
#openai api测试样例
from openai import OpenAI

# 设置 API 访问地址和密钥（vLLM 默认使用 "EMPTY"）
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:7777/v1"  # 或 http://127.0.0.1:8000/v1

# 创建 OpenAI 客户端，指向本地 vLLM 服务
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
completion = client.completions.create(
    model="vicuna-7b-v1.5-16k",
    prompt="介绍下清华大学。",
    max_tokens=512
)


print(completion.choices[0].text)
