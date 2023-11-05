import streamlit as st
from user_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go

# set tha page title 

st.title("User Data Analysis of  State")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)
#st.set_page_config(layout="wide",page_icon="")

Total_user_data = get_user() # tuple with both yeara nad state 
year_data =pd.DataFrame(Total_user_data [0]) # for yearly user
state_data = pd.DataFrame(Total_user_data [1]) # for Statewise user 

# Map
# st.dataframe(pd.DataFrame( Map_data[0])) # for yearly
# st.dataframe(pd.DataFrame(Map_data[1]))  # for Statewise user 

# Top
   # for Statewise user 
  
  
# calculate average
def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)
    
# count of each unique valaues


no_of_years = len(state_data["Year"].unique())
no_of_states = len(state_data["State"].unique())

# no_of_pincodes = len(top_pincode["Pincode_Users"])


# side bar manual for year data 
st.sidebar.header("Filter year")



year = st.sidebar.multiselect(
    
    label=f" out of {no_of_years} years",
    options=state_data ["Year"].unique(),
    default=state_data ["Year"].unique())

st.sidebar.header("Filter State ")
state = st.sidebar.multiselect(
    label=f"out of {no_of_states} states",
    options=state_data["State"].unique(),
    default=state_data["State"].unique())


# setting the query 
df_selection = state_data.query(
    "Year==@year  & State==@state")

no_of_brands = len(df_selection ["Brand"].unique())

st.sidebar.header("Filter Brand")

brand = st.sidebar.multiselect(
    label=f"out of{no_of_states} Brand",
    options=df_selection["Brand"].unique(),
    default=df_selection["Brand"].unique())


# setting the query 
df_selection = df_selection.query(
    "Year==@year & Brand==@brand & State==@state")



# setting the tabular format  to view 
# setting the KPI

def Home():
    
    
    state_count=pd.DataFrame(df_selection["State"].unique())
    state_count= state_count.count()
    
    brand_count =pd.DataFrame(df_selection["Brand"].unique())
    brand_count = brand_count.count()
    
    Average_Regestration = average_fuc(df_selection["Total_registered_users"])
    Total_transcation = average_fuc(df_selection["Total_transcation"])
    
    App_user1 = df_selection[df_selection["Number_of_app"] != 0]
    avg_user = average_fuc( App_user1["Number_of_app"])
    
   
      
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.info("state_count")
        st.metric(value= state_count,label="Count")
    with col2:
        st.info("Brand Types ")
        st.metric(value=brand_count,label="Count")
    with col3:
        st.info("Registered_users")
        st.metric(value=Average_Regestration,label="percentage")
    with col4:
        st.info("Transaction")
        st.metric(value=Total_transcation,label="percentage")
        
    with col5:
        st.info("App Users")
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
        fig = px.bar(df, x="State", y="Total_transcation",color='Year',title="Users Transcation Plot on state wise",hover_data=(["Brand"])) 
    #st.dataframe(df)
        st.plotly_chart(fig)
    with cl2:
        df = df_selection.sort_values(by=["Total_registered_users"],ascending=False)
        df = df.head(500)
        fig = px.bar(df, x="State", y="Total_registered_users",color='Year',title="Registered Users Plot on state wise") 
        st.plotly_chart(fig)
    
    d1,d2 = st.columns(2)
    with d1:
        df = df_selection.sort_values(by=["Per_share_current_device"],ascending=False)
        df = df.head(500)
        
        fig = px.pie(df, values='Per_share_current_device', names='Brand', title='Percent share device')
        st.plotly_chart(fig)
        
    with d2:
        df1 = df_selection.sort_values(by=["Number_of_app"],ascending=False)
       # df = df_selection.sort_values(by=["Number_of_app"],ascending=False)
        fig = px.bar(df1, x="State", y="Number_of_app",color='Year',title="App users") 
        st.plotly_chart(fig)
        
    
graphs()










