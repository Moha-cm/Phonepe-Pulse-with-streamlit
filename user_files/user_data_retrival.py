import streamlit as st

import pandas as pd
from sqlalchemy import create_engine, MetaData  


def get_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_user')
    df_year = pd.read_sql('SELECT * FROM user_year_aggregated',  con = cnx)
    df_statewise = pd.read_sql('SELECT * FROM user_state_aggregated',  con = cnx)
    
    return df_year,df_statewise


def map_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_user')
    map_year = pd.read_sql('SELECT * FROM map_user_year',  con = cnx)
    map_statewise = pd.read_sql('SELECT * FROM map_User_state',  con = cnx)
    
    return map_year,map_statewise

def top_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_user')
    top_year = pd.read_sql('SELECT * FROM user_top_year',  con = cnx)
    top_district = pd.read_sql('SELECT * FROM user_top_district',  con = cnx)
    top_pincode =  pd.read_sql('SELECT * FROM user_top_pincode',  con = cnx)
    
    return top_year,top_district,top_pincode



# user_year_aggregated
# user_state_aggregated

# map_user_year
# map_User_state

# user_top_year
# user_top_district
# user_top_pincode
    

    
    