import streamlit as st
import plotly.express as px 
from transaction_data_retrival import *
import plotly.graph_objs as go
import geopandas as gpd
from shapely.geometry import Point  
from streamlit_folium import st_folium
import folium

# set tha page title 
def set_page():
    st.set_page_config(layout="wide")
    st.title("Transaction Data Analysis")
    st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)
    st.write("This is for Transaction detatils")
    
set_page()



def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)


def setting_sidebar_dataframe():
    transaction_data = get_user()
    year_data  = pd.DataFrame(transaction_data[0])
    year_data["Total_value"]=year_data['Total_value'].abs()
    year_data["Total_transcation"]=year_data['Total_transcation'].abs()
    
    
    state_data =pd.DataFrame(transaction_data[1])
    state_data["Total_value"]=state_data['Total_value'].abs()
    state_data["Total_transcation"]=state_data['Total_transcation'].abs()

# retriving the data form the map data transaction for year and state
    top_data = map_user()
    m_year  = pd.DataFrame(top_data[0])
    m_district = pd.DataFrame(top_data[1])

# getting the top states, district and pincode 
    top_data = top_user()
    top_year  = pd.DataFrame(top_data[0])
    top_district = pd.DataFrame(top_data[1])
    top_pincode = pd.DataFrame(top_data[2])

#total  unique values 
    no_of_years = len(year_data["Year"].unique())
    
# setting the sidebar menu

    st.sidebar.header("Filter year")
    year = st.sidebar.multiselect(
        label=f" out of {no_of_years} years",
        options=["2018","2019","2020","2021","2022","2023"],
        default=["2018","2019","2020","2021","2022","2023"],
         key="year_multiselect")

# querying the year,state,top district,pincode with year data 
    year_selection = year_data.query("Year==@year")


    no_of_payment_reasons = len(year_selection["Payment_reason"].unique())

    st.sidebar.header("Filter Payments")
    payment = st.sidebar.multiselect(
        label=f" out of {no_of_payment_reasons} Payments",
        options=year_selection["Payment_reason"].unique(),
        default=year_selection["Payment_reason"].unique(),
         key="payment_multiselect")

    payment_selection = year_selection.query("Payment_reason==@payment")

# select the states based on the payemnt and year selection

    year1 = year

    state_selection = state_data.query(
        "Year==@year1  & Payment_reason==@payment")

    no_of_state = len(state_selection["State"].unique())
    st.sidebar.header("Filter States")
    state= st.sidebar.multiselect(
        label=f" out of {no_of_state} states",
        options=state_selection["State"].unique(),
        default=["tamil-nadu","uttar-pradesh","telangana","goa"],
         key="state_multiselect")
    state1 = state
    state_slelected = state_selection.query("State==@state") 
    

# select the district from the year,state from top district
    year2 = year1
    district_selection = top_district.query(
        "Year==@year2 & State==@state")

    no_of_district = len(district_selection["District"].unique())
    district= st.sidebar.multiselect(
        label=f" out of {no_of_district} district",
        options=district_selection["District"].unique(),
        default=district_selection["District"].unique(),
         key="District_multiselect")

    district_selected = district_selection.query("District==@district")

# select the pincode based on the year,state,payment from top pincode
    year3 = year2
    pin_selection = top_pincode.query("Year==@year3 & State==@state ")
    no_of_pincode = len(pin_selection ["Pincode"].unique())
    st.sidebar.header("Filter Pincode")
    pincode= st.sidebar.multiselect(
        label=f"out of{no_of_pincode} Pincode",
        options=pin_selection["Pincode"].unique(),
        default=pin_selection["Pincode"].unique(),
         key="pincode_multiselect")

    pin_selection = pin_selection.query("Pincode==@pincode")
    
    
    # setting the KPI for the datas
    #data = setting_sidebar_dataframe()
    year = payment_selection
    state = state_slelected
    district = district_selected
    pincode = pin_selection.dropna()

# for year data 
    year_Count = pd.DataFrame(year["Year"].unique())
    year_count= year_Count.count()
    Avg_per_Trans_y = average_fuc(year["Total_transcation"])
    Avg_per_Totall_y =average_fuc(year["Total_value"])


# KPI for year
    col1,col2,col3 = st.columns(3)
    with col1:
        st.info("Year ")
        st.metric(value= year_count,label="Count")
    with col2:
        st.info("Yearly Average Transaction")
        st.metric(value=Avg_per_Trans_y,label="percentage")
    with col3:
        st.info("Yearly Average value")
        st.metric(value=Avg_per_Totall_y,label="percentage")
    
    # # for state data

    state_count=pd.DataFrame(state["State"].unique())
    state_count= state_count.count()
    Avg_per_Trans_s = average_fuc(year["Total_transcation"])
    Avg_per_Totall_s =average_fuc(year["Total_value"])

