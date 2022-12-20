import streamlit as st
import datetime as dt
import sqlite3 as sq
conn = sq.connect('data.db')
c  = conn.cursor()

#def create_data()


def admin():
    st.header('Admin login')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password',type='password')
    if st.sidebar.checkbox("Login"):
        if password == 'ADMINOFHSS':
            st.success(f'Logined as {username}')
            tab1, tab2 = st.tabs(['Video or Podcast Uplode','Looking at all the post'])
            with tab1:
                st.subheader('Video or Podcast Uplode')
                name = st.text_input("Name of the author if they don't want there name posted type anonymous")
                type_of_podcast = st.text_input('What type of podcast it is?')
                tittle = st.text_input('Tittle of the podcast')
                description = st.text_area('Description of the Podcast')
                date = dt.datetime.now().date
                vid = st.file_uploader('Upload the Podcast here',accept_multiple_files=False)
            with tab2:
                st.subheader('Post')

        else:
            st.warning('Your not the Admin')



