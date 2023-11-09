import streamlit as st
#from streamlit_option_menu import option_menu

st.set_page_config(page_title="Phonepe Pulse",layout="wide")
st.title("Phonepe Pulse Data Visualization and Exploration ")
st.markdown("<style>div.block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)
st.subheader("Front page ")
st.sidebar.success("select a page above")




#st.write(youtube)


#st.write(channel_ids)

# if button1 :
    
#     channel_ids = validate_id(channel_id)
#     channel_data = get_channel_data(youtube,channel_ids)
#     playlist_ids = get_playlist_info(youtube,channel_data)
#     video_ids = playlist_video_list(youtube,channel_ids)
#     video_data = get_video_contents(youtube,video_ids)
#     comments = get_comments(youtube,video_ids)
        
#     if 'channel_data' not in st.session_state:
#         st.session_state.channel_data = channel_data
#     if 'playlist_ids' not in st.session_state:
#         st.session_state.playlist_ids = playlist_ids
#     if 'video_ids' not in st.session_state:
#         st.session_state.video_ids = video_ids
#     if 'video_data' not in st.session_state:
#         st.session_state.video_data =  video_data
#     if 'comments' not in st.session_state:
#         st.session_state.comments = comments 
    
#     st.write(channel_data[0],playlist_ids[0],video_data[0],comments[0])
#     st.balloons()