import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import time

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#assets
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_WdTEui.json")



st.set_page_config(page_title = "My Webpage", page_icon= ":dizzy:", layout = "wide")


with st.container():
    col1, col2 = st.columns([3,1])
    with col1:
        st.write("i wonder what got you here")
        
        st.title("The name's Hukkeri")
        st.subheader("Sourabh Hukkeri")
        st.write("I am a first year undergraduate student of Economics at IIT Roorkee")
        st.write("[You might want to check this out >](https://thefauxy.com/russian-missiles-rain-down-on-ukraine-as-rrr-song-nato-nato-wins-oscar/)")
    with col2: 
        st.write("")
        image_url = "https://i.imgur.com/iYkheW1.png"
        website_url = "https://twitter.com/SourabhHukkeri"

        image_link = f"<a href='{website_url}' target='_blank'><img src='{image_url}'></a>"

        st.markdown(image_link, unsafe_allow_html=True)




with st.container():
    
    st.write("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("What I do?")
        st.title("I develop")
        st.write("feelings in women's hearts ;)")  
        st.write("")
        st.write("Frankly, I'm exploring various fields of the software industry such as Web/App Development, Cybersecurity, Web3 etc")
        st.write("I am thrilled to embark on the journey of learning to develop and hopefully join MDGspace.")
    with col2:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    
    st.write("---")
    st.subheader("A video from the Peaky Blinders coz why not")

    video_file = open('peaky.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