# KPi  for state
    col1,col2,col3 = st.columns(3)
    with col1:
        st.info("State")
        st.metric(value= state_count,label="Count")
    with col2:
        st.info("State Average Transaction")
        st.metric(value=Avg_per_Trans_s,label="percentage")
    with col3:
        st.info("State Average value")
        st.metric(value=Avg_per_Totall_s,label="percentage")
        
    # # for District data

    Dis_count =pd.DataFrame(district["District"].unique())
    Dis_count = Dis_count.count()
    Avg_per_Trans_D = average_fuc(district["Total_transactions"])
    Avg_per_Totall_D =average_fuc(district["Total_value"])

# KPi  for district
    col1,col2,col3 = st.columns(3)
    with col1:
        st.info("District")
        st.metric(value= Dis_count,label="Count")
    with col2:
        st.info("Average Transaction on Top District")
        st.metric(value=Avg_per_Trans_D,label="percentage")
    with col3:
        st.info("Average value on Top District")
        st.metric(value=Avg_per_Totall_D,label="percentage")
        
        
    # # for pincode
    pin_count =pd.DataFrame(pincode["Pincode"].unique())
    pin_count = pin_count.count()
    Avg_per_Trans_p = average_fuc(pincode["Total_transactions"])
    Avg_per_Totall_p =average_fuc(pincode["Total_value"])

# KPi  for pincode
    col1,col2,col3 = st.columns(3)
    with col1:
        st.info("Pincode")
        st.metric(value= pin_count,label="Count")
    with col2:
        st.info("Average Transaction on Top Pincode ")
        st.metric(value=Avg_per_Trans_p,label="percentage")
    with col3:
        st.info("Average value on Top Pincode")
        st.metric(value=Avg_per_Totall_p,label="percentage")
        
        
    # Year plot 
    
    year = payment_selection
    state = state_slelected
    district = district_selected
    pincode = pin_selection.dropna()
    
    c1,c2 = st.columns(2)
    
    with c1:
        fig = px.bar(year,x="Year",y = "Total_transcation",color="Total_transcation",title=" Total Transaction in India")
        st.plotly_chart(fig)
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        
    with c2:
        fig = px.bar(year,x="Year",y = "Total_value",color="Total_value",title=" Total Value in India")
        st.plotly_chart(fig)
    
    
    c1,c2 =st.columns(2)
    
    with c1:
        fig =px.scatter(state,x = "Year",y ="Total_transcation",size="Total_value",color="Payment_reason")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)    
    with c2:
        fig =px.scatter(state,x = "Year",y ="Total_value",size="Total_value",color="Payment_reason")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)  
    
        
        
        
    # state 
    c1,c2 = st.columns(2)
    with c1:
        fig = px.bar(state,x="State",y = "Total_transcation",color="Payment_reason",title=" State Transaction in India",template="simple_white")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
    with c2:
        fig = px.bar(state,x="State",y = "Total_value",color="Payment_reason",title=" State Value in India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
    c1,c2 =st.columns(2)
    
    with c1:
        fig =px.scatter(state,x = "State",y ="Total_transcation",size="Total_value",color="Payment_reason")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)    
    with c2:
        fig =px.scatter(state,x = "State",y ="Total_value",size="Total_value",color="Payment_reason")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
    # district
    c1,c2 = st.columns(2)
    with c1:
        fig = px.bar(district,x="District",y = "Total_transactions",color="Total_transactions",title=" District Transaction in India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
    with c2:
        fig = px.bar(district,x="District",y = "Total_value",color="Total_value",title="District Value in India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
    c1,c2 =st.columns(2)
    
    with c1:
        fig =px.scatter(district,x = "District",y ="Total_transactions",size="Total_transactions",color="Total_transactions",title="District Transaction in India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)    
    with c2:
        fig =px.scatter(district,x = "District",y ="Total_value",size="Total_value",color="Total_value",title="District Value in India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
    
    
    # Pincode
    # c1,c2 = st.columns(2)
    # with c1:
    #     fig = px.bar(pincode,x="Pincode",y = "Total_transactions",color="Total_transactions",title=" Locatity Transaction in  India")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)
        
    # with c2:
    #     fig = px.bar(pincode ,x="Pincode",y = "Total_value",color="Total_value",title="Locatity Value in  India")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)
        
    # c1,c2 =st.columns(2)
    
    with c1:
        fig =px.scatter(pincode,x = "Pincode",y ="Total_transactions",size="Total_transactions",color="Total_value",title=" Locatity Transaction in  India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)    
    with c2:
        fig =px.scatter(pincode ,x = "Pincode",y ="Total_value",size="Total_value",color="Total_value",title=" Locatity value in  India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
    

    
    
    map_year_df = pd.read_csv(r"D:\Guvi project\states_transaction.csv")
    

    
    map_year  = map_year_df.query("State==@state1")
    # map_year_df = map_location()
    latitude = map_year["Latitude"]
    Longitude = map_year["Longitude"]
    data = pd.DataFrame({"LAT":latitude ,"LON":Longitude })
    st.header("States")
    st.map(data=data,zoom=4)
    
setting_sidebar_dataframe()
    