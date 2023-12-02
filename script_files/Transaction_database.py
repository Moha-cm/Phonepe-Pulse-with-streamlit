# Aggregated file source 
from Transaction_db_loading_function import *

import os
import glob
import json
import pandas as pd

# ----------------------------------------------------------------- Trandsaction Data ---------------------------------------------------------------

#========================================================== Getting the all paths of transaction ====================================================
Files = [r'D:\phone_pay_data\data\aggregated\transaction\country\india\*\*.json',r'D:\phone_pay_data\data\aggregated\transaction\country\india\state\*']

def get_tansaction_paths(dir_path):
  path = []
  state = []

  for i in dir_path:
      data_files = glob.glob(i)
      path.append(data_files)

  for j in path[1]:
    data_files = glob.glob(f'{i}\*\*.json')
    state.append(data_files)
  print(" the folder location was been processed") 

  return   path,state


ag_trans_path = get_tansaction_paths(Files)


# ===================================================== Aggregated Data for year ==================================================================

year_data_Report = data_year(ag_trans_path[0][0])

ag_year = pd.DataFrame(year_data_Report)
ag_year_dict = {"Total_value":int}
ag_year = ag_year.astype(ag_year_dict)
#print(ag_year)

#========================================================= Aggregated data fro state ===============================================================

state_data_Report = state_data(ag_trans_path[1][0])
state_agreagated_Data = pd.DataFrame(state_data_Report)
state_agreagated_Data_dict = {"Total_value":int}
state_agreagated_Data = state_agreagated_Data.astype(state_agreagated_Data_dict)
#print(state_agreagated_Data)

print("------------------------------------------------------------------------------")


#===================================================== folder path===========================================================================

Files = [r'D:\phone_pay_data\data\map\transaction\hover\country\india\*\*.json',r'D:\phone_pay_data\data\map\transaction\hover\country\india\state\*']

def get_tansaction_paths(dir_path):
  path = []
  state = []

  for i in dir_path:
      data_files = glob.glob(i)
      path.append(data_files)

  for j in path[1]:
    data_files = glob.glob(f'{i}\*\*.json')
    state.append(data_files)

  return   path,state

#============================================== Getting the year and state transaction map path ===================================================
t_map_path = get_tansaction_paths(Files)
Map_year_data= map_year_data(t_map_path[0][0])
trans_map_year = pd.DataFrame(Map_year_data)
trans_map_year_dict = {"Total_value":int}
trans_map_year = trans_map_year.astype(trans_map_year_dict)


#=================================================== For map transaction of state ================================================================

Map_state_data= map_state_data(t_map_path[1][0])
trans_map_state =pd.DataFrame(Map_state_data)
trans_map_state_dict = {"Total_value":int}
trans_map_state = trans_map_state.astype(trans_map_state_dict)
print(trans_map_state.info())

#============================================================ TOP transaction =====================================================================
print("---------------------------------------------------------------------------------------------")

Files = [r'D:\phone_pay_data\data\top\transaction\country\india\*\*.json',r'D:\phone_pay_data\data\top\transaction\country\india\state\*']

def get_tansaction_paths(dir_path):
    path = []
    state = []
    for i in dir_path:
        data_files = glob.glob(i)
        path.append(data_files)
    for j in path[1]:
        data_files = glob.glob(f'{i}\\*\\*.json')
        state.append(data_files)

    return   path,state


t_top_path =get_tansaction_paths(Files)

year_path = t_top_path[0][0]
# print(year_path)

state,district,pincode = top_year_data(year_path)

#  year
top_trans_state = pd.DataFrame(state)
top_trans_district = pd.DataFrame(district)
top_trans_pincode = pd.DataFrame(pincode)
top_trans_year = pd.concat([top_trans_state,top_trans_district,top_trans_pincode],axis=1)
top_trans_year = top_trans_year.drop(['D_Year','P_Year'], axis=1)



