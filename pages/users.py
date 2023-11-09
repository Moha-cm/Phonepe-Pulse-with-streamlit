import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from users_data_retrival import * 
import folium


# set tha page title 
def set_page():
    st.set_page_config(layout="wide")
    st.title("Users Data Analysis")
    st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)
    st.write("This is for Users details")
set_page()



def average_fuc(x):
    mean_x = int(x.mean())
    max_x = int(x.max())
    avg =  (mean_x/max_x)*100
    return "{:.2f}".format(avg)


def setting_dataframe_sidebar():
 #reterving the  data from the database for  aggregated users year and state
    Total_user_data = get_user() # tuple with both year and state 
    year_data=pd.DataFrame(Total_user_data [0])
    state_data = pd.DataFrame(Total_user_data [1])

# retriving the data form the map data transaction for year and state
    top_data = map_user()
    map_data =map_user()
    year_map = map_data[0]
    year_state = map_data[1]

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
        options=year_data ["Year"].unique(),
        default=year_data ["Year"].unique())


# querying the year,state,top district,pincode with year data 
    year_selection = year_data.query("Year==@year")


# setting the brand side bar and querying
    no_of_brands = len(year_selection["Brand"].unique())
    st.sidebar.header("Filter Payments")
    Brand  = st.sidebar.multiselect(
        label=f" out of {no_of_brands} Brands",
        options=year_selection["Brand"].unique(),
        default=year_selection["Brand"].unique())

    Brand_selection = year_selection.query("Brand==@Brand")

# select the states based on the payemnt and year selection
    state_selection = state_data.query("Year==@year  & Brand==@Brand")

    no_of_state = len(state_selection["State"].unique())
    st.sidebar.header("Filter States")
    state= st.sidebar.multiselect(
        label=f" out of {no_of_state} states",
        options=state_selection["State"].unique(),
        default=["tamil-nadu","uttar-pradesh","telangana","goa"])

    state_slelected = state_selection.query("State==@state") 

# select the district from the year,state from map data

    district_selection = top_district.query("Year==@year & State==@state")

    no_of_district = len(district_selection["District_Users"].unique())
    st.sidebar.header("Filter District")
    district= st.sidebar.multiselect(
        label=f" out of {no_of_district} district",
        options=district_selection["District_Users"].unique(),
        default=district_selection["District_Users"].unique())

    district_selected = district_selection.query("District_Users==@district")

    # select the pincode based on the year,state,payment from top pincode
    pin_selection = top_pincode.query("Year==@year & State==@state ")
    no_of_pincode = len(pin_selection ["Pincode"].unique())
    st.sidebar.header("Filter Pincode")
    pincode= st.sidebar.multiselect(
        label=f"out of{no_of_pincode} Pincode",
        options=pin_selection["Pincode"].unique(),
        default=pin_selection["Pincode"].unique())

    pin_selection = pin_selection.query("Pincode==@pincode")
    
    
  # FOr Year to set KPI
    year_Count = pd.DataFrame(Brand_selection["Year"].unique())
    year_count= year_Count.count()
    Brand_count = pd.DataFrame(Brand_selection["Brand"].unique())
    Brand_count= Brand_count.count()
    Avg_per_Reges_y = average_fuc(Brand_selection["Total_registered_users"])
    Avg_per_Trans_y = average_fuc(Brand_selection["Total_transcation"])
    Avg_App =average_fuc(Brand_selection["Number_of_app"])
    Avg_share_device =Brand_selection["Per_share_current_device"].mean()
    
# KPI for year
    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.info("Year")
        st.metric(value= year_count,label="Count")
    with col2:
        st.info("Brand")
        st.metric(value=Brand_count,label="Count")
    with col3:
        st.info("Average Registeres users")
        st.metric(value=Avg_per_Reges_y,label="percentage")
    with col4:
        st.info("Yearly Average  users Transaction")
        st.metric(value=Avg_per_Trans_y,label="percentage")
    with col5:
        st.info("Yearly Average App users")
        st.metric(value=Avg_App,label="percentage")
    with col6:
        st.info("Yearly Average share on Device")
        st.metric(value=Avg_share_device,label="percentage")
    
    
    # for state
    #  Brand_selection,state_slelected,district_selected ,pin_selection
      # FOr Year to set KPI
    
    state_Count = pd.DataFrame(state_slelected["State"].unique())
    state_count=  state_Count.count()
    Brand_count = pd.DataFrame(state_slelected["Brand"].unique())
    Brand_count= Brand_count.count()
    Avg_per_Reges_s = average_fuc(state_slelected["Total_registered_users"])
    Avg_per_Trans_s = average_fuc(state_slelected["Total_transcation"])
    Avg_App_s =average_fuc(state_slelected["Number_of_app"])
    Avg_share_device_s =state_slelected["Per_share_current_device"].mean()
    
