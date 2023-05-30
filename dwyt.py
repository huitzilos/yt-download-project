import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from pytube import YouTube
from googleapiclient.discovery import build
from pytube import YouTube
from flask import Flask, request, render_template, send_file
import tempfile
import os
# Configuración de la API de YouTube
API_KEY = "AIzaSyAocEc2RaxB59kggaEEIN0_YcVPGDY_BcI"  

# Crear un cliente para la API de YouTube
youtube = build("youtube", "v3", developerKey=API_KEY)


def search_video(query, max_results=10):
    response = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
    ).execute()

    videos = response["items"]
    return videos


st.set_page_config(page_title="YT - Download", page_icon=":tada:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#Animate
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

local_css("/content/drive/MyDrive/CP/style/style.css")

animate_image = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_szdrhwiq.json")


# ---- HEADER SECTION ----
with st.container():
    st.markdown(
        """
        <style>
        .centered-text {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        
    st_lottie(animate_image, height=200, key="coding")
    st.write("<h1 class='centered-text'>Welcome to YT Download</h1>", unsafe_allow_html=True)
    st.write("<h2 class='centered-text'>Final project of the subject basic computing, the page allows you to search for videos stored on YouTube and allows you to download the desired video.</h1>", unsafe_allow_html=True)
    st.write("<p class='centered-text'>Presented by: Diego Armando Torres López.</p>", unsafe_allow_html=True)

# ---- Contaienr ----
with st.container():
    st.write("---")        
    #Busqueda de videos
    search_query = st.text_input("Enter your search query")
    if st.button("Search"):
        if search_query:
            videos = search_video(search_query)

            for video in videos:
              video_title = video["snippet"]["title"]
              video_id = video["id"]["videoId"]
              video_url = f"https://www.youtube.com/watch?v={video_id}"
              video_image = video["snippet"]["thumbnails"]["default"]["url"]
              youtube_video = YouTube(video_url)
              video_title = youtube_video.title
              # Descarga el video a un archivo temporal
              stream = youtube_video.streams.get_highest_resolution()
              temp_file_path = os.path.join(tempfile.gettempdir(), f'{video_title}.mp4')
              archivo = stream.download(output_path=tempfile.gettempdir(), filename=f'{video_title}.mp4')
              #file = request.files(archivo)
              temp_file_prueba = tempfile.NamedTemporaryFile(delete=False)
              st.write("---")
              st.write("##")
              image_column, text_column = st.columns((1, 2))
              with image_column:
                st.image(video_image)
              with text_column:
                st.subheader(video_title)
                st.markdown(f"URL del video:  {video_url}")

                with open(archivo, "rb") as file:

                  btn =  st.download_button(
                      label="Download video",
                      data=file,
                      file_name=archivo,
                      mime="mp4"
                  )

