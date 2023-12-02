import streamlit as st

import pandas as pd
from sqlalchemy import create_engine, MetaData  


# --------------------------------------------------- Retrival data from SQL database ------------------------------------------------------------------


#======================================================= Getting the Users data from =======================================================

@st.cache_data
def get_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_user')
    df_year = pd.read_sql('SELECT * FROM user_year_aggregated',  con = cnx)
    df_statewise = pd.read_sql('SELECT * FROM user_state_aggregated',  con = cnx)
    
    return df_year,df_statewise

# ============================================================== Getting the map users data  ==================================================================================================================================================

@st.cache_data
def map_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_user')
    map_year = pd.read_sql('SELECT * FROM map_user_year',  con = cnx)
    map_statewise = pd.read_sql('SELECT * FROM map_User_state',  con = cnx)
    
    return map_year,map_statewise

# ================================================================ Top users data  =======================================================================================================================================

@st.cache_data
def top_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_user')
    top_year = pd.read_sql('SELECT * FROM user_top_year',  con = cnx)
    top_district = pd.read_sql('SELECT * FROM user_top_district',  con = cnx)
    top_pincode =  pd.read_sql('SELECT * FROM user_top_pincode',  con = cnx)
    
    return top_year,top_district,top_pincode
    
# ------------------------------------------------------------------------------------------------------------------------------------------------
    
    