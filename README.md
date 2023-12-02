# Project Title :Phonepe-Pulse-with-streamlit

Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly

## Problem Statement

The Phonepe pulse Github repository contains a large amount of data  information related to Tarnsaction and Users in the states of India. ...

## Approach

1. **Data Extraction:**
   - Employ scripting to clone the Phonepe pulse Github repository, extracting data related to transactions and user activities.

2. **Data Transformation:**
   - Using **Python** libraries such as Pandas, to manipulate and preprocess the extracted data. This step involves cleaning, handling missing values, and transforming the data into a format conducive to analysis.

3. **Database Insertion:**
   - Utilize the "mysql-connector-python" library in Python to establish a connection with a MySQL database. Execute SQL commands to seamlessly insert the transformed data, ensuring efficient storage and retrieval.

4. **Dashboard Creation:**
   - Harness the capabilities of **Streamlit** and **Plotly** in Python to craft an interactive and visually captivating dashboard. This platform will serve as the gateway for users to explore and understand the insights derived from the data.

5. **Data Retrieval:**
   - Employ the "mysql-connector-python" library to connect to the MySQL database. Retrieve the data into a Pandas dataframe, enabling dynamic updates to the dashboard and ensuring users always have access to the latest information.

6. **Data Analysis**
   - Develop a comprehensive dashboard that facilitates an effective and insightful analysis of the data.

## Pyhton packages
```
pip install pandas

pip install streamlit

Pip install sqlalchemy

pip install PyMySQL

pip isstall git

pip install plotly
```

Dowload the source files from repo  and  use the bellow commandas to run

## Script Execution
## Data Extraction and Transformation

Run the following commands to extract and transform data related to users:
```
python .\Transaction_database.py
python .\users_datase.py
```
This script employs scripting to clone the Phonepe Pulse GitHub repository, then extracts users and transaction  data and store in database. 

## Run the application using the following command
```
streamlit run ./home.py
```
This will launch the Streamlit application.
