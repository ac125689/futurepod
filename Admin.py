import streamlit as st

def podcast_audio(file_name,date,name_of_the_auther,type_of_podcast,tittle_of_podcast,Description_of_the_Podcast):
    st.header(date)
    st.subheader(tittle_of_podcast)
    st.caption(f'By: {name_of_the_auther}')
    st.write(f'Type of Podcast: {type_of_podcast}')
    st.write(Description_of_the_Podcast)
    st.audio(f'Podcast/{file_name}', format= 'audio/mp3')



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
                podcast_audio('test1.mp3','12/21/2022','abhi','lala','BOBO',"dvasdvasvasdfvkhsbdfvsbdfvosdnvfisdbvflnsdfvsdfvnlsdfvbsdofv")
            with tab2:
                st.subheader('Post')

        else:
            st.warning('Your not the Admin')



