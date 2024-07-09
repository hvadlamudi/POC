from langchain.chains.llm import LLMChain
from langchain import OpenAI
# from langchain import OpenAI
from langchain.chains import ConversationChain
# from langchain_openai import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain
# from openai import OpenAI
from langchain.prompts import PromptTemplate

import prompts.prompts

# loaded_prompt = load_prompt("prompts/ETRM_prompt_tcode_test.json")
loaded_prompt = prompts.prompts.prompt

def generate_test(Tcode, VendorName):
    # llm = OpenAI(temperature=0.9)
    llm = OpenAI(temperature=0.9, max_tokens=4000)
    prompt_template_saptestgen_team = PromptTemplate(input_varibles=['Tcode', 'VendorName'],
                                                     template="as an SAP expert, genearte  positive and negative testcase with Testcase ID, Testcase title, Test case description, Expected result, actual results, Test data and prerequisite in excel format.")
    saptestgenChain = LLMChain(llm=llm, prompt=prompt_template_saptestgen_team)
    response = saptestgenChain({'Tcode': Tcode, 'VendorName': VendorName})
    return response

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

        response = completion.choices[0].message.content
        return response
    except Exception as e:
        print(e)
        pass

def generate_test_prompt_hari(format_prompt, question = None, session_id=""):
    # prompt_template_saptestgen_team = PromptTemplate.from_template(format_prompt)
    try:
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        question = question if question else "What is the pi value? output should be in table formate with 2 columns they are value and remarks."
        prompt = PromptTemplate(input_variables=["history", "input"], template=format_prompt)
        memory = ConversationBufferMemory()
        conversation_with_kg = ConversationChain(
            llm=client,
            verbose=True,
            prompt=prompt,
            memory=memory
        )


        # response = completion.choices[0].message.content
        response = conversation_with_kg.predict(input=question)
        print(f"AI Response:::: {response}")
        # print(conversation_with_kg.memory.kg)
        # print(conversation_with_kg.memory.kg.get_triples())
        return response
    except Exception as e:
        print(e)
        pass

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