# state path
state_path = t_top_path[1][0]
S_district, s_pincode = top_state_data(state_path)
top_state_district = pd.DataFrame(S_district)
top_state_pincode = pd.DataFrame(s_pincode)
# print(top_state_pincode)
# print(top_state_district)

print("All finished ")




############################################################# Storing to the data to database ##################################################

#db_conncection()

import pandas as pd 

def Trasaction_database(ag_year,state_agreagated_Data,trans_map_year,trans_map_state, top_trans_year, top_state_district, top_state_pincode):
    
    import pymysql
    #import mysql.connector
    import mysql.connector
    
    from sqlalchemy import create_engine

    # connecting to the server 
    
    mydb = mysql.connector.connect(host="localhost", user="root",password="")
    mycursor = mydb.cursor(buffered=True) 
    mycursor = mydb.cursor(buffered=True) 
    mycursor = mydb.cursor()
    print("Connection created ")
    print("Creating the database ")
    # create the database and creating the tables in the database 
    mycursor.execute("CREATE DATABASE phonepay_pulse_Transcation")
    mycursor.execute("USE phonepay_pulse_Transcation")
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_Transcation')
    

    
    # data folder 
    # transaction
    mycursor.execute("CREATE TABLE transcation_year_aggregated (Year VARCHAR(255), Data_duration_from INT, Data_duration_to INT, Payment_reason VARCHAR(255), Total_transcation INT, Total_value INT)")
    mycursor.execute("CREATE TABLE transcation_state_aggregated (State VARCHAR(255),Year VARCHAR(255), Data_duration_from INT, Data_duration_to INT, Payment_reason VARCHAR(255), Total_transcation INT, Total_value INT)")
    
    #store the data 
    ag_year.to_sql('transcation_year_aggregated', con=cnx, if_exists='append', index=False) 
    state_agreagated_Data.to_sql('transcation_state_aggregated', con=cnx, if_exists='append', index=False)
    
    
    
    # Map folder
    # Transaction 
    mycursor.execute("CREATE TABLE map_year_transcation (Year VARCHAR(255), State_name VARCHAR(255), Total_transactions INT,Total_value  INT)")
    mycursor.execute("CREATE TABLE map_state_transcation ( State VARCHAR(255), Year VARCHAR (255),District_Name VARCHAR(255),Total_transactions INT,Total_value  INT)")
    
    # store the map data 
    trans_map_year.to_sql('map_year_transcation', con=cnx, if_exists='append', index=False)
    trans_map_state.to_sql('map_state_transcation', con=cnx, if_exists='append', index=False)
    
    
    
    
    # Top transaction
    mycursor.execute("CREATE TABLE top_year_transcation (Year VARCHAR(255), State VARCHAR(255),S_Total_transactions INT,S_Total_value  INT,District VARCHAR(255),D_Total_transactions INT,D_Total_value INT,Pincode VARCHAR(255),P_Total_transactions INT,P_Total_value INT )")
    mycursor.execute("CREATE TABLE top_state_transcation ( State VARCHAR(255),Year VARCHAR(255),District VARCHAR(255),Total_transactions INT,Total_value  INT)")
    mycursor.execute("CREATE TABLE top_Pincode_transcation ( State VARCHAR(255),Year VARCHAR(255),Pincode VARCHAR(255),Total_transactions INT,Total_value  INT)")
    
    # store the top data 
    top_trans_year.to_sql('top_year_transcation', con=cnx, if_exists='append', index=False)
    top_state_district.to_sql('top_state_transcation', con=cnx, if_exists='append', index=False)
    top_state_pincode.to_sql('top_Pincode_transcation', con=cnx, if_exists='append', index=False)
    
    
    print("Database created and the  values are stored !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return   " User database created "

Trasaction_database(ag_year,state_agreagated_Data,trans_map_year,trans_map_state, top_trans_year, top_state_district, top_state_pincode)


# ---------------------------------------------------------------------------------------------------------------------------------------------------