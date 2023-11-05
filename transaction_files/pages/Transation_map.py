from transaction_data_retrival import * 
import streamlit as st
from transaction_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd 


st.title(" Data Analysis  based on Top Tansaction")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)


top_data = map_user()
m_year  = pd.DataFrame(top_data[0])
m_district = pd.DataFrame(top_data[1])

