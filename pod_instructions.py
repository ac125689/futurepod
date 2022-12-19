import streamlit as st

write = """
Recordings without a chromebook:-
    1.Find the power cord at bottom of the cart and plug it to the wall
    2.Take a note of the number on your headset this corresponds to a channel on the control board
    3.Important! Adjust your voice levels to create a balanced sound (make sure the Green Dot are within the green lines)
    4.Press mute for unused microphones
    5.Press the “Record” button to begin recording
    6.When finished,  press “Record” again

Transferring your recording from the control panel to laptop or to a Chromebook:-
    1.Login to the media center podcasting Dell laptop (use your first part of your email address and password) or  you can use your Chromebook to transfer the recording 
    2.Connect the USB cord from the control panel to the  Dell laptop  or your Chromebook
    3.Click on micro SD icon on the control panel Which is next to the music symbol icon
    4.Click on podcast transfer mode
    5.Click yes to transfer the recording
    6.If you're using your Chromebook 
        a.Then go to the files app on your Chromebook
        b.Then you should see RODECASTER At the bottom left in the file app
        c.Double click on RODE
        d.Double click on podcasts
        e.Double click (or select) audio recordings you recorded
    7.If you're using the Dell laptop
        a.then go to file explorer on the laptop 
        b.Then click on this PC
        c.Then you should see RODECASTER and  double click on it
        d.Double click on RODE
        e.Double click on podcasts
        f.End the first audio recording is you're recording
    8.Rename the podcast
    9.choose the platform anchor for your MP3 file
    10.save the MP3 file to downloads
    11.email the file to  yourself and added to drive
    12.Click “done” on the control panel

Removing your podcast from the control panel:-
    1.Click on the settings icon
    2.Press  podcast
    3.press the trash icon

Connecting Bluetooth devices to the control panel:-
    1.Turn on Bluetooth on the device that you choose to connect to the control panel
    2.Click on the Bluetooth symbol on the control panel 
    3.Now on your Bluetooth device  you should search for a name of a device  called “RODECASTER PRO”
    4.Click on that device name  and you should be connected to the control panel.

Adjusting the volume of the Bluetooth devices:-
    1.Under the Bluetooth button you should see a slider
    2.You can move the slider up and down to adjust the volume of the background  music.

"""
def instructions():
    st.title('Sutudents in WW-P HSS')
    st.header('Writen instructions for podcast station')
    st.markdown(write)