import logging
from io import StringIO
import ast

# repose to df
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters
from saptest import *
from utilities import initialize_session, reset_session

logger = logging.getLogger(__name__)
initialize_session()

st.set_page_config(layout='wide')
st.sidebar.image('logos/impactqa.png')
st.sidebar.title("Test Case Generation POC")
st.markdown("<h5 style='text-align: right; color: black;'>UNLOCK THE FUTURE OF SAP & CTRM TESTING</h5>", unsafe_allow_html=True)
st.image(image='logos/nexai.png', caption=' # NeX-AI #', )
#st.markdown('<img style="background-image": right;" src="C:/Users/impactqaservices68/PycharmProjects/pythonProject/logos/logo.png" />', unsafe_allow_html=True)

data = {
    'Main': ['SAP', 'SAP', 'SAP', 'SAP', 'SAP', 'SAP' ,'CTRM/ETRM' ,'CTRM/ETRM','CTRM/ETRM','CTRM/ETRM','CTRM/ETRM','CTRM/ETRM'],
    'Choose Module': ['Asset Management','HR', 'Supply chain', 'Ls Oil Upstream', 'Ls Oil downstream', 'Other Modules', 'Deal Execution', 'Trading', 'Logistics', 'Risk Management', 'Settlement', 'Endure Configuration']
}
df = pd.DataFrame(data)
dynamic_filters = DynamicFilters(df, filters=['Main', 'Choose Module'])
dynamic_filters.display_filters(location='sidebar', gap='small')
# poc_prompt = ['Choose Prompt', 'SAP +ve Test cases', 'ETRM', 'ETRM endur configuration', 'SAP -Ve test cases']
# transaction_name = st.sidebar.selectbox('Transaction Name?', poc_prompt)
transaction_name = st.sidebar.text_input('Transaction Name? Search test case')
print("Selected prompt is " + transaction_name)
tcode = st.sidebar.text_input('Transaction code?')
# tcode = 'MN21'
t_Name = transaction_name
col1, col2 = st.columns([.5, 1])
with col1:
    st.session_state.sidebar_submit_flag = st.sidebar.button('Generate Test')
with col2:
    reset_button = st.sidebar.button(label='Reset')

if reset_button:
    reset_session()
    st.rerun()

# Add a slider to the sidebar:
add_slider = st.sidebar.slider('Select temperature', 0.0, 1.0, (.50, .90))
if transaction_name.lower() == "ETRM".lower() and st.session_state.sidebar_submit_flag:
    st.write("LLM generating test cases for ... " + transaction_name)
    # response = generate_test_prompt_templates(format_prompt=loaded_prompt.format(Tcode='MN21', VendorName='aramco'))
    response = generate_test_prompt(Transaction_code=tcode, Transaction_Name=t_Name, format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=t_Name))
    st.subheader("Test cases for : "+transaction_name)

elif transaction_name.lower() == "ETRM endur configuration".lower() and st.session_state.sidebar_submit_flag:
    st.write("LLM generating test cases for ... "+transaction_name)
    # response = generate_test_prompt_templates(format_prompt=loaded_prompt.format(Tcode='MN21', VendorName='aramco'))
    response = generate_test_prompt(Transaction_code=tcode, Transaction_Name=t_Name, format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=t_Name))
    st.subheader("Test cases for : "+transaction_name)

elif transaction_name is not None and st.session_state.sidebar_submit_flag:
    st.write("LLM generating test cases for ... "+transaction_name)
    response = generate_test_prompt_vasu(Transaction_code=tcode, Transaction_Name=t_Name, format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=t_Name))
    st.subheader("Test cases for : "+transaction_name)

else:
    response = "Choose the module, Transaction code, Name and click on Generate button"

# st.write(pd.DataFrame.from_dict(response)) #working only for on record. needs to be fixed to download as xls.
st.write(response)
# if st.session_state.sidebar_submit_flag:
#     if response is None:
#         pass
#     else:
#         dict_obj = ast.literal_eval(str(response))
#         TestCases = (dict_obj["text"])
#         TestCases = StringIO(TestCases)
#         df = pd.read_csv(TestCases, sep="|", index_col=False)
#         df.dropna(how='all', axis=1)
#         df = df.drop(df.columns[0],axis=1)
#         df = df.drop(df.columns[7],axis=1)
#         print(df.shape)
#         st.dataframe(df)

user_input = st.chat_input('Tweak above generated test cases')
# if "messages" not in st.session_state:
#     st.session_state.messages = []
if user_input is not None:
    # st.session_state.messages.append({'role':'user','content':user_input})
    # st.session_state.messages.add({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        print(st.session_state.messages)
        prompt = st.session_state.messages[-2]['content']
        st.write(user_input)
        # print(llm(text))