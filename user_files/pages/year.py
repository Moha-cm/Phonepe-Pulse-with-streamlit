import streamlit as st
from user_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go

# set tha page title 

st.title("User Data Analysis for   Year")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)

Total_user_data = get_user() # tuple with both year and state 
year_data=pd.DataFrame(Total_user_data [0])






st.dataframe(year_data)
no_of_brands = len(year_data["Brand"].unique())
no_of_years = len(year_data["Year"].unique())


st.sidebar.header("Filter year")
year = st.sidebar.multiselect(
    
    label=f" out of {no_of_years} years",
    options=year_data ["Year"].unique(),
    default=year_data ["Year"].unique())

st.sidebar.header("Filter brand ")

brand = st.sidebar.multiselect(
    label=f"out of {no_of_brands} brands",
    options=year_data["Brand"].unique(),
    default=year_data["Brand"].unique())


df_selection = year_data.query(
    "Year==@year  & Brand==@brand")

def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)
    
    


def Home():
    
    
    brand_count=pd.DataFrame(df_selection["Brand"].unique())
    brand_count= brand_count.count()
    
    

    
    avg_regs = average_fuc(df_selection["Total_registered_users"])
    avg_trans = average_fuc(df_selection["Total_transcation"])
    
    App_user1 = df_selection[df_selection["Number_of_app"] != 0]
    avg_user = average_fuc( App_user1["Number_of_app"])

 
   

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.info("Brand Types ")
        st.metric(value=brand_count,label="Count")
    with col2:
        st.info("Registered_users")
        st.metric(value=avg_regs,label="percentage")
    with col3:
        st.info("Transaction")
        st.metric(value=avg_trans ,label="percentage")
    with col4:
        st.info("App_users")
        st.metric(value=avg_user,label="percentage")
        
            
    with st.expander("Tabular"):
        showData = st.multiselect("Filter: ",df_selection.columns)
        st.write(df_selection[showData])
Home()


def graphs():
    cl1,cl2 = st.columns(2)
    with cl1:
        df = df_selection.sort_values(by=["Total_transcation"],ascending=False)
        df = df.head(500)   
        fig = px.bar(df, x="Year", y="Total_transcation",color='Brand',title="Users Yearly Transcation Plot ",hover_data=(["Brand"])) 
    #st.dataframe(df)
        st.plotly_chart(fig)
    with cl2:
        df = df_selection.sort_values(by=["Total_registered_users"],ascending=False)
        df = df.head(500)
        fig = px.bar(df, x="Year", y="Total_registered_users",color='Brand',title="Yearly Registered Users Plot ") 
        st.plotly_chart(fig)
    
    d1,d2 = st.columns(2)
    with d1:
        df = df_selection.sort_values(by=["Per_share_current_device"],ascending=False)
        df = df.head(500)
        
        fig = px.pie(df, values='Per_share_current_device', names='Brand', title='Yearly Percent share device')
        st.plotly_chart(fig)
    with d2:
        
        df = df_selection.sort_values(by=["Number_of_app"],ascending=False)
        df = df.head(500)
        df = df_selection.sort_values(by=["Number_of_app"],ascending=False)
        fig = px.bar(df, x="Brand", y="Number_of_app",color='Year',title="Yearly App users") 
        
        st.plotly_chart(fig)

graphs()

