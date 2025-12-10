import streamlit as st
import pandas as pd
from app.db import conn
from app.cyber_incident import get_all_cyber_incidents

st.set_page_config(
    page_title="Home",
    page_icon='',
    layout="wide"
)


df = get_all_cyber_incidents(conn)




st.title("welcome to home page")
st.write("this is the main landing of my page application")

df["timestamp"]=pd.to_datetime(df["timestamp"])



with st.sidebar:
    st.header("navigation")
    st.selectbox('severity', df['severity'].unique())
    severity_ = st.selectbox("Severity",df ["severity"].unique())

filtered_data=df[df["severity"]==severity_]

col1, col2=st.columns(2)

with col1:
    st.bar_chart(filtered_data["category"].value_counts())

with col2:
    st.line_chart(filtered_data["timestamp"])




st.bar_chart(df["category"].value_counts())

st.caption("capture")

st.dataframe(df)


              