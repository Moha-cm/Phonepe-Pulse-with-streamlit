import streamlit as st

#==================================================== setting the page configuration ======================================================================

st.set_page_config(page_title="Phonepe Pulse",layout="wide")
st.title("Phonepe Pulse Data Visualization and Exploration ")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)
st.subheader("Front page ")
st.sidebar.success("select a page above")
st.markdown(
    """
    # Extracting and Processing Data from the Phonepe Pulse Github Repository

    📊 The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner. Here are the steps to achieve this:

    1. **Extract data from the Phonepe pulse Github repository through scripting and clone it.**
    Clone the Phonepe pulse Github repository using Git Bash or any other suitable tool to fetch the data from the repository.

    2. **Transform the data into a suitable format and perform any necessary cleaning and pre-processing steps.**
    Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This step involves cleaning the data, removing any duplicates, and transforming the data into a suitable format for storage and retrieval.

    3. **Insert the transformed data into a MySQL database for efficient storage and retrieval.**
    Use MySQL or SQLite to store the transformed data for efficient storage and retrieval. This step involves creating a new database, defining the schema, and inserting the transformed data into the database.

    4. **Create a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually appealing manner.**
    Use Streamlit and Plotly in Python to create an interactive and visually appealing dashboard that displays the data in a user-friendly manner. This step involves creating a new Python script, defining the layout of the dashboard, and adding interactive elements such as dropdowns and sliders.

    5. **Fetch the data from the MySQL database to display in the dashboard.**
    Use Python to fetch the data from the MySQL database and display it in the dashboard. This step involves connecting to the database, querying the data, and displaying it in the dashboard.
    """
)

# ====================================================================================================================================================