import os
import glob
import json
import pandas as pd

# data folder 
# year 
def data_year(path):
  list_year_data = []
  for files_path in path:
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      data_duration_from = data.get("data").get("from")
      data_duration_to = data.get("data").get("to")
      transaction_list = data.get("data").get("transactionData") # list
      for  each_transcation in transaction_list:
        #print(each_transcation)
        payment_reason = each_transcation.get("name")
        for i in each_transcation.get("paymentInstruments"):
          total_transcation = i.get("count")
          total_value =i.get("amount")
          data_dict = dict( Year= year,Data_duration_from=data_duration_from,Data_duration_to = data_duration_to,Payment_reason= payment_reason,Total_transcation=total_transcation, Total_value =  total_value)
          list_year_data.append(data_dict)
          
  print(f"The year traction data is  is collected  as {type( list_year_data)}")
  return    list_year_data


def state_data(state_path):
    state_list_year_data = []
    for files_path in state_path:
        with open(files_path, 'r') as f:
            data = json.load(f)
            filename_list = files_path.split("\\")
            year = filename_list[-2]
            state  = filename_list[-3]
            data_duration_from = data.get("data").get("from")
            data_duration_to = data.get("data").get("to")
            transaction_list = data.get("data").get("transactionData") # list
            for  each_transcation in transaction_list:
                #print(each_transcation)
                payment_reason = each_transcation.get("name")
                for i in each_transcation.get("paymentInstruments"):
                    total_transcation = i.get("count")
                    total_value =i.get("amount")
                    data_dict = dict(State =state ,Year= year,Data_duration_from=data_duration_from,Data_duration_to = data_duration_to,Payment_reason= payment_reason,Total_transcation=total_transcation, Total_value =  total_value)
                    state_list_year_data.append(data_dict)
    print(f"State transaction for the year is collected  as {type(state_list_year_data)}")

    return    state_list_year_data

##############################################################################################################################################
#******************************************    Map  File ***********************************************************************************


# Getting the year transaction data

def map_year_data(year_path):
  map_year_list = []
  for files_path in year_path :
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]

      for i in data.get("data").get("hoverDataList"):
        name = i.get("name")
        for j in i.get("metric"):
          total_transactions = j.get("count")
          total_value =j.get("amount")

          val = dict(Year = year,State_name=name,Total_transactions = total_transactions,Total_value=total_value)
          #print(val)
          map_year_list.append(val)
          
  print(f"Transaction  for the year  is collected  as {type(map_year_list)}")
          
  return map_year_list



# State transaction 
def map_state_data(state_path):
  map_state_list = []
  for files_path in state_path :
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      state= filename_list[-3]
      #print(state)
      #print(data)

      for i in data.get("data").get("hoverDataList"):
        name = i.get("name")
        for j in i.get("metric"):
          total_transactions = j.get("count")
          total_value =j.get("amount")

          val = dict(State=state,Year = year,District_Name=name,Total_transactions = total_transactions,Total_value=total_value)
          #print(val)
          map_state_list.append(val)
          
  print(f"Transaction  for the state  is collected  as {type(map_state_list)}")
  return map_state_list


#################################################################################################################################################
################################################## TOP transaction ###############################################################################

def top_year_data(year_path):
  state_list = []
  district_list = []
  pincode_list = []
  for files_path in year_path:
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      #print(year)

      for each_state in data.get("data").get("states"):
        state = each_state.get("entityName")
        total_transactions = each_state.get("metric").get("count")
        total_value = each_state.get("metric").get("amount")

        state_dict = dict(  Year=year,State = state,S_Total_transactions=total_transactions,S_Total_value =total_value)
        state_list.append(state_dict)

      for each_district in data.get("data").get("districts"):
        district = each_district.get("entityName")
        total_transactions = each_district.get("metric").get("count")
        total_value = each_district.get("metric").get("amount")

        dictrict_dict = dict(D_Year=year,District= district,D_Total_transactions=total_transactions,D_Total_value =total_value)
        #state_list.append( dictrict_dict)
        district_list.append(dictrict_dict)

      for pincodes in data.get("data").get("pincodes"):
        pincode= pincodes.get("entityName")
        total_transactions = pincodes.get("metric").get("count")
        total_value = pincodes.get("metric").get("amount")

        pincode_dict = dict(P_Year=year,Pincode= pincode,P_Total_transactions=total_transactions,P_Total_value =total_value)

        pincode_list.append(pincode_dict)
  print(f"Transaction  for the year  is collected  as {type(pincode_list)}")
  #print(pincode_list)

  return  state_list,district_list,pincode_list




def top_state_data(state_path):

  district_list = []
  pincode_list = []
  for files_path in state_path:
    #print(files_path)
    with open(files_path, 'r') as f:
      data = json.load(f)
      filename_list = files_path.split("\\")
      year = filename_list[-2]
      state = filename_list[-3]
      #print(data)

      for each_district in data.get("data").get("districts"):
        district = each_district.get("entityName")
        total_transactions = each_district.get("metric").get("count")
        total_value = each_district.get("metric").get("amount")

        dictrict_dict = dict(State=state,Year=year,District= district,Total_transactions=total_transactions,Total_value =total_value)

        district_list.append(dictrict_dict)
        #print(dictrict_dict)

      for pincodes in data.get("data").get("pincodes"):
        pincode= pincodes.get("entityName")
        total_transactions = pincodes.get("metric").get("count")
        total_value = pincodes.get("metric").get("amount")
        pincode_dict = dict(State=state,Year=year,Pincode= pincode,Total_transactions=total_transactions,Total_value =total_value)
        pincode_list.append(pincode_dict)
       # print(pincode_dict)
       
  print(f"Transaction  for the year  is collected  as {type(pincode_list)}")
  return  district_list, pincode_list



