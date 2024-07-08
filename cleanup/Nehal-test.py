import streamlit as st
import graphviz as graphviz

st.title("Test App")
st.markdown("Description")
st.graphviz_chart('''
    digraph {
    Step 1 -> Step 2
    Step 2 -> Step 3
''')

st.sidebar.title("Sidebar")
st.sidebar.radio("Pick an option", ["Option 1", "Option 2", "Option 3"])