# KPI for state
    col1,col2,col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.info("State")
        st.metric(value= state_count,label="Count")
    with col2:
        st.info("Brand")
        st.metric(value=Brand_count,label="Count")
    with col3:
        st.info("Average Registeres users")
        st.metric(value=Avg_per_Reges_s,label="percentage")
    with col4:
        st.info( "Average State users Transaction")
        st.metric(value=Avg_per_Trans_s,label="percentage")
    with col5:
        st.info("Average State App users")
        st.metric(value=Avg_App_s,label="percentage")
    with col6:
        st.info("State Average share on Device")
        st.metric(value=Avg_share_device_s,label="percentage")
        
    # for top  district
    #  Brand_selection,state_slelected,district_selected ,pin_selection
    
    district_Count = pd.DataFrame(district_selected["District_Users"].unique())
    district_Count=  district_Count.count()
    Avg_per_Reges_d = average_fuc(district_selected["RegisteredUsers"])
    
    
    Pincode_Count = pd.DataFrame(pin_selection["Pincode"].unique())
    Pincode_Count=  Pincode_Count.count()
    Avg_per_Reges_p = average_fuc(pin_selection["RegisteredUsers"])
    
    
    
    # KPI for District and pincode
    col1,col2,col3,col4 = st.columns(4)
    # district
    with col1:
        st.info("District")
        st.metric(value= district_Count,label="Count")

    with col3:
        st.info(" Average  Registeres District users")
        st.metric(value=Avg_per_Reges_d,label="percentage")
        
    # Pincode
    with col2:
        st.info("Pincode")
        st.metric(value=Pincode_Count,label="Count")
    with col4:
        st.info(" Average Registeres pincode users")
        st.metric(value= Avg_per_Reges_p,label="percentage")
  
    #Brand_selection,state_slelected,district_selected ,pin_selection
    # Year plot 
    year_df = Brand_selection
    state_df = state_slelected
    district_df = district_selected
    pincode_df = pin_selection.dropna()
    
    c1,c2 = st.columns(2)
    
    with c1:
        fig = px.bar(year_df,x="Year",y = "Total_transcation",color="Brand",title=" Total User Transaction in India")
        st.plotly_chart(fig)
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        
    with c2:
        fig = px.bar(year_df,x="Year",y = "Total_registered_users",color="Brand",title=" Total User Registered in India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
    c3,c4 = st.columns(2)
    with c3:
        fig = px.bar(year_df,x="Year",y = "Number_of_app",color="Brand",title=" Registered App user in India")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
    with c4:
        fig = px.bar(year_df,x="Year",y = "Per_share_current_device",color="Brand",title=" Percentage Share in Device")
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
    
    # state plot -----------------
    
    c1,c2 = st.columns(2)
    
    with c1:
        fig = px.bar(state_df ,x="State",y = "Total_transcation",color="Brand",title=" State User Transaction in India",hover_data=["Year"])
        st.plotly_chart(fig)
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        
    with c2:
        fig = px.bar(state_df,x="State",y = "Total_registered_users",color="Brand",title=" State User Registered in India",hover_data=["Year"])
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
    c3,c4 = st.columns(2)
    with c3:
        fig = px.bar(state_df,x="State",y = "Number_of_app",color="Brand",title=" Registered App user in each State",hover_data=["Year"])
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
    with c4:
        fig = px.bar(state_df,x="State",y = "Per_share_current_device",color="Brand",title=" Percentage Share in Device",hover_data=["Year"])
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
    
    # District plot 
    
    c1,c2 = st.columns(2)

    with c1:
        fig = px.bar(district_df,x="District_Users",y = "RegisteredUsers",color="Year",title=" Pincode User Registered in India",hover_data=["State"])
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
    with c2:
        fig = px.bar( pincode_df,x="Pincode",y = "RegisteredUsers",color="Year",title=" Pincode User Registered in India",hover_data=["State"])
        fig.update_xaxes(showgrid =False)
        fig.update_yaxes(showgrid =False)
        st.plotly_chart(fig)
        
        
    map_year_df = pd.read_csv(r"D:\Guvi project\states_users.csv")
    

    
    map_year  = map_year_df.query("State==@state")
    # map_year_df = map_location()
    latitude = map_year["Latitude"]
    Longitude = map_year["Longitude"]
    data = pd.DataFrame({"LAT":latitude ,"LON":Longitude })
    st.header("States")
    st.map(data=data,zoom=10,use_container_width=500)
    
    
    
    
    # District plot 
    #district_df
    
    
    
    
    
    
    
    
    
    
    
    
    
    # c1,c2 =st.columns(2)
    
    # with c1:
    #     fig =px.scatter(year,x = "Year",y ="Number_of_app",size="Number_of_app",color="Brand")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)    
    # with c2:
    #     fig =px.scatter(year,x = "Year",y ="Per_share_current_device",size="Total_value",color="Payment_reason")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)  
    
        
        
        
    # # state 
    # c1,c2 = st.columns(2)
    # with c1:
    #     fig = px.bar(state,x="State",y = "Total_transcation",color="Payment_reason",title=" State Transaction in India",template="simple_white")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)
        
    # with c2:
    #     fig = px.bar(state,x="State",y = "Total_value",color="Payment_reason",title=" State Value in India")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)
        
    # c1,c2 =st.columns(2)
    
    # with c1:
    #     fig =px.scatter(state,x = "State",y ="Total_transcation",size="Total_value",color="Payment_reason")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)    
    # with c2:
    #     fig =px.scatter(state,x = "State",y ="Total_value",size="Total_value",color="Payment_reason")
    #     fig.update_xaxes(showgrid =False)
    #     fig.update_yaxes(showgrid =False)
    #     st.plotly_chart(fig)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

    return Brand_selection,state_slelected,district_selected ,pin_selection

setting_dataframe_sidebar()

