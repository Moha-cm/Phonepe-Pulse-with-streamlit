import streamlit as st
from user_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go

# set tha page title 

st.title("User Data Analysis of  District")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)

#st.write("under CONstructionn???????????????????????????!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


# Top district 
top_data = top_user()

top_year  = pd.DataFrame(top_data[0])
top_district = pd.DataFrame(top_data[1])
top_pincode = pd.DataFrame(top_data[2])
#top_year1  = pd.DataFrame( top_data[0]) # for yearly



# st.dataframe(top_district)
# st.dataframe(top_pincode)

top_dict = {"State_Users":str,"District_Users":str,"Pincode_Users":str,"Year":str,"S_RegisteredUsers":int,"D_RegisteredUsers":int,"P_RegisteredUsers":int}
top_year = top_year.astype(top_dict)

# st.dataframe(top_year)

# state_user_ag_data_dict = {"Total_transcation":int}
# state_user_ag_data = state_user_ag_data.astype(state_user_ag_data_dict)

#st.dataframe(top_year)

# Average
def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)


no_of_years = len(top_year["Year"].unique())

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
no_of_district = len(df_selection ["District_Users"].unique())
st.sidebar.header("Filter District")
district= st.sidebar.multiselect(
    label=f"out of{no_of_district} District",
    options=df_selection["District_Users"].unique(),
    default=df_selection["District_Users"].unique())

# setting the query 
df_selection = df_selection.query("District_Users==@district")

no_of_pincode = len(pin_selection ["Pincode"].unique())
st.sidebar.header("Filter District")
pincode= st.sidebar.multiselect(
    label=f"out of{no_of_pincode} Pincode",
    options=pin_selection["Pincode"].unique(),
    default=pin_selection["Pincode"].unique())

pin_selection = pin_selection.query("Pincode==@pincode")

#st.dataframe(pin_selection)




def Home():
    
    
    state_count=pd.DataFrame(df_selection["State"].unique())
    state_count= state_count.count()
    
    D_count =pd.DataFrame(df_selection["District_Users"].unique())
    D_count = D_count.count()
    
    Pin_count =len(pin_selection["Pincode"].unique())
    
    D_Trans = average_fuc(df_selection["RegisteredUsers"])
    
    P_Trans = average_fuc(pin_selection["RegisteredUsers"])
  
     

    col1,col2,col3 = st.columns(3)
    with col1:
        st.info("state_count")
        st.metric(value= state_count,label="Count")
    with col2:
        st.info("District")
        st.metric(value=D_count,label="Count")
    with col3:
        st.info("Top District Users")
        st.metric(value=D_Trans,label="percentage")
 
     
    col5,col6,col7 = st.columns(3) 
    with col5:
        st.info("Pincode")
        st.metric(value=Pin_count,label="count")
    
    with col6:
        st.info("Top Pincode Users")
        st.metric(value=P_Trans,label="percentage")
        
          
      
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
        df = df_selection.sort_values(by=["RegisteredUsers"],ascending=False)
        fig = px.bar(df, x="District_Users", y="RegisteredUsers",color='State',title=" Registered Users on  each District",hover_data=(["Year"])) 
        st.plotly_chart(fig)
        
    with cl2: #pin_selection["Total_transactions"]
        df = pin_selection.sort_values(by=["RegisteredUsers"],ascending=False)
        fig = px.bar(df, x="Pincode", y="RegisteredUsers",color='State',title=" RegisteredUsers on each state  Pincode",hover_data=(["Year"])) 
        st.plotly_chart(fig)
    
    
    # d1,d2 = st.columns(2)
    # with d1:
    #     df = df_selection.sort_values(by=["Total_value"],ascending=False)
    #     fig = px.bar(df, x="District", y="Total_value",color='State',title="Total Value on each state District",hover_data=(["Year"])) 
    #     st.plotly_chart(fig)
     
        
    # with d2:
    #     df1 = pin_selection.sort_values(by=["Total_value"],ascending=False)
    #     fig = px.bar(df1, x="Pincode", y="Total_value",color='State',title="Total Value on each stae Pincode",hover_data=(["Year"])) 
    #     st.plotly_chart(fig)
    
    d5,d6 = st.columns(2)
    
    with d5:
        df1 = pin_selection.sort_values(by=["RegisteredUsers"],ascending=False)
        fig = px.pie(df1, color="State", hover_data=['Pincode'],values="RegisteredUsers",names='State',title="Registered Users on each state Pincode")
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
        
    with d6:
        df1 = df_selection.sort_values(by=["RegisteredUsers"],ascending=False)
        fig = px.pie(df1, color="District_Users",values="RegisteredUsers",names='State',title="Registered Users on each District Pincode",hover_data=['Year'])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)
    
    
    
    
    
    # d3,d4 = st.columns(2)
    # with d3:
    #     df1 = pin_selection.sort_values(by=["Total_value"],ascending=False)
    #     fig = px.pie(df1, color="Year", hover_data=['Pincode'],values="Total_value",names='State',title="Total Value on each state Pincode")
    #     fig.update_traces(textposition='inside', textinfo='percent+label')
    #     st.plotly_chart(fig)
    # with d4:
    #     df1 = df_selection.sort_values(by=["Total_value"],ascending=False)
    #     fig = px.pie(df1, color="District",values="Total_value",names='State',title="Total Value on each District Pincode",hover_data=['Year'])
    #     fig.update_traces(textposition='inside', textinfo='percent+label')
    #     st.plotly_chart(fig)
   
