import streamlit as st
from transaction_data_retrival import *
import plotly.express as px 
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# set tha page title 

st.title(" Ttansaction  Data Analysis based on    Year")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)



transaction_data = get_user()
year_data  = pd.DataFrame(transaction_data[0])
state_data =pd.DataFrame(transaction_data[1])

# st.write(year_data.nunique())
# st.write(state_data.nunique())



#total 
no_of_years = len(year_data["Year"].unique())
no_of_payment_reasons = len(year_data["Payment_reason"].unique())



# setting the sidebar menu

st.sidebar.header("Filter year")
year = st.sidebar.multiselect(
    label=f" out of {no_of_years} years",
    options=year_data ["Year"].unique(),
    default=year_data ["Year"].unique())

st.sidebar.header("Filter Payments")
payment = st.sidebar.multiselect(
    label=f" out of {no_of_payment_reasons} Payments",
    options=year_data ["Payment_reason"].unique(),
    default=year_data["Payment_reason"].unique())


# year1 = year
# payment1 = payment
df_selection = year_data.query(
    "Year==@year  & Payment_reason==@payment")

state_df_selection = state_data.query(
    "Year==@year  & Payment_reason==@payment")

no_of_state = len(state_df_selection["State"].unique())

st.sidebar.header("Filter States")
state = st.sidebar.multiselect(
    label=f" out of {no_of_state} states",
    options=state_df_selection["State"].unique(),
    default=state_df_selection["State"].unique())

state_df_selection = state_df_selection.query("State==@state")

# st.dataframe(df_selection)
# st.dataframe(state_df_selection)


def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)


#Setting the KPI
def Home():
    
    # for year
    df_selection["Total_value"]=df_selection['Total_value'].abs()
    df_selection["Total_transcation"]=df_selection['Total_transcation'].abs()
    paymnet_count=pd.DataFrame(df_selection["Payment_reason"].unique())
    paymnet_count= paymnet_count.count()
    year_trans_percentage = average_fuc(df_selection["Total_transcation"])
    year_value_percentag = average_fuc(df_selection["Total_value"])
    
    # for state
    state_df_selection["Total_value"]=state_df_selection['Total_value'].abs()
    state_df_selection["Total_transcation"]=state_df_selection['Total_transcation'].abs()
    state_count = pd.DataFrame(state_df_selection["State"].unique())
    state_count =state_count.count()
    state_trans_percentage = average_fuc(state_df_selection["Total_transcation"])
    state_value_percentage = average_fuc(state_df_selection["Total_value"])
    #st.write(state_count, state_trans_percentage,state_value_percentage )# for year KPI   

    col1,col2,col3 = st.columns(3)

    with col1:
        st.info("Payment Types")
        st.metric(value=paymnet_count,label="Count")
    with col2:
        st.info("Yearly Transaction")
        st.metric(value=year_trans_percentage ,label="percentage")
    with col3:
        st.info("Yearly  Value")
        st.metric(value=year_value_percentag ,label="percentage")
    
    # for state 
    col4,col5,col6 =st.columns(3)
    with col4:
        st.info("state")
        st.metric(value=state_count,label="Count")
        
    with col5:
        st.info("State Transaction")
        st.metric(value=state_trans_percentage,label="percent")
    with col6:
        st.info("State Value")
        st.metric(value=state_value_percentage,label="percent")
    
    with st.expander("Yearly Table"):
        showData = st.multiselect("Filter: ",df_selection.columns)
        st.write(df_selection[showData])
        
    
        st.metric(value=paymnet_count,label="Count")
        
    with st.expander("State Table"):
        showData = st.multiselect("Filter: ",state_df_selection.columns)
        st.write(state_df_selection[showData])
        
    
Home()
def grp_transaction_sum():
    c1,c2=st.columns(2)
    #year
    with c1:
        top_emp = df_selection.groupby('Payment_reason')['Total_transcation'].sum()
        fig = px.bar( x=top_emp.index, y=top_emp.values,color=top_emp.index,title="Year Transaction sum") 
        st.plotly_chart(fig)
        st.write("Yearly Total Transcation",top_emp)
    
    ##state
    with c2:
        
        top_emp = state_df_selection.groupby('Payment_reason')['Total_transcation'].sum()
        fig = px.bar( x=top_emp.index, y=top_emp.values,color=top_emp.index,title="State Year Transaction sum") 
        st.plotly_chart(fig)
        st.write("Yearly Total Transcation",top_emp)
        
       
        
        
   
    # st.write("State Total Transcation",top_emp)  
        
grp_transaction_sum()



def v():
    
    
    
    
    cl2,cl3 = st.columns(2) 
    with cl2:
        a =state_df_selection.groupby(["Payment_reason","Year"])["Total_transcation"]
        c =a.agg(["mean","min","max","count","sum"])
        b = pd.DataFrame(c)
        st.write("Transcation Info Grouped on Payment reason and Year",b)    
        # st.dataframe(b)
        
    with cl3: 
        a =state_df_selection.groupby(["Payment_reason","Year"])["Total_value"]
        c =a.agg(["mean","min","max","count","sum"])
        b = pd.DataFrame(c)   
        st.write("Values Info Grouped on Payment reason and Year",b) 
v()
  

