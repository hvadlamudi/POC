import logging
import uuid
from langchain.memory import ConversationBufferMemory
from abc import ABC
import streamlit as st
from langchain.memory import ConversationBufferMemory
import streamlit as st
from streamlit_feedback import streamlit_feedback

logger = logging.getLogger(__name__)
def get_uuid(num_chars=4) -> str:
    return str(uuid.uuid4())[:num_chars]


def initialize_session():
    """Initialize chat history"""
    if "session_id" not in st.session_state:
        st.session_state.session_id = get_uuid(num_chars=8)
    if 'username' not in st.session_state:
        st.session_state['username'] = ''
    if "messages" not in st.session_state:
        st.session_state.messages = {st.session_state.session_id: {}}
    if "sidebar_submit_flag" not in st.session_state:
        st.session_state.sidebar_submit_flag = False
    if "tname" not in st.session_state:
        st.session_state.tname = None
    if "tcode" not in st.session_state:
        st.session_state.tcode = None
    if "entity_memory" not in st.session_state:
        st.session_state.entity_memory = ConversationBufferMemory()


def reset_session():
    "reset session state"
    for key in st.session_state.keys():
        if 'file_uploader_key' in key:
            st.session_state.file_uploader_key += 1
        else:
            del st.session_state[key]

def _submit_feedback(user_response):
    score_map={
        "👍":1,
        "👎":0
    }
feedback_kwargs = {
    "feedback_type":"thumbs",
    "optional_text_label":"[Optional] Please provide an explanation."
}
def render_conservation(session_id):
    if "messages" in st.session_state:
        for msg_id in st.session_state.messages[session_id].keys():
            message = st.session_state.messages[session_id][msg_id]
            feedback_key = 'feedback_'+msg_id
            if message['role'] == 'assistant':
                with st.chat_message(message['role'], avatar="bot.jpg"):
                    st.markdown(message['content'])

                    if feedback_key not in st.session_state:
                        st.session_state[feedback_key]=None

                    disable_with_score=(
                        st.session_state[feedback_key].get('score')
                        if st.session_state[feedback_key]
                        else None
                    )

                    user_response=streamlit_feedback(
                        **feedback_kwargs,
                        disable_with_score = disable_with_score,
                        key = feedback_key,
                        on_submit = _submit_feedback,
                    )

                    if user_response:
                        st.session_state.messages[session_id][msg_id].update(user_response)

            else:
                with st.chat_message(message['role'], avatar='user.jpg'):
                    st.markdown(message['content'])
    # st.session_state.session_id
