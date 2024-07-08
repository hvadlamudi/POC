import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

data1 = {
    'region': ['North America', 'North America', 'Europe', 'Oceania', 'North America', 'North America', 'Europe', 'Oceania', 'North America', 'North America', 'Europe', 'Oceania'],
    'country': ['USA', 'Canada', 'UK', 'Australia','USA', 'Canada', 'UK', 'Australia', 'USA', 'Canada', 'UK', 'Australia'],
    'city': ['New York', 'Toronto', 'London', 'Sydney', 'New York', 'Toronto', 'London', 'Sydney','New York', 'Toronto', 'London', 'Sydney'],
    'district': ['Manhattan', 'Downtown', 'Westminster', 'CBD','Brooklyn', 'Midtown', 'Kensington', 'Circular Quay', 'Queens', 'Uptown', 'Camden', 'Bondi']
}

data = {
    'Main': ['SAP', 'SAP', 'SAP', 'SAP', 'SAP', 'SAP' ,'CTRM/ETRM' ,'CTRM/ETRM','CTRM/ETRM','CTRM/ETRM','CTRM/ETRM','CTRM/ETRM'],
    'Choose Module': ['Asset Management','HR', 'Supply chain', 'Ls Oil Upstream', 'Ls Oil downstream', 'Other Modules', 'Deal Execution', 'Trading', 'Logistics', 'Risk Management', 'Settlement', 'Endure Configuration']
}

df = pd.DataFrame(data)
# dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'])
dynamic_filters = DynamicFilters(df, filters=['Main', 'Choose Module'])
st.write("Apply filters in any order 👇")
dynamic_filters.display_filters(location='sidebar', gap='small')
# dynamic_filters.display_filters(location='sidebar', gap='samll')
dynamic_filters.display_df()