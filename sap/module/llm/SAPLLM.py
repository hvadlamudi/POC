from openai import OpenAI


class SAPLLM:
    def __init__(self, model ,token_limit, temperature, topp, topk):
        self.model = model
        self.token_limit = token_limit
        self.temperature = temperature
        self.topp = topp
        self.topk = topk

    def query_llm(self, question=""):
        try:
            client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
            question = question if question else "What is the pi value? output should be in table formate with 2 columns they are value and remarks."
            completion = client.chat.completions.create(
                model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
                messages=[
                    {"role": "system",
                     "content": "Your a responsible kind and helpful AI to answer below user questions."},
                    {"role": "user", "content": question}
                ],
                temperature=0.7,
            )

            response = completion.choices[0].message.content
            return response
        except Exception as e:
            print(e)
            pass