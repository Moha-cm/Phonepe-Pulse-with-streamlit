from transaction_data_retrival import * 
import streamlit as st
from transaction_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd 


st.title(" Data Analysis  based on Top Tansaction")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)


top_data = top_user()
top_year  = pd.DataFrame(top_data[0])
top_district = pd.DataFrame(top_data[1])
top_pincode = pd.DataFrame(top_data[2])

# st.dataframe(top_year)
# st.dataframe(top_district)
# st.dataframe(top_pincode)



 
def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)



no_of_years = len(top_year["Year"].unique())


# no_of_District = len(top_district["District_Users"].unique())
# no_of_Pincode = len(top_year["Pincode_Users"].unique())


# year
st.sidebar.header("Filter year")
year = st.sidebar.multiselect(
    label=f" out of {no_of_years} years",
    options=top_year["Year"].unique(),
    default=top_year ["Year"].unique())

# setting the query 
df_selection = top_district.query(
    "Year==@year")


# state
no_of_states = len(df_selection["State"].unique())

state = st.sidebar.multiselect(
    label=f" out of {no_of_states} states",
    options=df_selection["State"].unique(),
    default=df_selection["State"].unique())

# query
df_selection = top_district.query("State==@state")
pin_selection = top_pincode.query("State==@state")

# district
no_of_district = len(df_selection ["District"].unique())
st.sidebar.header("Filter District")
district= st.sidebar.multiselect(
    label=f"out of{no_of_district} District",
    options=df_selection["District"].unique(),
    default=df_selection["District"].unique())

# setting the query 
df_selection = df_selection.query("District==@district")

#pincode
no_of_pincode = len(pin_selection ["Pincode"].unique())
st.sidebar.header("Filter District")
pincode= st.sidebar.multiselect(
    label=f"out of{no_of_pincode} Pincode",
    options=pin_selection["Pincode"].unique(),
    default=pin_selection["Pincode"].unique())

pin_selection = pin_selection.query("Pincode==@pincode")

st.dataframe(pin_selection)
# year_df = top_year.query("Year==@year  & State==@state &Pincode==@pincode")

# setting the tabular format  to view 
# setting the KPI

def Home():
    
    
    state_count=pd.DataFrame(df_selection["State"].unique())
    state_count= state_count.count()
    
    D_count =pd.DataFrame(df_selection["District"].unique())
    D_count = D_count.count()
    
    Pin_count =len(pin_selection["Pincode"].unique())
    
    
    D_Trans = average_fuc(df_selection["Total_transactions"])
    D_value = average_fuc(df_selection["Total_value"])
    
    P_Trans = average_fuc(pin_selection["Total_transactions"])
    P_value = average_fuc(pin_selection["Total_value"])
     
      

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.info("state_count")
        st.metric(value= state_count,label="Count")
    with col2:
        st.info("Brand Types ")
        st.metric(value=D_count,label="Count")
    with col3:
        st.info("Top District Transaction")
        st.metric(value=D_Trans,label="percentage")
    with col4:
        st.info("Top District value")
        st.metric(value=D_count,label="percentage")
     
    col5,col6,col7 = st.columns(3) 
    with col5:
        st.info("Pincode")
        st.metric(value=Pin_count,label="count")
    
    with col6:
        st.info("Top Pincode Transaction")
        st.metric(value=P_Trans,label="percentage")
        
    with col7:
        st.info("Top Pincode Transaction")
        st.metric(value=P_value,label="percentage")
        
    # with st.expander("Top  Transaction"):
    #     showData = st.multiselect("Filter: ", year_df.columns)
    #     st.write(df_selection[showData]) 
        
      
    with st.expander(" District Tabular"):
        showData = st.multiselect("Filter: ",df_selection.columns)
        st.write(df_selection[showData]) 
    
    with st.expander(" Pincode Tabular"):
        showData = st.multiselect("Filter: ",pin_selection.columns)
        st.write(df_selection[showData]) 
      
Home()

def graphs():
    cl1,cl2 = st.columns(2)
    with cl1:
        df = df_selection.sort_values(by=["Total_transactions"],ascending=False)
        fig = px.bar(df, x="District", y="Total_transactions",color='State',title=" Total Transcation on  each District",hover_data=(["Year"])) 
        st.plotly_chart(fig)
        
    with cl2: #pin_selection["Total_transactions"]
        df = pin_selection.sort_values(by=["Total_transactions"],ascending=False)
        fig = px.bar(df, x="Pincode", y="Total_transactions",color='State',title="Total Transcataion on each state  Pincode",hover_data=(["Year"])) 
        st.plotly_chart(fig)
    
    
    d1,d2 = st.columns(2)
    with d1:
        df = df_selection.sort_values(by=["Total_value"],ascending=False)
        fig = px.bar(df, x="District", y="Total_value",color='State',title="Total Value on each state District",hover_data=(["Year"])) 
        st.plotly_chart(fig)
     
        
    with d2:
        df1 = pin_selection.sort_values(by=["Total_value"],ascending=False)
        fig = px.bar(df1, x="Pincode", y="Total_value",color='State',title="Total Value on each stae Pincode",hover_data=(["Year"])) 
        st.plotly_chart(fig)
    
    d5,d6 = st.columns(2)
    
    with d5:
        df1 = pin_selection.sort_values(by=["Total_transactions"],ascending=False)
        fig = px.pie(df1, color="State", hover_data=['Pincode'],values="Total_transactions",names='State',title="Total Transaction on each state Pincode")
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
        
    with d6:
        df1 = df_selection.sort_values(by=["Total_transactions"],ascending=False)
        fig = px.pie(df1, color="District",values="Total_transactions",names='State',title="Total Transaction on each District Pincode",hover_data=['Year'])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
    
    
    
    
    
    d3,d4 = st.columns(2)
    with d3:
        df1 = pin_selection.sort_values(by=["Total_value"],ascending=False)
        fig = px.pie(df1, color="Year", hover_data=['Pincode'],values="Total_value",names='State',title="Total Value on each state Pincode")
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
    with d4:
        df1 = df_selection.sort_values(by=["Total_value"],ascending=False)
        fig = px.pie(df1, color="District",values="Total_value",names='State',title="Total Value on each District Pincode",hover_data=['Year'])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
   
graphs()






