import logging
from io import StringIO
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters
from saptest import *
from utilities import initialize_session, reset_session, render_conservation, get_uuid

st.set_page_config(layout='wide')
st.sidebar.image('logos/impactqa.png')
st.sidebar.title("Test Case Generation POC")
st.markdown("<h5 style='text-align: right; color: black;'>UNLOCK THE FUTURE OF SAP & CTRM TESTING</h5>",
            unsafe_allow_html=True)
st.image(image='logos/nexai.png', caption=' # NeX-AI #', )
data = {
    'Main': ['SAP', 'SAP', 'SAP', 'SAP', 'SAP', 'SAP', 'CTRM/ETRM', 'CTRM/ETRM', 'CTRM/ETRM', 'CTRM/ETRM', 'CTRM/ETRM',
             'CTRM/ETRM'],
    'Choose Module': ['Asset Management', 'HR', 'Supply chain', 'Ls Oil Upstream', 'Ls Oil downstream', 'Other Modules',
                      'Deal Execution', 'Trading', 'Logistics', 'Risk Management', 'Settlement', 'Endure Configuration']
}
df = pd.DataFrame(data)


def sidebar():

    with st.sidebar:
        dynamic_filters = DynamicFilters(df, filters=['Main', 'Choose Module'])
        dynamic_filters.display_filters(location='sidebar', gap='small')
        st.session_state.tname = st.sidebar.text_input('Transaction Name? Search test case')  # t_Name = Transaction_Name
        st.session_state.tcode = st.sidebar.text_input('Transaction code?')  # tcode = 'MN21'
        col1, col2 = st.columns([.5, 1])
        with col1:
            st.session_state.sidebar_submit_flag = st.sidebar.button('Generate Test')
        with col2:
            reset_button = st.sidebar.button(label='Reset')

        if reset_button:
            reset_session()
            st.rerun()

        # Add a llm, token, temp to the slider sidebar:
        st.session_state.name_llm = st.sidebar.selectbox('Choose LLM', ('gpt-3.5-turbo-instruct', 'gpt-4-turbo'), index=0)
        st.session_state.token_size = st.sidebar.slider('Maxtokens', 64, 4000, 3900)
        st.session_state.temp_size = st.sidebar.slider('Choose temperature', 0.0, 1.0, .90)
