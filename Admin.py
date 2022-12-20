import streamlit as st
import datetime as dt

h = dt.datetime.now().hour
m = dt.datetime.now().minute



def admin():
    st.header('Admin login')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password',type='password')
    if st.sidebar.checkbox("Login"):
        if password == f'ADMIN{h}{m}':
            st.success(f'Logined as {username}')
            tab1, tab2 = st.tabs(['Video or Podcast Uplode','comeing soon'])
            with tab1:
                st.subheader('Video or Podcast Uplode')
            with tab2:
                st.subheader('comeing soon')



