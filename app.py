import streamlit as st
import numpy as np
from pickle import load
import pandas as pd
from prediction import show_predict_page
from About import About_diamond
from EDA import show_explore_page
import base64

page=st.sidebar.selectbox("Explore or predict or About",{"predict","Explore","About"})



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
if(page=="predict"):

    add_bg_from_local('diamonds.jpg')   

    show_predict_page()
elif(page=="Explore"):
    add_bg_from_local('diamond_eda.jpg') 
    show_explore_page()
else:
    add_bg_from_local('diamond_about.jpg') 
    About_diamond()