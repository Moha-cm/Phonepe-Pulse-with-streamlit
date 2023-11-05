import streamlit as st

import pandas as pd
from sqlalchemy import create_engine, MetaData  



def get_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_Transcation')
    df_year = pd.read_sql('SELECT * FROM transcation_year_aggregated',  con = cnx)
    df_statewise = pd.read_sql('SELECT * FROM transcation_state_aggregated',  con = cnx)
    
    return df_year,df_statewise


def map_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_Transcation')
    map_year = pd.read_sql('SELECT * FROM map_year_transcation',  con = cnx)
    map_statewise = pd.read_sql('SELECT * FROM ap_state_transcation',  con = cnx)
    
    return map_year,map_statewise

def top_user():
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_Transcation')
    top_year = pd.read_sql('SELECT * FROM top_year_transcation',  con = cnx)
    top_district = pd.read_sql('SELECT * FROM top_state_transcation',  con = cnx)
    top_pincode =  pd.read_sql('SELECT * FROM top_Pincode_transcation',  con = cnx)
    
    return top_year,top_district,top_pincode
























# transcation_year_aggregated
# transcation_state_aggregated

# map_year_transcation
#  map_state_transcation
 
#  top_year_transcation
#  top_state_transcation
#  top_Pincode_transcation
    

    
    