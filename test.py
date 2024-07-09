from langchain_community.memory.kg import ConversationKGMemory
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate


llm = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does not know. The AI ONLY uses information contained in the "Relevant Information" section and does not hallucinate.

Relevant Information:

{history}

Conversation:
Human: {input}
AI:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

conversation_with_kg = ConversationChain(
    llm=llm,
    verbose=True,
    prompt=prompt,
    memory=ConversationKGMemory(llm=llm)
)
question = None
while question != 'QUIT':
    question = input("Enter your question here..QUIT to quit\n")
    print(f"AI Response: {conversation_with_kg.predict(input=question)}")
    print(conversation_with_kg.memory.kg)
    print(conversation_with_kg.memory.kg.get_triples())









def new_ConversationBufferMemory_memory():

    llm = OpenAI(model_name='text-davinci-003',
                 temperature=0,
                 max_tokens=256)

    memory = ConversationBufferMemory()

    conversation = ConversationChain(
        llm=llm,
        verbose=True,
        memory=memory
    )

    conversation.predict(input="Hi there! I am Sam")
    conversation.predict(input="How are you today?")
    conversation.predict(input="I'm good thank you. Can you help me with some customer support?")
    print(conversation.memory.buffer)
