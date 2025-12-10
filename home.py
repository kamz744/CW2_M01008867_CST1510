import streamlit as st
import pandas as pd
from app_model.db import conn
from app_model.cyber_incidents import get_all_cyber_incidents
df = pd.DataFrame({
"Name": ["Jordan", "Alex", "Taylor"],
 "Score": [95, 88, 76]
})


st.title("welcome to home page")
st.write("hello")
st.header("hello")
st.subheader("subheader")
st.write("flexible display")

st.caption("capture")

st.dataframe(df)


with st.sidebar:
    st.header("navigation")
    severity_=st.selectbox ("severity,data) ["severity"].unique())
                           
filtered_data = data [data [" severity "] == severity_]                    