graphs()

















# no_of_states = len(top_year["State_Users"].unique())
# no_of_District = len(top_year["District_Users"].unique())
# no_of_Pincode = len(top_year["Pincode_Users"].unique())
# no_of_years = len(top_year["Year"].unique())

# st.sidebar.header("Filter year")


# year = st.sidebar.multiselect(
#     label=f" out of {no_of_years} years",
#     options=top_year["Year"].unique(),
#     default=top_year ["Year"].unique())

# state = st.sidebar.multiselect(
#     label=f" out of {no_of_states} states",
#     options=top_year["State_Users"].unique(),
#     default=top_year ["State_Users"].unique())

# district = st.sidebar.multiselect(
#     label=f" out of {no_of_years} District",
#     options=top_year["District_Users"].unique(),
#     default=top_year["District_Users"].unique())

# pincode = st.sidebar.multiselect(
#     label=f" out of {no_of_years} Pincode",
#     options=top_year["Pincode_Users"].unique())
# top_year["District_Users"] = top_year["District_Users"].astype(str)

# df_selection = top_year.query("Year==@year  & State_Users==@state")



# st.write(df_selection)



# # setting the KPI
# def Home():
    
#     state_count=pd.DataFrame(df_selection["State_Users"].unique())
#     state_count= state_count.count()
    
#     District_count=pd.DataFrame(df_selection["District_Users"].unique())
#     state_count= District_count.count()
    
#     pincode_count=pd.DataFrame(df_selection["Pincode_Users"].unique())
#     Pincode_count= pincode_count.count()
    

    
#     State_Average_Regestration = average_fuc(df_selection["S_RegisteredUsers"])
#     District_average_reges = average_fuc(df_selection["D_RegisteredUsers"])
#     pincode_average_reges = average_fuc(df_selection["P_RegisteredUsers"])
    
    
    
   
      
    
#     col1,col2,col3 = st.columns(3)
#     with col1:
#         st.info("State")
#         st.metric(value= state_count,label="Count")
#     with col2:
#         st.info("District ")
#         st.metric(value=District_count,label="Count")
#     with col3:
#         st.info("Pincode")
#         st.metric(value=pincode_count,label="count")
        
#     col4,col5,col6 = st.columns(3)
#     with col4:
#         st.info("State Registered Users")
#         st.metric(value=State_Average_Regestration,label="percentage")
        
#     with col5:
#         st.info("District Registered Users")
#         st.metric(value=District_average_reges,label="percentage")
#     with col6:
#         st.info("Pincode Registered users")
#         st.metric(value = pincode_average_reges,label="percentage")
        
    
        
#     with st.expander("Tabular"):
#         showData = st.multiselect("Filter: ",df_selection.columns)
#         st.write(df_selection[showData])   
# Home()


