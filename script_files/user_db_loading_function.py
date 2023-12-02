import os
import glob
import json
import pandas as pd

# ------------------------------------------------------- Users Data ----------------------------------------------------------------------------


#================================================== getting the user_year data ===================================================================
def user_year_data(year_path):
  user_year_data = []
  for files_path in year_path :
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      total_registered_users  = data.get("data").get("aggregated").get("registeredUsers")
      number_of_app = data.get("data").get("aggregated").get("appOpens")

      if data.get("data").get("usersByDevice",None) == None:
        #print(total_registered_users,number_of_app)

        value1 = dict(Year=year,Total_registered_users=total_registered_users,Number_of_app=number_of_app)
        #print(value1)
        user_year_data .append(value1)


      else:
        for i in data.get("data").get("usersByDevice"):
          brand = i.get("brand",None)
          total_transcation = i.get("count",None)
          per_share_current_device = i.get("percentage",None)
          #print(total_registered_users,number_of_app,brand,total_transcation,per_share_current_device)

          value2 = dict(Year=year,Total_registered_users=total_registered_users,Number_of_app=number_of_app,Brand=brand,Total_transcation=total_transcation,Per_share_current_device=per_share_current_device)
          #print(value2)
          user_year_data.append(value2)
  print("\n ")
  
  print(f"user  for the year is collected  as {type(user_year_data)}")
  return  user_year_data






#========================================================= getting the users state data ===========================================================
def state_user_data(state_path):
  user__state_data = []
  for files_path in state_path :
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      state = filename_list[-3]
      total_registered_users  = data.get("data").get("aggregated").get("registeredUsers")
      number_of_app = data.get("data").get("aggregated").get("appOpens")

      if data.get("data").get("usersByDevice",None) == None:
        #print(total_registered_users,number_of_app)

        value1 = dict(Year=year,Total_registered_users=total_registered_users,Number_of_app=number_of_app)
        #print(value1)
        user__state_data.append(value1)


      else:
        for i in data.get("data").get("usersByDevice"):
          brand = i.get("brand",None)
          total_transcation = i.get("count",None)
          per_share_current_device = i.get("percentage",None)
          #print(total_registered_users,number_of_app,brand,total_transcation,per_share_current_device)

          value2 = dict(State=state,Year=year,Total_registered_users=total_registered_users,Number_of_app=number_of_app,Brand=brand,Total_transcation=total_transcation,Per_share_current_device=per_share_current_device)
          #print(value2)
          user__state_data.append(value2)
  print(f"user for the state is collected  as {type(user__state_data)}")

  return   user__state_data
#print(year_user_ag_data)



########################################################### Map user ################################################################################


# Year user data
def year_data(year_path):

  map_year_list = []
  for files_path in year_path :
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
     # print(data)

      dict_keys = data.get("data").get("hoverData").keys()
      for i in [*dict_keys]:
        j =data.get("data").get("hoverData").get(f"{i}")
        state = i
        registeredUser = j.get("registeredUsers")
        appOpens = j.get("appOpens")

        state_dict = dict(State =  state,Year = year,RegisteredUser= registeredUser, AppOpens= appOpens)
        #print(state_dict)
        map_year_list.append(state_dict)
        
  print(f" years users is collected  as {type(map_year_list)}")

  return map_year_list



#============================================================ State users data ==============================================================
def state_data(state_path):

  state_list = []
  for files_path in state_path :
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      state_f = filename_list[-3]
      #print(data)

      dict_keys = data.get("data").get("hoverData").keys()

      for i in [*dict_keys]:
        j =data.get("data").get("hoverData").get(f"{i}")
        state = i
        registeredUser = j.get("registeredUsers")
        appOpens = j.get("appOpens")

        state_dict = dict(State=state_f, District =  state,Year = year,RegisteredUser= registeredUser, AppOpens= appOpens)
        #print(state_dict)
        state_list.append(state_dict)
        
  print(f"state users is collected  as {type(state_list)}")

  return state_list

########################################################## Top user ################################################################################

# top state and district and pincode of the year
def top_year_data(year_path):

  district_list = []
  pincode_list = []
  state_list = []
  for files_path in year_path:
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      #state = filename_list[-3]

      for  each_state in data.get("data").get("states"):
        users = each_state.get("name")
        registeredUsers =  each_state.get("registeredUsers")
        state_dict = dict(Year = year,State_Users=users,S_RegisteredUsers=registeredUsers)
        state_list.append(state_dict)

      for  each_district in data.get("data").get("districts"):
        users = each_district.get("name")
        registeredUsers = each_district.get("registeredUsers")
        dictrict_dict = dict(D_Year = year,District_Users=users,D_RegisteredUsers=registeredUsers)
        district_list.append(dictrict_dict)


      for pincodes in data.get("data").get("pincodes"):
        users = pincodes.get("name")
        registeredUsers = pincodes.get("registeredUsers")
        pincode_dict = dict(P_Year = year,Pincode_Users=users,P_RegisteredUsers=registeredUsers)

        pincode_list.append(pincode_dict)
  print(f"Transaction  for the year  is collected  as {type(pincode_list)}")

  return state_list,district_list,pincode_list


#======================================================= Top District and pincode of the  each state ============================================
def top_state_data(state_path):

  district_list = []
  pincode_list = []
  state_list = []
  for files_path in state_path:
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      state = filename_list[-3]
     # print(data)

      for  each_district in data.get("data").get("districts"):
        users = each_district.get("name")
        registeredUsers = each_district.get("registeredUsers")
        dictrict_dict = dict(State = state,Year = year,District_Users=users,RegisteredUsers=registeredUsers)
        district_list.append(dictrict_dict)


      for pincodes in data.get("data").get("pincodes"):
        users = pincodes.get("name")
        registeredUsers = pincodes.get("registeredUsers")
        pincode_dict = dict(State = state,Year = year,Pincode=users,RegisteredUsers=registeredUsers)

        pincode_list.append(pincode_dict)
  print(f"Transaction  for the year  is collected  as {type(pincode_list)}")
 
  return district_list,pincode_list

#--------------------------------------------------------------------------------------------------------------------------------------------------