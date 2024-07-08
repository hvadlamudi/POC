from sap.module.llm.SAPLLM import SAPLLM


class LLMConfig:
    def __init__(self, model_settings):
        self.llm = None
        if model_settings:
            self.model = model_settings['model']
            self.token_limit = model_settings['token_limit']
            self.temperature = model_settings['temperature']
            self.topp = model_settings['topp']
            self.topk = model_settings['topk']

            self._load_module(model=self.model, token_limit = self.token_limit, temperature = self.temperature, topp = self.topp, topk = self.topk)

    def _load_module(self, model="Dummy Mode", token_limit=1024, temperature=0.7, topp=0.8, topk=40):
        self.llm = SAPLLM(model=model,token_limit=token_limit,temperature=temperature, topp=topp, topk=topk)
