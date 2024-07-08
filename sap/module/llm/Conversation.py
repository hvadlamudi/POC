from abc import ABC, abstractmethod

from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseMemory
from langchain.chains.base import Chain
from langchain_core.prompts import PromptTemplate
import streamlit as st
from sap.module.llm.LLMConfig import LLMConfig


class BaseConversation(ABC):
    def __init__(self,
                 prompt: PromptTemplate,
                 llm_config: LLMConfig,
                 memory: BaseMemory = None):
        self.conversation_memory = memory
        self.llm_config = llm_config
        self.prompt = prompt

    @property
    @abstractmethod
    def chain(self) -> Chain:
        pass

    @abstractmethod
    def get_response(self, query, **kwargs) -> str:
        pass


class SAPConversation(BaseConversation):

    def __init__(self, model_settings):
        super().__init__(
            prompt=PromptTemplate(),
            llm_config=LLMConfig(model_settings),
            memory=ConversationBufferMemory()
        )

    @property
    def chain(self) -> Chain:
        pass

    def get_response(self, query, **kwargs) -> str:
        response = None
        try:
            st.session_state.enable_chat_flag = True


            llm_chain = create_default_chain(
                llm=self.llm_config.llm,
                conversation_memory = self.conversation_memory,
                default_template = self.prompt
            )
            response = llm_chain.run({'input': query})
        except Exception as e:
            pass

        return response

def create_default_chain(llm, conversation_memory, default_template):
    try:
        return ConversationChain(
            llm=llm,
            memory = conversation_memory,
            prompt = PromptTemplate(
                template=default_template,
                input_variables=['input']
            ),
            output_key="text",
            verbose=True
        )
    except Exception as e:
        print(f"ERROR: ")
        raise e
