import os
from langchain.chains.llm import LLMChain
# from langchain.llms import OpenAI
from openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import load_prompt
# from langchain_openai import OpenAI
import pandas as pd

os.environ["OPENAI_API_KEY"] = "sk-proj-Hqspghoh2kse2TwIM8PxT3BlbkFJdiS3VpfEszU1wr96JJou"
# llm = OpenAI(temperature=0.9)
# # text = "as an SAP expert, genearte  positive and negative testcase with Testcase ID, Testcase title, Test case description, Expected result, actual results, Test data and prerequisite in excel format."
# # print(llm(text))
# prompt_template_saptestgen_team = PromptTemplate(input_varibles=['Tcode', 'VendorName'],
#                                                  template="as an SAP expert, genearte  positive and negative testcase with Testcase ID, Testcase title, Test case description, Expected result, actual results, Test data and prerequisite in excel format.")
# print(prompt_template_saptestgen_team.format(Tcode='MN21'))
# # print(llm(prompt_template_saptestgen_team.format(Tcode='MN21', VendorName='aramco')))
# prompt_template_saptestgen_team.save("ETRM_prompt.json")
# loaded_prompt = load_prompt("prompts/ETRM_prompt_tcode.json") #ETRM_prompt.json
loaded_prompt = load_prompt("prompts/ETRM_prompt_tcode_test.json")


# print(loaded_prompt.format(Tcode='MN21', VendorName='aramco'))
# print(llm(loaded_prompt.format(Tcode='MN21', VendorName='aramco')))

def generate_test(Tcode, VendorName):
    # llm = OpenAI(temperature=0.9)
    llm = OpenAI(temperature=0.9, max_tokens=4000)
    prompt_template_saptestgen_team = PromptTemplate(input_varibles=['Tcode', 'VendorName'],
                                                     template="as an SAP expert, genearte  positive and negative testcase with Testcase ID, Testcase title, Test case description, Expected result, actual results, Test data and prerequisite in excel format.")
    saptestgenChain = LLMChain(llm=llm, prompt=prompt_template_saptestgen_team)
    response = saptestgenChain({'Tcode': Tcode, 'VendorName': VendorName})
    return response


# print(generate_test(Tcode='MN21', VendorName='aramco'))

def generate_test_prompt(Transaction_code, Transaction_Name, format_prompt):
    # llm = OpenAI(temperature=0.9)
    # llm = OpenAI(temperature=0.9, max_tokens=3900, model = "gpt-4-turbo")
    llm = OpenAI(temperature=0.9, max_tokens=3900, model="gpt-3.5-turbo-instruct")
    # format_prompt = "as an SAP expert, genearte  positive and negative testcase with Testcase ID, Testcase title, Test case description, Expected result, actual results, Test data and prerequisite in excel format."
    prompt_template_saptestgen_team = PromptTemplate(input_varibles=['Transaction_code', 'Transaction_Name'],
                                                     template=format_prompt)
    saptestgenChain = LLMChain(llm=llm, prompt=prompt_template_saptestgen_team)
    response = saptestgenChain({'Transaction_code': Transaction_code, 'Transaction_Name': Transaction_Name})
    return response


def generate_test_prompt_vasu(Transaction_code, Transaction_Name, format_prompt, question=None, session_id=""):
    prompt_template_saptestgen_team = PromptTemplate.from_template(format_prompt)

    # Point to the local server
    try:
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        question = question if question else "What is the pi value? output should be in table formate with 2 columns they are value and remarks."
        completion = client.chat.completions.create(
            model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
            messages=[
                {"role": "system", "content": "Your a responsible kind and helpful AI to answer below user questions."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
        )

        response=completion.choices[0].message.content
        return response
    except Exception as e:
        print(e)
        pass


# print(generate_test_prompt(Tcode='MN21', VendorName='aramco', format_prompt=loaded_prompt.format(Tcode='MN21', VendorName='aramco')))
def generate_test_prompt_templates(format_prompt):
    # llm = OpenAI(temperature=0.9)
    llm = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
    # llm = OpenAI(temperature=0.9, max_tokens=3900, model="gpt-4-turbo")
    prompt_template_saptestgen_team = PromptTemplate(template=format_prompt)
    saptestgenChain = LLMChain(llm=llm, prompt=prompt_template_saptestgen_team)
    # response = saptestgenChain({}) # string response
    response = saptestgenChain({}).items()
    # return (pd.DataFrame.from_dict(response)) # dict response
    return response

# https://www.youtube.com/watch?v=5qP6u-WGSPk
# print(generate_test_prompt_templates(format_prompt=loaded_prompt.format(Tcode='MN21', VendorName='aramco')))
