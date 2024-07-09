import os
from langchain.chains.llm import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import load_prompt
import pandas as pd

llm = OpenAI(temperature=0.9, max_tokens=4000, model="gpt-3.5-turbo-instruct")
# text = "as an SAP expert, genearte  positive and negative testcase with Testcase ID, Testcase title, Test case description, Expected result, actual results, Test data and prerequisite in excel format."
# print(llm(text))
format_Prompt = """ 
you are SAP expert, you will be given a transaction code {transactioncode} and  Transaction name {transactionname} to generate positive and Negative testcases for an oil and gas company"

Context:
Test cases are basically steps to validate the functionality of the given transactions code in the SAP system

Output Instructions:
your output should be a markdown table with the following column names
Testcase ID , Testcase title , Test case description , Expected result , actual results , Test data , prerequisite , screenshot
"""
prompt_template_saptestgen_team = PromptTemplate(input_varibles=['Tcode', 'VendorName'], template=format_Prompt)
# print(prompt_template_saptestgen_team.format(Tcode='MN21'))
# print(llm(prompt_template_saptestgen_team.format(Tcode='MN21', VendorName='aramco')))
prompt_template_saptestgen_team.save("prompts/ETRM_prompt_tcode.json")
loaded_prompt = load_prompt("prompts/ETRM_prompt_tcode.json")
# print(loaded_prompt.format(Tcode='MN21', VendorName='aramco'))
# print(llm(loaded_prompt.format(Tcode='MN21', VendorName='aramco')))
outcome_testcase = llm(loaded_prompt.format(Tcode='MN21', VendorName='aramco'))
print(outcome_testcase)
df=pd.DataFrame.from_dict(outcome_testcase)
df.show

# from langchain_community.llms import
#
# class Config:
#  def __init__(self, temperature, max_tokens, frequency_penalty):
#      self.temperature = temperature
#      self.max_tokens= max_tokens
#      self.frequency_penalty= frequency_penalty
# #
# # llm = Ollama(model="llama2:13b-chat-q4_K_M")
# prompt_config = Config(0.9, 64, 0.5)

# Something like this
# print(llm.invoke(prompt="Hello what is your name?"), config=prompt_config)