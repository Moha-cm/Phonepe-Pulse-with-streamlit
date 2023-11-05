import streamlit as st
from user_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go

# set tha page title 

st.title("User Data Analysis of  District")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)


# Top district 
Top_data = top_user()
top_year  = pd.DataFrame( Top_data[0]) # for yearly
top_district = pd.DataFrame(Top_data[1])
top_pincode = pd.DataFrame(Top_data[2])

# st.dataframe(top_district)
# st.dataframe(top_pincode)



no_of_states = len(top_district["State"].unique())
no_of_years = len(top_district["Year"].unique())


no_of_top_pincode = len(top_pincode["Pincode"].unique())
st.sidebar.header("Filter year")

# sidebar
year = st.sidebar.multiselect(
    label=f" out of {no_of_years} years",
    options=top_district ["Year"].unique(),
    default=top_district["Year"].unique())

st.sidebar.header("Filter states")

state = st.sidebar.multiselect(
    
    label=f" out of {no_of_states} states",
    options=top_district ["State"].unique(),
    default=top_district["State"].unique())
year1 = year
state1 =  state

# query
state_selection = top_district.query(
    "Year==@year  & State==@state")
no_of_district = len(state_selection["District_Users"].unique())

District = st.sidebar.multiselect(
    label=f" out of {no_of_district} District",
    options=state_selection ["District_Users"].unique(),
    default=state_selection["District_Users"].unique())

df_selection  = state_selection .query(
    "District_Users==@District")

# getting the pincode dataframe


df_selection2 = top_pincode.query(
    "Year==@year1  & State==@state1")
no_of_pincode = len(df_selection2["Pincode"].unique())
pincode = st.sidebar.multiselect(
    label=f" out of {no_of_pincode} Pincodes",
    options=df_selection2["Pincode"].unique(),
    default=df_selection2["Pincode"].unique())



def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)



def Home():
    
    State_count=pd.DataFrame(df_selection["State"].unique())
    State_count= State_count.count()
    
    District_count=pd.DataFrame(df_selection["District_Users"].unique())
    District_count= District_count.count()
    
    avg_regs = average_fuc(df_selection["RegisteredUsers"])
    
    pincode_count = df_selection2["Pincode"].unique()
    pincode_count = len(pincode_count)
    
    #st.write(pincode_count )
    
    
    
    col1,col2,col3= st.columns(3)

    with col1:
        st.info(" State ")
        st.metric(value= State_count,label="Count")
    with col2:
        st.info("District_Users")
        st.metric(value=  District_count,label="Count")
        
    with col3:
        st.info("Registered Users")
        st.metric(value=avg_regs,label="percentage")

    with st.expander("Tabular"):
        showData = st.multiselect("Filter: ",df_selection.columns)
        st.write(df_selection[showData])
        
    pin1,pin2,pin3 = st.columns(3)
    with pin1:
        st.info("Pincode")
        st.metric(value=pincode_count,label="count")
    
    
Home()

def graphs():
    cl1,cl2 = st.columns(2)
    with cl1:
        df = df_selection.sort_values(by=["RegisteredUsers"],ascending=False) 
        df =  df.head(1000)  
        fig = px.bar(df, x="RegisteredUsers", y="District_Users",color='Year',title=" Yearly RegisteredUsers on  District  ",hover_data=(["State"]),orientation='h') 
    #st.dataframe(df)
        st.plotly_chart(fig)
             
    with cl2:
        df = df_selection.sort_values(by=["RegisteredUsers"],ascending=False)
        fig = px.bar(df, x="RegisteredUsers", y="State",color='Year',title="Yearly Registered Users on Each state ") 
        st.plotly_chart(fig)
        
    
    cl3,cl4 = st.columns(2)
    with cl3:
       
        df_selection2["Pincode"] = df_selection2["Pincode"].astype(str) 
        df1 = df_selection2.sort_values(by=["RegisteredUsers"],ascending=False)
        fig = px.bar(df1, x="State", y="RegisteredUsers",color='Pincode',title="Yearly Resgistered userd on Ecah state") 
        st.plotly_chart(fig)
   
graphs()