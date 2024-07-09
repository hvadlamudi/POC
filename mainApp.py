import ast
import logging
from io import StringIO
import streamlit as st

import prompts.prompts
from sap.module.ui_components.sidebar import *
from streamlit_dynamic_filters import DynamicFilters
from saptest import *
from utilities import initialize_session, reset_session, render_conservation, get_uuid

logger = logging.getLogger(__name__)
initialize_session()

global TestCases, df
sidebar()
response = None
tname = st.session_state.tname
tcode = st.session_state.tcode

if st.session_state.sidebar_submit_flag:
    if tname.lower() == "ETRM".lower():
        st.write("LLM generating test cases for ... " + tname)
        response = generate_test_prompt(Transaction_code=tcode, Transaction_Name=tname,
                                        format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=tname))
        st.subheader("Test cases for : " + tname)

    elif tname.lower() == "ETRM endur configuration".lower():
        st.write("LLM generating test cases for ... " + tname)
        response = generate_test_prompt(Transaction_code=tcode, Transaction_Name=tname,
                                        format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=tname))
        st.subheader("Test cases for : " + tname)

    elif tname is not None:
        st.write("LLM generating test cases for ... " + tname)
        # response = generate_test_prompt_vasu(Transaction_code=tcode, Transaction_Name=tname, format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=tname))
        st.subheader("Test cases for : " + tname)
        response = generate_test_prompt_hari(format_prompt=prompts.prompts.prompt)

    else:
        response = "Choose the module, Transaction code, Name and click on Generate button"



#  add response to Messages as dict items for rendering in the upcomming code.
user_msg_id=f"user_{get_uuid()}"
print(f"User id: {user_msg_id}")
st.session_state.messages[st.session_state.session_id][user_msg_id] = {"role": "user", "content": loaded_prompt}
assistant_msg_id = f"assistant_{get_uuid()}"
st.session_state.messages[st.session_state.session_id][assistant_msg_id] = {"role": "assistant", "content": response}

def to_dataframe(TestCases):
    TestCases = StringIO(TestCases)
    df = pd.read_csv(TestCases, sep="|", index_col=False)
    df.dropna(how='all', axis=1)
    print(df.shape)
    df = df.iloc[1:]  # Drop first  row
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # Drop unnamed columns
    print(df.shape)
    return df


# if st.session_state.sidebar_submit_flag:
if response is None:
    st.write("No response from LLM")
    pass  # val exists and is None
else:
    print("response is not none")
    st.write(response)
    # dict_obj = ast.literal_eval(str(response))
    # TestCases = (dict_obj["text"])
    # df = to_dataframe(TestCases=TestCases)
    # st.dataframe(df)

print("response reported back to st")
user_input = st.chat_input('Tweak above generated test cases')
# if "messages" not in st.session_state:
#     st.session_state.messages = []
if user_input is not None:
    response = generate_test_prompt_hari(format_prompt=prompts.prompts.prompt, question=user_input, session_id=st.session_state.session_id)
    # render_conservation(st.session_state.session_id)
    st.write(response)
