import streamlit as st
from user_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go

# set tha page title 

st.title("User Data Analysis of  District")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)

st.write("under CONstructionn???????????????????????????!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


# Top district 
Top_data = top_user()
top_year1  = pd.DataFrame( Top_data[0]) # for yearly

top_dict = {"State_Users":str,"District_Users":str,"Pincode_Users":str,"Year":str,"S_RegisteredUsers":int,"D_RegisteredUsers":int,"P_RegisteredUsers":int}
top_year = top_year1.astype(top_dict)

top_year = st.dataframe(top_year)

# state_user_ag_data_dict = {"Total_transcation":int}
# state_user_ag_data = state_user_ag_data.astype(state_user_ag_data_dict)

st.dataframe(top_year)

# Average
def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)


no_of_states = len(top_year["State_Users"].unique())
no_of_District = len(top_year["District_Users"].unique())
no_of_Pincode = len(top_year["Pincode_Users"].unique())
no_of_years = len(top_year["Year"].unique())

st.sidebar.header("Filter year")


year = st.sidebar.multiselect(
    label=f" out of {no_of_years} years",
    options=top_year["Year"].unique(),
    default=top_year ["Year"].unique())

state = st.sidebar.multiselect(
    label=f" out of {no_of_states} states",
    options=top_year["State_Users"].unique(),
    default=top_year ["State_Users"].unique())

district = st.sidebar.multiselect(
    label=f" out of {no_of_years} District",
    options=top_year["District_Users"].unique())

pincode = st.sidebar.multiselect(
    label=f" out of {no_of_years} Pincode",
    options=top_year["Pincode_Users"].unique())
top_year["District_Users"] = top_year["District_Users"].astype(str)

df_selection = top_year.query("Year==@year  & State_Users==@state")



st.write(df_selection)



# setting the KPI
def Home():
    
    state_count=pd.DataFrame(df_selection["State_Users"].unique())
    state_count= state_count.count()
    
    District_count=pd.DataFrame(df_selection["District_Users"].unique())
    state_count= District_count.count()
    
    pincode_count=pd.DataFrame(df_selection["Pincode_Users"].unique())
    Pincode_count= pincode_count.count()
    

    
    State_Average_Regestration = average_fuc(df_selection["S_RegisteredUsers"])
    District_average_reges = average_fuc(df_selection["D_RegisteredUsers"])
    pincode_average_reges = average_fuc(df_selection["P_RegisteredUsers"])
    
    
    
   
      
    
    col1,col2,col3 = st.columns(3)
    with col1:
        st.info("State")
        st.metric(value= state_count,label="Count")
    with col2:
        st.info("District ")
        st.metric(value=District_count,label="Count")
    with col3:
        st.info("Pincode")
        st.metric(value=pincode_count,label="count")
        
    col4,col5,col6 = st.columns(3)
    with col4:
        st.info("State Registered Users")
        st.metric(value=State_Average_Regestration,label="percentage")
        
    with col5:
        st.info("District Registered Users")
        st.metric(value=District_average_reges,label="percentage")
    with col6:
        st.info("Pincode Registered users")
        st.metric(value = pincode_average_reges,label="percentage")
        
    
        
    with st.expander("Tabular"):
        showData = st.multiselect("Filter: ",df_selection.columns)
        st.write(df_selection[showData])   
Home()


