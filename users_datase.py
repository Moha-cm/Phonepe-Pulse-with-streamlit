import os
import glob
import json
import pandas as pd
from user_function import *

##################################################### users Data###############################################################################

Files = [r'D:\phone_pay_data\data\aggregated\user\country\india\*\*.json',r'D:\phone_pay_data\data\aggregated\user\country\india\state\*']


def get_user_paths(dir_path):
  path = []
  state = []

  for i in dir_path:
      data_files = glob.glob(i)
      path.append(data_files)

  for j in path[1]:
    data_files = glob.glob(f'{i}/*/*.json')
    state.append(data_files)

  return   path,state

year_path= get_user_paths(Files)


year_user_ag_data = user_year_data(year_path[0][0])
year_user_ag_data= pd.DataFrame(year_user_ag_data)
year_user_ag_data=year_user_ag_data.dropna()
year_user_ag_data_dict = {"Total_transcation":int}
year_user_ag_data = year_user_ag_data.astype(year_user_ag_data_dict)



state_path = year_path[1][0]
State_user_data = state_user_data(state_path)
state_user_ag_df = pd.DataFrame(State_user_data)
state_user_ag_data=state_user_ag_df.dropna()
state_user_ag_data_dict = {"Total_transcation":int}
state_user_ag_data = state_user_ag_data.astype(state_user_ag_data_dict)






########################################################### Map users ################################################################################
print("-----------------------------------------------------------------------------------------------------------------------")

Files = [r'D:\phone_pay_data\data\map\user\hover\country\india\*\*.json',r'D:\phone_pay_data\data\map\user\hover\country\india\state\*']


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
u_map_path = get_tansaction_paths(Files)

#map_path[0][0]

year_path = u_map_path[0][0]
year_user_map = year_data(year_path)
map_year_user = pd.DataFrame(year_user_map)
map_year_user_dict = {"RegisteredUser":int,"AppOpens":int }
map_year_user = map_year_user.astype(map_year_user_dict)
#print(map_year_user)

state_path = u_map_path[1][0]
state_user_map = state_data(state_path)
map_state_user = pd.DataFrame(state_user_map)
map_state_user_dict = {"RegisteredUser":int,"AppOpens":int }
map_state_user = map_state_user.astype(map_state_user_dict)
#print(map_state_user)


########################################################## top users ################################################################################
print("-----------------------------------------------------------------------------------------------------------------------")


Files = [r'D:\phone_pay_data\data\top\user\country\india\*\*.json',r'D:\phone_pay_data\data\top\user\country\india\state\*']

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

top_path = get_tansaction_paths(Files)

# year 
year_path = top_path[0][0]
y_top_state,y_top_district,y_top_pincode = top_year_data(year_path)
top_year_user_state = pd.DataFrame(y_top_state)
top_year_user_district  = pd.DataFrame(y_top_district)
top_year_user_pincode =  pd.DataFrame(y_top_pincode)

year_top_users = pd.concat([top_year_user_state,top_year_user_district, top_year_user_pincode], axis=1)
year_top_users = year_top_users.drop(['D_Year', 'P_Year'], axis=1)


# state
state_path = top_path[1][0]
top_district,top_pincode = top_state_data(state_path)
top_district_user = pd.DataFrame(top_district)
top_pincode_user = pd.DataFrame(top_pincode)
print("All worked")




def user_database(year_user_ag_data,state_user_ag_data,map_year_user,map_state_user,year_top_users,top_district_user,top_pincode_user):
 
    
    import pymysql
  
    
    from sqlalchemy import create_engine
    import mysql.connector

    # connecting to the server 

    mydb = mysql.connector.connect(host="localhost", user="root",password="")
    mycursor = mydb.cursor(buffered=True) 
    mycursor = mydb.cursor(buffered=True) 
    mycursor = mydb.cursor()
    print("Connection created ")
    print("Creating the database ")
    # create the database and creating the tables in the database 
    mycursor.execute("CREATE DATABASE phonepay_pulse_user")
    mycursor.execute("USE phonepay_pulse_user")
    cnx = create_engine('mysql+pymysql://root:@localhost/phonepay_pulse_user')
    


    # data folder 
    # transaction
    
    mycursor.execute("CREATE TABLE user_year_aggregated (Year VARCHAR(255),Total_registered_users INT,Number_of_app INT,Brand VARCHAR(255),Total_transcation INT,Per_share_current_device FLOAT)") 
    mycursor.execute("CREATE TABLE user_state_aggregated (State VARCHAR(255),Year VARCHAR(255),Total_registered_users INT,Number_of_app INT,Brand VARCHAR(255),Total_transcation INT,Per_share_current_device FLOAT)")
    
    # user data store 
    year_user_ag_data.to_sql('user_year_aggregated', con=cnx, if_exists='append', index=False)
    state_user_ag_data.to_sql('user_state_aggregated', con=cnx, if_exists='append', index=False)
    
    
    # map folder
    mycursor.execute("CREATE TABLE map_user_year (State VARCHAR (255),YEAR VARCHAR(255),RegisteredUser INT,AppOpens INT)")
    mycursor.execute("CREATE TABLE map_User_state(State VARCHAR (255),District VARCHAR(255),YEAR VARCHAR(255),RegisteredUser INT,AppOpens INT)")
    
    # user map data 
    map_year_user.to_sql('map_user_year', con=cnx, if_exists='append', index=False)
    map_state_user.to_sql('map_user_state', con=cnx, if_exists='append', index=False)
    
    # Top folder
    mycursor.execute("CREATE TABLE user_top_year (Year VARCHAR(255),State_Users VARCHAR(255),S_RegisteredUsers INT,District_Users VARCHAR(255),D_RegisteredUsers INT,Pincode_Users VARCHAR(255),P_RegisteredUsers INT)")
    mycursor.execute("CREATE TABLE user_top_district(State VARCHAR(255),Year VARCHAR(255),District_Users VARCHAR(255),RegisteredUsers INT )") 
    mycursor.execute("CREATE TABLE user_top_pincode(State VARCHAR(255),Year VARCHAR(255),Pincode VARCHAR(255),RegisteredUsers INT )") 
    
    # Top users data 
    year_top_users.to_sql('user_top_year', con=cnx, if_exists='append', index=False)
    top_district_user.to_sql('user_top_district', con=cnx, if_exists='append', index=False)
    top_pincode_user.to_sql('user_top_pincode', con=cnx, if_exists='append', index=False)
    print("Database created and the  values are stored !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return   "database created "
   
user_database(year_user_ag_data,state_user_ag_data,map_year_user,map_state_user,year_top_users,top_district_user,top_pincode_user)


