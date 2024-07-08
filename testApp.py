import logging
import streamlit as st
from saptest import *
from utilities import initialize_session, reset_session
import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

# Aryan Test Application Changes

logger = logging.getLogger(__name__)
initialize_session()

st.set_page_config(layout='wide')
st.sidebar.image('logos/impactqa.png')
st.sidebar.title("Test Case Generation POC")
st.markdown("<h5 style='text-align: right; color: black;'>UNLOCK THE FUTURE OF SAP & CTRM TESTING</h5>", unsafe_allow_html=True)
# # Place the image in the second column to align it to the right
# # Leaves image a little large
# col1, col2 = st.columns([3, 1])
# with col2:
#     st.image(image='logos/nexai.png', caption=' # NeX-AI #', use_column_width=True)

# Img not displaying using filename, would need to use url to img to display
st.markdown('<img style="float: right; max-width: 150px;" src="/Users/impactqaservices68/PycharmProjects/pythonProject/logos/nexai.png">', unsafe_allow_html=True)


data = {
    'Main': ['SAP', 'SAP', 'SAP', 'SAP', 'SAP', 'SAP' ,'CTRM/ETRM' ,'CTRM/ETRM','CTRM/ETRM','CTRM/ETRM','CTRM/ETRM','CTRM/ETRM'],
    'Choose Module': ['Asset Management','HR', 'Supply chain', 'Ls Oil Upstream', 'Ls Oil downstream', 'Other Modules', 'Deal Execution', 'Trading', 'Logistics', 'Risk Management', 'Settlement', 'Endure Configuration']
}

df = pd.DataFrame(data)
dynamic_filters = DynamicFilters(df, filters=['Main', 'Choose Module'])
dynamic_filters.display_filters(location='sidebar', gap='small')
poc_prompt = ['Choose Prompt', 'SAP +ve Test cases', 'ETRM', 'ETRM endur configuration', 'SAP -Ve test cases']
transaction_name = st.sidebar.selectbox('Transaction Name?', poc_prompt)
print("Selected prompt is " + transaction_name)
tcode = st.sidebar.text_input('Enter Tcode')
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
if transaction_name == "ETRM" and st.session_state.sidebar_submit_flag:
    st.write("LLM generating test cases for ... " + transaction_name)
    # response = generate_test_prompt_templates(format_prompt=loaded_prompt.format(Tcode='MN21', VendorName='aramco'))
    response = generate_test_prompt(Transaction_code=tcode, Transaction_Name=t_Name, format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=t_Name))
    st.subheader("Test cases for : "+transaction_name)

elif transaction_name == "ETRM endur configuration" and st.session_state.sidebar_submit_flag:
    st.write("LLM generating test cases for ... "+transaction_name)
    # response = generate_test_prompt_templates(format_prompt=loaded_prompt.format(Tcode='MN21', VendorName='aramco'))
    response = generate_test_prompt(Transaction_code=tcode, Transaction_Name=t_Name, format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=t_Name))
    st.subheader("Test cases for : "+transaction_name)

elif transaction_name is not None and st.session_state.sidebar_submit_flag:
    st.write("LLM generating test cases for ... "+transaction_name)
    response = generate_test_prompt(Transaction_code=tcode, Transaction_Name=t_Name, format_prompt=loaded_prompt.format(Transaction_code=tcode, Transaction_Name=t_Name))
    st.subheader("Test cases for : "+transaction_name)

else:
    response = "Choose the module, Transaction code, Name and click on Generate button"

# st.write(pd.DataFrame.from_dict(response)) #working only for on record. needs to be fixed to download as xls.
st.write(response)

user_input = st.chat_input('ask question about the test cases')